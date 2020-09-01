import paramiko


class ConnectServer:
    def __init__(self, host):
        # noinspection PyBroadException
        try:
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host.hostname, port=host.port, username=host.username, password=host.password, compress=True)
            channel = ssh.invoke_shell()
            #  进行交互
            interactive.interactive_shell(channel)
            #  结束交互，终止连接
            channel.close()
            ssh.close()
        except Exception:
            print("Exit! If have anything Problem Please Check ConfigFile")
