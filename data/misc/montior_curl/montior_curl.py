import psutil
import os
import signal
while True:
    for one_socket in psutil.net_connections(kind="all"):
        if one_socket.raddr and one_socket.raddr.ip == '118.24.169.134':
            pid = one_socket.pid if one_socket.pid else -1
            if pid != -1:
                os.kill(pid, signal.SIGKILL)
            print('%s:%d  pid:%d' % (one_socket.raddr.ip,
                                     one_socket.raddr.port, pid))
