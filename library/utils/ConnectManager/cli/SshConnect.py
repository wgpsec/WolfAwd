from library.utils.ConnectManager.base.SshConnect import ConnectServer
from library.utils.getconf import GetHostConfig

"""
目前主要框架没写出来，CTF name应该是贯穿整个程序运行的
"""


class SshConnect:
    def __init__(self, host_num):
        """
        __init__.py用来读取配置文件
        目前无配置文件
        储存为self.host
             self.port
             self.username
             self.passwd
        """

        self.host_conf = GetHostConfig(host_num, gamename="Test")

    def host_list(self):
        """
        用以输出所有的服务器信息
        """
        host_sum = int(self.host_conf["hostSum"])
        print("------------------------------------------------")
        for i in range(host_sum):
            print("[Server-%d]==>" % i +
                  "[IP]:" + self.host_conf[i].get("host") +
                  "[Username]:" + self.host_conf[i].get("username") +
                  "[Password]:" + self.host_conf[i].get("password"))
        print("------------------------------------------------")

    def connect_shell(self):
        ConnectServer(self)
