from library.utils.ConnectManager.base.SendCommand import SendCommand
import json


class SendAll:
    def __init__(self, host_num):
        """
        读取配置文件,并配置要执行的命令
        """
        self.config_file = open("/games/test/config.json", "r")
        self.config = json.load(self.config_file)["hostConfig"]
        self.command = input("Command==>")
        for i in range(host_num):
            self.host = self.config[host_num].get("host")
            self.port = int(self.config[host_num].get("port"))
            self.username = self.config[host_num].get("username")
            self.password = self.config[host_num].get("password")
            self.send_command()

    def send_command(self):
        SendCommand(self)
