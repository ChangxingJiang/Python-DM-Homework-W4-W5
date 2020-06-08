import json
import requests
import time
import pandas as pd

def fetch_url(url): # 获取评论
    headers = {'user-agents': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.text
def parser_html(html):
    s = json.loads(html)
    comment_list=[]#全部评论信息
    step_list=[]#暂时储存列表
    try:
        step_list.append("ID")
        step_list.append("comment")
        for i in range(20):
            comment = s["data"]["reply"][i]
            username = comment["member"]["name"]
            content = comment["content"]["message"]
            step_list.append(username)
            step_list.append(content)
            comment_list.append(step_list)
    except:
        print("无法获取该视频评论")
        continue

def writePage(urating):
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv('Bilibili.csv', encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


if __name__ == '__main__':
    page = 0
    while True:
        av=input("av:")
        url = 'https://api.bilibili.com/x/v2/reply?type=1&oid={}&pn='.format(av) + str(page)
        try:
            html = fetch_url(url)
            parser_html(html)
            page += 1
            time.sleep(5)
        except:
            break





