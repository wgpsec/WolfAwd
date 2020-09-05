import requests

"""
先这样写着,后期可以考虑对requests进行封装
混淆流量之类的
"""


def get_requests():
    return requests


requests = get_requests()
