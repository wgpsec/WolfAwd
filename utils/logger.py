#! /usr/bin/env python
import logging
from colorama import init
init()
from colorama import Fore, Back, Style
import os
# import ctypes
#
# FOREGROUND_WHITE = 0x0007
# FOREGROUND_BLUE = 0x01  # text color contains blue.
# FOREGROUND_GREEN = 0x02  # text color contains green.
# FOREGROUND_RED = 0x04  # text color contains red.
# FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
#
# STD_OUTPUT_HANDLE = -11
# std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


# def set_color(color, handle=std_out_handle):
#     bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
#     return bool


logger = None


class Logger:
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def get_logger(self):
        if self.logger:
            return self.logger
        else:
            return self()

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        print(Fore.BLUE)
        self.logger.info(message)
        print(Fore.WHITE)

    def warning(self, message):
        print(Fore.YELLOW)
        self.logger.error(message)
        print(Fore.WHITE)

    def error(self, message):
        print(Fore.RED)
        self.logger.error(message)
        print(Fore.WHITE)

    def cri(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logyyx = Logger('yyx.log', logging.WARNING, logging.DEBUG)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')
