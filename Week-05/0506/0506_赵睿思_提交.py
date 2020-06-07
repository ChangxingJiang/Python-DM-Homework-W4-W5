#爬取 小片片解读传闻中的陈芊芊 视频评论
import requests
import json
import time


def fetchURL(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    print(r.url)
    return r.text

def parserHtml(html):
    s = json.loads(html)
    commentlist = []
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
        commentlist.append(blist)

def writePage(urating):
    import pandas as pd
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv('Bilibili_comment.csv', mode='a', index=False, sep='：', header=False)

if __name__ == '__main__':
    e=0
    page=0
    while e == 0 :
        url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=200750674&pn=' + str(page)
        try:
            html = fetchURL(url)
            parserHtml(html)
            page=page+1
            time.sleep(5)
        except:
            e=1

