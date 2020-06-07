'''
作业有点难。。所以先学了个简单的
扒取微博主页微博的id 时间 内容 点赞评论转发数
'''


from urllib.parse import urlencode
import requests
from  pyquery import PyQuery as pq

api = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/3081216591?uid=3081216591&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E8%B0%A2%E5%8F%AF%E5%AF%85',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


params = {
        'type': 'uid',
        't': 0,
        'luicode': '10000011',
        'lfid': '100103type=1&q=谢可寅',
        'type': 'uid',
        'value': 3081216591,
        'containerid': '1076033081216591',
        'since_id': ''
    }

url= api + urlencode(params)      #加入参数后的网址

try:
    response = requests.get(url, headers=headers)      #获取网页代码内容 JSON格式
    if response.status_code == 200:
        json=response.json()
except requests.ConnectionError as e:
    print('Error', e.args)

contents = json.get('data').get('cards')       #获取card标签后的内容

for content in contents[1:]:  #第一项内容没有所要的东西 所以从第二项开始遍历
    content = content.get('mblog')
    weibo = {}
    weibo['id'] = content.get('id')
    weibo['发布时间']=content.get('created_at')
    weibo['内容']=pq(content.get('text')).text().replace('\n','')      #问题：长文章无法完全显示
    weibo['点赞数'] = content.get('attitudes_count')
    weibo['评论数'] = content.get('comments_count')
    weibo['转发数'] = content.get('reposts_count')
    print(weibo)


#问题：无法翻页