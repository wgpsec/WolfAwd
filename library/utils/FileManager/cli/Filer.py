from library.utils.FileManager.base.Filer import Filer
from library.utils.getconf import GetHostConfig


class UseFiler:
    def __init__(self, method):
        self.method = method
        self.usage()
        self.host_num = input("Num:")
        self.host_conf = GetHostConfig(self.host_num, gamename="Test")
        Filer(self)

    @staticmethod
    def usage():
        pass
