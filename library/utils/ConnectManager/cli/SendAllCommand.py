from library.utils.ConnectManager.base.SendCommand import SendCommand


class SendAll:
    def __init__(self):
        """
        读取配置文件,并配置要执行的命令
        """
        self.command = input("Command==>")
    def send_command(self):
        for i in range(nums): #服务器总数
            SendCommand(self)

