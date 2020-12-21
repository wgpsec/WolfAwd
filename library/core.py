class Attacker():
    def __init__(self, target_ip, target_port, cmd, vulns):
        self.target_ip = target_ip
        self.target_port = target_port
        self.cmd = cmd
        self.vulns = vulns

    def run(self):
        res = ''
        if self.get_backdoor_status():
            res = self.attack_by_backdoor()
        else:
            res = self.attack_by_vulns()

        return res

    def get_backdoor_status(self):
        return 0

    def attack_by_backdoor(self):
        return ''

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
