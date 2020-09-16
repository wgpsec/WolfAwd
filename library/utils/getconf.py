import json


class GetHostConfig:
    def __init__(self, host_num, gamename):
        self.config_file = open("/games/" + gamename + "/config.json", "r")
        self.config = json.load(self.config_file)["hostConfig"]
        self.host = self.config[host_num].get("host")
        self.port = int(self.config[host_num].get("port"))
        self.username = self.config[host_num].get("username")
        self.password = self.config[host_num].get("password")
        self.returnback()

    def returnback(self):
        return self
