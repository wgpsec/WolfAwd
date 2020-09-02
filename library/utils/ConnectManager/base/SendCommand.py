import paramiko


class SendCommand:
    def __init__(self, host):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host.hostname, host.port, host.username, host.password, timeout=10)
            std_in, std_out, std_err = client.exec_command(host.command)
            result = std_out.read()
            error = std_err.read()
            if not error:
                print(result.decode('utf-8'))
            else:
                print(error.decode('utf-8'))
        except Exception:
            print("Connect %d Error" % host.hostname)
