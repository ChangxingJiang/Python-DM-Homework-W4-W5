"""

"""

import json
import time

import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "referer": 'https://www.bilibili.com/video/BV1Ma4y1v7RF',
}  # Headers

url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=668387865&sort=2&_=1591369288117&pn='
param_dict = {
    'pn': 0,
    'type': 1,
    'oid': 668387865,
    'sort': 2,
}  # 参数列表

pn = 1
for m in range(256):
    if __name__ == "__main__":
        r = requests.get(url, headers=headers)
        data = json.loads(r.text)
        comment = []
    for i in data['data']['replies']:
        print(i['member']['uname'] + ":" + i['content']['message'])
        if i['replies'] != None:
            for j in i['replies']:
                print("评论回复:" + j['member']['uname'] + ":" + j['content']['message'])
    pn += 1
    param_dict['pn'] = pn
    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=668387865&sort=2&_=1591369288117&pn='
    url = url + str(pn)
    time.sleep(0.5)

# “油管千万粉大神Kurt入驻b站！”视频评论爬虫
