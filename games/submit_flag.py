def submit_flag(target_ip,target_port, flag):
    import requests

    session = requests.session()

    burp0_url = "http://a.wendell.pro:9090/"
    burp0_cookies = {"sessionid": "mpszxk6igffufgxv2pr7pazcmfeq0auc"}
    burp0_headers = {"Cache-Control": "max-age=0", "Origin": "http://a.wendell.pro:9090",
                     "Upgrade-Insecure-Requests": "1", "DNT": "1", "Content-Type": "application/x-www-form-urlencoded",
                     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Referer": "http://a.wendell.pro:9090/", "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    burp0_data = {"flag": flag, "token": "4300f7f61934925694f6138f3045e61e"}
    res = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data).text
    # if 'flag提交成功' in res:
    #     return 1
    # else:
    #     return 0
    import re
    result = re.search(r'hulla.send\("(.*?)"', res).groups(0)[0]
    return result
