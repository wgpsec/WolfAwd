from library.utils.ConnectManager.base.SshConnect import ConnectServer


class SshConnect:
    def __init__(self):
        """
        __init__.py用来读取配置文件
        目前无配置文件
        储存为self.host
             self.port
             self.username
             self.passwd

        """

    def connect_shell(self):
        ConnectServer(self)
