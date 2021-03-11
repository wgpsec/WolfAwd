import os
import time
from utils.logger import Logger
from utils.tools import parse_options
from library import all_attack_func
from library import all_guard_func
from library.core import Attacker
import importlib
import traceback
import threading


AWD_PATH = os.getcwd()
#这里可能没有权限要手动创建一个日志文件
LOGS_PATH = AWD_PATH + '/logs/logs.log'
logger = Logger(LOGS_PATH) 

class WolfAwd():
    def __init__(self, options):
        self.set_target = self.set_target_by_options(options)
        self.get_action_cmd = self.get_action_by_options(options)
        self.targets = self.get_target_by_options(options)
        self.command = options.command
        self.vulns = self.load_vuln_by_options(options)
        self.attacker = []
        self.loop = options.loop
        self.loop_time = options.loop_time
        # if options.command:
            # action(target_ip, target_port, command)

    #默认启用all_attack_func的方法
    def get_action_by_options(self, options):
        module = globals().get('all_' + options.module + '_func')
        return getattr(module, options.action)

    
    #生成IP列表
    def set_target_by_options(self, options):
        if options.config=="1":
            print("输入起始IP  终止IP  端口")
            print("例如：127.0.0.1 127.0.0.9 80")
            raw = input()
            start_target = raw.split()[0]
            end_target = raw.split()[1]
            port = raw.split()[2]
            start_D = start_target.split(".")[-1]
            end_D = end_target.split(".")[-1]
            with open(AWD_PATH+'/games/targets', 'w') as f:
                for i in range(int(start_D),int(end_D)+1):
                    target = start_target.split(".")[0]+"."+start_target.split(".")[1]+"."+start_target.split(".")[2]+"."+str(i)+":"+port+"\n"
                    f.write(target)
                f.close()
            return "已更新 ./games/targets 文件"


    #根据target文件获取地址
    def get_target_by_options(self, options):
        #没指定的话从targets文件里选取，按行读
        if not options.targets:
            with open(AWD_PATH+'/games/targets', 'r') as f:
                targets = f.readlines()
            return [tuple(i.strip().split(':')) for i in targets]
        #指定了的话就一个
        else:
            targets = options.target.split(':')
            return [tuple(i.strip().split(':')) for i in targets]



    def load_vuln_by_options(self, options):
        if options.vuln == '*':
            # to-do 自动加载所有poc
            pass
        vulns = options.vuln.split(' ')
        result = []
        for vuln in vulns:
            vuln = importlib.import_module('games.poc.' + vuln).vulnerable_attack
            result.append(vuln)
        return result



    #显示模块
    def run_action(self, target_ip, target_port, command=''):
        if not command:
            cmd = self.get_action_cmd(target_ip, target_port)
        else:
            cmd = self.get_action_cmd(target_ip, target_port, command)
        attacker = Attacker(target_ip, target_port, cmd, self.vulns)
        self.attacker.append(attacker)
        try:
            res = attacker.run()
            logger.info('%s:%s action 完成 结果如下  \n\n' % (target_ip, target_port)+res+"\n\n-------------------------")
        except Exception as e:
            res = '运行失败'
            logger.info(res)
            logger.warning(e)
            logger.debug(traceback.format_exc())


    #批量执行
    def run(self):
        while self.loop:
            for target_ip, tartget_port in self.targets:
                #改用多线程，不会卡住
                threading.Thread(target=self.run_action,args=(target_ip, tartget_port, self.command)).start()
            self.loop -= 1
            time.sleep(self.loop_time)
    
            
            
if __name__ == "__main__":
    logger.info('WolfAwd start ')
    #获取输入内容
    options = parse_options()
    awd = WolfAwd(options)
    awd.run()
