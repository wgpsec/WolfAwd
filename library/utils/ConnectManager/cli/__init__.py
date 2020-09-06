from .SshConnect import SshConnect
from .SendAllCommand import SendAll


class ConnectManager:
    def __init__(self):
        """
        __init__ 选择发送全部主机指令或者进入单个主机的shell目前可以实现加固的SSH连接
        """
        self.usage()
        while True:
            function_choice = input(">>>")
            if function_choice == "0" or function_choice == "help":
                self.usage()
            elif function_choice == "1" or function_choice == "shell":
                SshConnect()
            elif function_choice == "2" or function_choice == "send":
                SendAll()

    @staticmethod
    def usage():
        """
        帮助信息
        """
        print("+----------------------------------------------------+")
        print("|Num|Command |    Describe                           |")
        print("+----------------------------------------------------+")
        print("|0. | help   |    Get Usage                          |")
        print("|1. | shell  |    Get into Single Shell              |")
        print("|2. | send   |    Send a Command to All servers      |")
        print("+----------------------------------------------------+")
