"""
抓取视频Url:https://www.bilibili.com/video/BV1Ki4y187pp?from=search&seid=7147633400336821574

1. 可以补充一些注释，尤其是你的代码时干什么的
2. 每次请求之间建议有一定的延时时间
3. 如果使用try...except...语句，最好其中仅包含可能报错的内容，这样每次报错损失的数据量最小
"""

import time

import requests


def get_replies(page_number):
    headers = {
        'cookie': 'CURRENT_FNVAL=16; _uuid=221941B2-66DC-C19C-E872-F1385AD7FFA091362infoc; buvid3=F05DD1FB-8A7F-4D6B-B921-6B6B864FEFD8155822infoc; PVID=2; sid=d6unv9ma; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f',
        'referer': 'https://www.bilibili.com/video/BV1Ki4y187pp?from=search&seid=7147633400336821574',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    url = 'https://api.bilibili.com/x/v2/reply?'
    for number in range(page_number):
        video_url_params = {
            'jsonp': 'jsonp',
            'pn': number + 1,
            'type': '1',
            'oid': 540179417,
            'sort': '0',
        }

        # 执行网页请求
        try:
            repliesall = requests.get(url, params=video_url_params, headers=headers).json()['data']['replies']
        except:
            print("无法获取该视频评论")
            continue

        # 解析网页信息
        for replies in repliesall:
            try:
                text = replies['content']['message']
                print('评论：', text)
            except:
                print("无法获取一条评论")
                continue

        time.sleep(2)


if __name__ == '__main__':
    get_replies(21)
