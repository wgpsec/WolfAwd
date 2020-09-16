from library.utils.ConnectManager.base.SendCommand import SendCommand
from library.utils.getconf import GetHostConfig


class SendAll:
    def __init__(self, host_num):
        """
        读取配置文件,并配置要执行的命令
        """
        self.command = input("Command==>")
        for i in range(host_num):
            self.host_conf = GetHostConfig(host_num, gamename="Test")
            self.send_command()

    def send_command(self):
        SendCommand(self.host_conf)
