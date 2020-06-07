# -*- coding: utf-8 -*-
"""
爬取B站视频《长命锁》评论
@author: Chloe
"""
import time
import requests
import json

headers = {'user-agents': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}


def getcomment(page):
    avID = []
    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=200750674&pn=' + str(page)
    r = requests.get(url, headers=headers).text
    data = json.loads(r)
    comments = data['data']['comment']
    for ac in comments:
        avID.append(ac['comment']['list'])
        user= ac['user']['name']
        content=ac['text']
        time=ac['info']['time']
    time.sleep(2)
    return comments



if __name__ == '__main__':
    e=0
    page=0
    while e == 0 :
        try:
            getcomment(page)
            page = page + 1
            time.sleep(5)
        except:
            e = 1
    with open('E:\python\W4W5\comment.json', 'a', encoding = 'utf-8', newline = '') as f:
    json.dump(comments, f)
    f.close()
    return


