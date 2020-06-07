"""
爬取 小片片解读传闻中的陈芊芊 视频评论

1. 在使用通过请求获得的Json时，应先判断属性是否存在，或使用try...except...以避免报错
2. 建议将import统一放在文件最前面
3. while循环如果需要跳出建议使用break
4. x=x+1建议使用运算符x+=1实现
5. 变量名和函数名建议使用下划线形式
"""

import json
import time

import pandas as pd
import requests


def fetchURL(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    print(r.url)
    return r.text


def parser_html(html):
    s = json.loads(html)
    comment_list = []
    hlist = []
    hlist.append("名字")
    hlist.append("评论")
    for i in range(20):
        comment = s['data']['replies'][i]
        blist = []
        username = comment['member']['uname']
        content = comment['content']['message']
        blist.append(username)
        blist.append(content)
        comment_list.append(blist)


def write_page(urating):
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv('Bilibili_comment.csv', mode='a', index=False, sep='：', header=False)


if __name__ == '__main__':
    page = 0
    while True:
        url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=200750674&pn=' + str(page)
        try:
            html = fetchURL(url)
            parser_html(html)
            page += 1
            time.sleep(5)
        except:
            break
