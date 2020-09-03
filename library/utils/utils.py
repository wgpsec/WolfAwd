import hashlib


def md5(data):
    return hashlib.md5(data.encode('utf--8')).hexdigest()
