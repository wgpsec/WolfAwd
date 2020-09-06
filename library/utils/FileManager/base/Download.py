import paramiko


class Downloader:
    def __init__(self, host):
        transport = paramiko.Transport(host.hostname, host.port)
        transport.connect(username=host.username, password=host.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        if host.method == "upload":
            # 上传功能
            sftp.put(host.localpath, host.remotepath)
        elif host.method == "download":
            # 下载功能
            sftp.get(host.remotepath, host.localpath)
        transport.close()
