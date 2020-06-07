"""
说明
b站视频评论爬虫
我做这个爬虫的时候没有遇到反爬虫，这个案例好像有点容易……甚至连翻页都不需要

有两个发现：
1.请求并不在XHR里面，在JS里
2.参数里面如果加上了原有的callback就无法显示，删去之后一切正常
"""

from urllib.parse import urlencode

import requests

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "cookie": "_uuid=7D855BFE-2339-1B35-0000-289D3732E60A84789infoc; buvid3=8B5473CD-0BE3-45C1-82F1-7978217AEFD8155824infoc; UM_distinctid=1724fc01277107-0313b973103568-f7d1d38-e1000-1724fc01279211; bsource=seo_baidu; PVID=1; CNZZDATA1272960325=2094693799-1591340722-%7C1591445345; CURRENT_FNVAL=16; sid=i5tu4jke; bfe_id=cade757b9d3229a3973a5d4e9161f3bc",
    "pragma": "no-cache",
    "referer": "https://www.bilibili.com/video/BV1UA411v79n",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

para_dict = {
    # "callback": "jQuery172005942406017133117_1591449034078",
    "jsonp": "jsonp",
    "pn": 1,
    "type": 1,
    "oid": 328499747,
    "sort": 2,
    "_": 1591449041293
}  # 被注释掉的callback是原网页里面的参数，加了之后就无法显示，删了之后就可以显示了，为什么？

if __name__ == '__main__':
    response = requests.get("https://api.bilibili.com/x/v2/reply?" + urlencode(para_dict), headers=headers)
    response_json = response.json()

    for i in response_json["data"]["replies"]:
        name = i["member"]["uname"]
        sex = i["member"]["sex"]
        content = i["content"]["message"].replace("\n", "")
        print("评论用户名：", name)
        print("性别：", sex)
        print("评论内容：", content)
        print("")
