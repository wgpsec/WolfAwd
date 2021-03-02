from optparse import OptionParser
import base64
import re
import hashlib
def parse_options():
    parser = OptionParser()
    parser.add_option("-m", "--module", \
                      dest="module", default="attack", \
                      help="Input the  func module here :)")
    parser.add_option("-p", "--poc", \
                      dest="vuln", default="chinaz",
                      help="The vuln you want to use")
    parser.add_option("-a", "--action", \
                      dest="action", default="get_flag",
                      help="The action you want to do")
    parser.add_option("-c", "--command", \
                      dest="command", default="",
                      help="The command you want to exec")
    parser.add_option("-t", "--targets", \
                      dest="targets", default="",
                      help="The target you want to attack")
    (options, args) = parser.parse_args()

    return options

def md5(s,salt=''):
    new_s = str(s) + salt
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()

def str_to_base64(str):
    return base64.b64encode(str.encode()).decode()

def base64_to_str(base64str):
    return base64.b64decode(base64str.encode()).decode()

def get_backdoor_hash(target_ip, target_port):
    return md5(get_backdoor_password(target_ip,target_port))
def get_backdoor_password(target_ip,target_port):
    return target_ip + target_port + "W4nde1lsfdvd"
