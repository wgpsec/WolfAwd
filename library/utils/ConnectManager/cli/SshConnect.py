from library.utils.ConnectManager.base.SshConnect import ConnectServer
import json

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
        
        self.config_file = open("/games/test/config.json", "r")
        self.config = json.load(self.config_file)["hostConfig"]
        self.host = self.config[host_num].get("host")
        self.port = int(self.config[host_num].get("port"))
        self.username = self.config[host_num].get("username")
        self.password = self.config[host_num].get("password")

    def host_list(self):
        """
        用以输出所有的服务器信息
        """
        host_sum = int(self.config["hostSum"])
        print("------------------------------------------------")
        for i in range(host_sum):
            print("[Server-%d]==>" % i +
                  "[IP]:" + self.config[i].get("host") +
                  "[Username]:" + self.config[i].get("username") +
                  "[Password]:" + self.config[i].get("password"))
        print("------------------------------------------------")

    def connect_shell(self):
        ConnectServer(self)
