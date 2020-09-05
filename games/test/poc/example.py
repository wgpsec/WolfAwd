from  library.utils.request import requests


"""
这个是poc的示例文件,从util获取请求文件,方便以后封装

poc文件需要配置poc_config
实现poc函数,poc函数传入ip和要执行的操作,返回结果
"""

"""
    name 为poc名字
    shell_type 为poc类型,分三种,
        2,可以获取shell
        1, 可以获取webshell
        0, 只能get flag
    os_type
        0 php
        1 python

"""

poc_config = {
    "name": "example",
    "shell_type": 1,
    "os_type": 2
}


def poc(target_host, command):
    text = requests.get("http://"+target_host+"/", params=command).text
    return text[1:]


