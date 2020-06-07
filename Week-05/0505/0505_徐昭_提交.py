#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
目的：爬取B站视频里的评论
"""
import requests
import json
import time
import math
import pandas as pd
import os


def check():  # 检查是否有这个文件，如果有就删除
    filename = 'bilibili.csv'
    if os.path.exists(filename):
        os.remove(filename)


def fetchURL(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 修改头部

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # 值返回是200时才不产生异常
        return r.text  # 返回文本
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")


def parserHtml(html):  # 将获取的r.text文本传到这里进行解析
    try:
        s = json.loads(html)  # 还原数据格式
        # print(s)
    except:
        print('error')
    commentlist = []  # 储存所有评论信息的列表

    for i in range(20):
        comment = s['data']['replies'][i]  # 评论信息
        blist = []  # 储存每条评论的临时列表

        username = comment['member']['uname']  # 名字
        sex = comment['member']['sex']  # 性别
        ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment['ctime']))  # 评论时间
        content = comment['content']['message']  # 评论内容
        likes = comment['like']  # 点赞数
        rcounts = comment['rcount']  # 回复数
        # 将各种信息添加到blist里
        blist.append(username)
        blist.append(sex)
        blist.append(ctime)
        blist.append(content)
        blist.append(likes)
        blist.append(rcounts)

        commentlist.append(blist)  # 把每条评论信息添到commentlist里

    writePage(commentlist)


def writePage(urating):  # 将commenlist里的内容写进表格里
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv('Bilibili.csv', encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


def writeTitle():  # 填写表格里的表头
    hlist = ["名字", "性别", "时间", "评论", "点赞数", "回复数"]
    titlelist = []
    titlelist.append(hlist)
    writePage(titlelist)


def BvToAv(Bv):  # 将B站里的bv号转为av号
    BvNo1 = Bv[2:]
    keys = {
        '1': '13', '2': '12', '3': '46', '4': '31', '5': '43', '6': '18', '7': '40', '8': '28', '9': '5',
        'A': '54', 'B': '20', 'C': '15', 'D': '8', 'E': '39', 'F': '57', 'G': '45', 'H': '36', 'J': '38', 'K': '51',
        'L': '42', 'M': '49', 'N': '52', 'P': '53', 'Q': '7', 'R': '4', 'S': '9', 'T': '50', 'U': '10', 'V': '44',
        'W': '34', 'X': '6', 'Y': '25', 'Z': '1',
        'a': '26', 'b': '29', 'c': '56', 'd': '3', 'e': '24', 'f': '0', 'g': '47', 'h': '27', 'i': '22', 'j': '41',
        'k': '16', 'm': '11', 'n': '37', 'o': '2',
        'p': '35', 'q': '21', 'r': '17', 's': '33', 't': '30', 'u': '48', 'v': '23', 'w': '55', 'x': '32', 'y': '14',
        'z': '19'
    }
    BvNo2 = []
    for index, ch in enumerate(BvNo1):
        BvNo2.append(int(str(keys[ch])))
    BvNo2[0] = int(BvNo2[0] * math.pow(58, 6))
    BvNo2[1] = int(BvNo2[1] * math.pow(58, 2))
    BvNo2[2] = int(BvNo2[2] * math.pow(58, 4))
    BvNo2[3] = int(BvNo2[3] * math.pow(58, 8))
    BvNo2[4] = int(BvNo2[4] * math.pow(58, 5))
    BvNo2[5] = int(BvNo2[5] * math.pow(58, 9))
    BvNo2[6] = int(BvNo2[6] * math.pow(58, 3))
    BvNo2[7] = int(BvNo2[7] * math.pow(58, 7))
    BvNo2[8] = int(BvNo2[8] * math.pow(58, 1))
    BvNo2[9] = int(BvNo2[9] * math.pow(58, 0))

    sum = 0
    for i in BvNo2:
        sum += i
    sum -= 100618342136696320
    temp = 177451812

    return sum ^ temp


if __name__ == '__main__':
    check()
    e = 0
    page = 0
    writeTitle()
    while e == 0:
        Bv = "BV1nz411i7dW"  # 这里是李子柒最新一期的视频，可以自行更改
        url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=' + \
              str(BvToAv(Bv)) + '&pn=' + str(page)
        try:
            html = fetchURL(url)
            parserHtml(html)
            page = page + 1  # 翻页
            print('Page ' + str(page) + ' finished')
            if page % 20 == 0:  # 每爬20页停3s
                time.sleep(3)
        except:
            e = 1

    print("end!")  # 操作完成！
