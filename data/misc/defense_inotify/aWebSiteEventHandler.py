import os
import shutil
import datetime
from . import pyinotify
import logging
from .config import WATCH_FLAG_ACCESS, LOG_LEVEL, LOG_FILE

"""
新建文件并且写入会产生CREATE event,MODIFY event,CLOSE_WRITE event
touch文件会产生 CREATE event,CLOSE_WRITE event
仅打开会产生 CLOSE_NOWRITE event
修改文件会产生
MODIFY event: 
CLOSE_WRITE event

删除文件会产生 DELETE event
s
"""
WEBSITE_DIR = '/var/www/html'
WEBSITEBAK_DIR = '/tmp/html'


class WebSiteEventHandler(pyinotify.ProcessEvent):

    logging.basicConfig(level=LOG_LEVEL, filename=LOG_FILE)
    # 自定义写入那个文件，可以自己修改

    logging.info("Starting monitor...")

    # 标记程序直接的删除行为, 防止循环调用
    is_delete_now = None
    is_modify_now = None
    is_delete_now_nomodify = None
    is_delete_now_nocreate = None
    is_modify_now_nomodify = []
    # def process_IN_CLOSE_NOWRITE(self, event):
    #         os.path.join(event.path, event.name), datetime.datetime.now()))
    #
    # def process_IN_CLOSE_WRITE(self, event):
    #
    #     # print("CLOSE_WRITE event:", event.pathname)
    #
    #     logging.info("CLOSE_WRITE event : %s  %s" % (
    #         os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_CREATE(self, event):

        # print("CREATE event:", event.pathname)
        filepath = os.path.join(event.path, event.name)
        logging.info("CREATE event : %s  %s" % (os.path.join(
            event.path, event.name), datetime.datetime.now()))
        if self.is_delete_now_nocreate == filepath:
            self.is_delete_now_nocreate = None
        else:
            self.delete_file(event)

    def process_IN_DELETE(self, event):

        print("DELETE event:", event.pathname)
        filepath = os.path.join(event.path, event.name)
        logging.info("DELETE event : %s  %s" % (os.path.join(
            event.path, event.name), datetime.datetime.now()))
        filepath = os.path.join(event.path, event.name)
        # 设置标记,防止循环调用
        self.is_delete_now_nocreate = filepath
        self.is_delete_now_nomodify = filepath

        self.restore_file(event)

    def process_IN_MODIFY(self, event):

        print("MODIFY event:", event.pathname)
        filepath = os.path.join(event.path, event.name)
        logging.info("MODIFY event : %s  %s" % (os.path.join(
            event.path, event.name), datetime.datetime.now()))
        # self.delete_file(event)
        if filepath in self.is_modify_now_nomodify:
            # 删除一次
            self.is_modify_now_nomodify.remove(filepath)
        else:
            # 阻止删除文件的循环调用
            self.is_delete_now_nomodify = filepath

            # 调用恢复文件会产生三次次 MODIFY event 事件,数组写入两次,防止循环调用
            self.is_modify_now_nomodify.append(filepath)
            self.is_modify_now_nomodify.append(filepath)
            self.is_modify_now_nomodify.append(filepath)
            # 恢复文件
            self.restore_file(event)

    # 　实现删除恢复功能
    def restore_file(self, event):
        filepath = os.path.join(event.path, event.name)
        file_bak_path = filepath.replace(WEBSITE_DIR, WEBSITEBAK_DIR, 1)
        head, tail = os.path.split(filepath)
        if os.path.exists(file_bak_path):
            if not os.path.exists(head):
                os.makedirs(head)
            if os.path.isfile(file_bak_path):
                shutil.copy2(file_bak_path, filepath)
            else:
                if not os.path.exists(filepath):
                    shutil.copytree(file_bak_path, filepath)
            print("restore", filepath)
            logging.info("restore : %s  %s" %
                         (filepath, datetime.datetime.now()))

    def delete_file(self, event):
        filepath = os.path.join(event.path, event.name)
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            shutil.rmtree(filepath)

    def process_IN_ACCESS(self, event):
        print("ACCESS event:", event.path)
        if event.path == WATCH_FLAG_ACCESS or event.path == WATCH_FLAG_ACCESS + '/':
            logging.warning("ACCESS event : %s  %s" % (os.path.join(
                event.path, event.name), datetime.datetime.now()))
            with open('/tmp/lock', 'w+') as f:
                f.write('1')
