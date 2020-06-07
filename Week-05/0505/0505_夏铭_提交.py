#问题：每层楼的部分评论需点击“点击查看”才能显示，但是那些评论有一个参数好像是是随机的，不会爬。。。

import requests
import json
import time

def getComments(video_id): #video_id为视频av号
    url = 'https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid={}&sort=1'.format(video_id)
    '''
       pn:页数
       sort:0按发送时间倒序 1按热门排序 2按点赞数排序
       oid:视频av号
    '''
    rsp = requests.get(url).content.decode()
    comment_num=json.loads(rsp)["data"]["page"]["count"]
    page_num_all=comment_num//20+1
    for n in range(1, page_num_all):
        print('正在请求第%a页'%(n))
        url = 'https://api.bilibili.com/x/v2/reply?pn='+str(n)+'&type=1&oid={}&sort=1'.format(video_id)
        rsp = requests.get(url).content.decode()
        en = json.loads(rsp)['data']['replies']
        for y in range(len(en)):
            comment = en[y]['content']['message']
            print(comment)
            time.sleep(1)
if __name__ == "__main__":
    res=getComments(56728862) #输入视频av号，此处以老番茄视频为例