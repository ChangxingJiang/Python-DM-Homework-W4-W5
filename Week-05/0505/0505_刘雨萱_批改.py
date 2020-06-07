"""
爬取B站视频《长命锁》评论
@author: Chloe

1. 应优先代码可以正常运行，没有错误（可能是因为将部分代码提出为函数时造成的错误）
2. while循环如果用来控制跳出，可以直接用break
3. x=x+1建议使用运算符x+=1实现
4. 修改字典中的内容不能只是调用并修改到其他变量中【变量的含义】
5. 变量名不能和引用的模块名冲突
6. 在使用通过请求获得的Json时，应先判断属性是否存在，或使用try...except...以避免报错
"""

import json
import time

import requests

headers = {'user-agents': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}


def getcomment(page):
    avID = []
    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=200750674&pn=' + str(page)
    r = requests.get(url, headers=headers).text
    data = json.loads(r)
    comments = data['data']['comment']
    for ac in comments:
        avID.append(ac['comment']['list'])
        comment_user = ac['user']['name']
        comment_content = ac['text']
        comment_time = ac['info']['time']
    time.sleep(2)
    return comments


if __name__ == '__main__':
    page = 0
    comments = None
    while True:
        try:
            comments = getcomment(page)
            page += 1
            time.sleep(5)
        except:
            break
    with open('E:\python\W4W5\comment.json', 'a', encoding='utf-8', newline='') as f:
        json.dump(comments, f)
        f.close()
