import os
import shutil
import datetime
import pyinotify
import logging

LOG_LEVEL = logging.INFO
LOG_FILE = './monitor.log'
"""
新建文件并且写入会产生CREATE event,MODIFY event,CLOSE_WRITE event
touch文件会产生 CREATE event,CLOSE_WRITE event
仅打开会产生 CLOSE_NOWRITE event
修改文件会产生
MODIFY event: 
CLOSE_WRITE event

删除文件会产生 DELETE event

"""
WEBSITE_DIR = '/mnt/d/wendell/codeEnv/wgp/AWD/WolfAwd/data/misc/defense_inotify/www'
WEBSITEBAK_DIR = '/mnt/d/wendell/codeEnv/wgp/AWD/WolfAwd/data/misc/defense_inotify/tmp/www'


class WebSiteEventHandler(pyinotify.ProcessEvent):
    logging.basicConfig(level=LOG_LEVEL, filename=LOG_FILE)
    # 自定义写入那个文件，可以自己修改

    logging.info("Starting monitor...")

    # 标记程序直接的删除行为, 防止循环调用
    is_delete_now = None
    is_modify_now = None
    is_delete_now_nomodify = None
    is_delete_now_nocreate = None
    is_restore_now_nomodify = []
    # def process_IN_CLOSE_NOWRITE(self, event):
    #         os.path.join(event.path, event.name), datetime.datetime.now()))
    #
    # def process_IN_CLOSE_WRITE(self, event):
    #
    #     # print("CLOSE_WRITE event:", event.pathname)
    #
    #     logging.info("CLOSE_WRITE event : %s  %s" % (
    #         os.path.join(event.path, event.name), datetime.datetime.now()))

    logging.basicConfig(level=logging.INFO, filename='./monitor.log')
    # 自定义写入那个文件，可以自己修改
    logging.info("Starting monitor...")

    def process_IN_ACCESS(self, event):

        logging.info("ACCESS event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_ATTRIB(self, event):

        logging.info("IN_ATTRIB event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_CLOSE_NOWRITE(self, event):

        logging.info("CLOSE_NOWRITE event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_CLOSE_WRITE(self, event):

        logging.info("CLOSE_WRITE event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_CREATE(self, event):

        logging.info("CREATE event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_DELETE(self, event):

        logging.info("DELETE event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_MODIFY(self, event):

        logging.info("MODIFY event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_OPEN(self, event):

        logging.info("OPEN event : %s  %s" % (os.path.join(event.path, event.name), datetime.datetime.now()))

    # 　实现删除恢复功能
    def restore_file(self, event):
        filepath = os.path.join(event.path, event.name)
        file_bak_path = filepath.replace(WEBSITE_DIR, WEBSITEBAK_DIR, 1)
        if os.path.exists(file_bak_path):
            shutil.copy(file_bak_path, filepath)
            print("restore", filepath)
            logging.info("restore : %s  %s" % (filepath, datetime.datetime.now()))

    def delete_file(self, event):
        filepath = os.path.join(event.path, event.name)
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            os.rmdir(filepath)