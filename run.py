import os
from utils.logger import Logger
from utils.tools import parse_options
from library import all_attack_func
from library import all_guard_func
from library.core import Attacker
import importlib
AWD_PATH = os.getcwd()
LOGS_PATH = AWD_PATH + '/logs/logs.log'
logger = Logger(LOGS_PATH)

class WolfAwd():
    def __init__(self, options):
        self.get_action_cmd = self.get_action_by_options(options)
        self.targets = self.get_target_by_options(options)
        self.command = options.command
        self.vulns = self.load_vuln_by_options(options)
        self.attacker = []
        # if options.command:
            # action(target_ip, target_port, command)

    def get_action_by_options(self, options):
        module = globals().get('all_' + options.module + '_func')
        return getattr(module, options.action)

    def get_target_by_options(self, options):
        if not options.targets:
            with open(AWD_PATH+'/games/targets', 'r') as f:
                targets = f.readlines()
            return [tuple(i.strip().split(':')) for i in targets]
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

    def run_action(self, target_ip, target_port, command=''):
        if not command:
            cmd = self.get_action_cmd(target_ip, target_port)
        else:
            cmd = self.get_action_cmd(target_ip, target_port, command)
        attacker = Attacker(target_ip, target_port, cmd, self.vulns)
        self.attacker.append(attacker)
        res = attacker.run()
        logger.info('%s:%s action 完成 结果如下 ' % (target_ip, target_port))
        logger.info(res)
        logger.info('-------------------------')

    def run(self):
        for target_ip, tartget_port in self.targets:
            self.run_action(target_ip, tartget_port, self.command)

if __name__ == "__main__":
    logger.info('WolfAwd start ')
    options = parse_options()
    awd = WolfAwd(options)
    awd.run()
