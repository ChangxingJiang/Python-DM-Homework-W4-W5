import requests
from urllib.parse import urlencode
import time
import math

headers = {
	"accept": "application/json, text/plain, */*",
	# "accept-encoding": "gzip, deflate, br",#不加这个
	"accept-language": "zh-CN,zh;q=0.9",
	"cache-control": "no-cache",
	"cookie": "_uuid=7D855BFE-2339-1B35-0000-289D3732E60A84789infoc; buvid3=8B5473CD-0BE3-45C1-82F1-7978217AEFD8155824infoc; UM_distinctid=1724fc01277107-0313b973103568-f7d1d38-e1000-1724fc01279211; bsource=seo_baidu; PVID=1; CNZZDATA1272960325=2094693799-1591340722-%7C1591340722; bfe_id=6f285c892d9d3c1f8f020adad8bed553",
	"origin": "https://space.bilibili.com",
	"pragma": "no-cache",
	"referer": "https://space.bilibili.com/20165629/video?tid=0&page=1&keyword=&order=pubdate",
	"sec-fetch-dest": "empty",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-site",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
	}

para_dict = {
	"mid": 20165629,
	"ps": 30,
	"tid": 0,
	"pn": 1,
	"keyword": "",
	"order": "pubdate",
	"jsonp": "jsonp",
	}

nowp = 1
maxp = 1

while nowp <= maxp:
	print("正在请求第%d页"%nowp)
	para_dict["pn"] = nowp
	response = requests.get("https://api.bilibili.com/x/space/arc/search?" + urlencode(para_dict),headers = headers)#注意格式
	response_json = response.json()
	
	maxp = math.ceil(response_json["data"]["page"]["count"] / 30)#获取视频总页数
	for i in response_json["data"]["list"]["vlist"]:
		title = i["title"]
		play = i["play"]
		print("标题：",title)
		print("播放次数：",play)
	nowp += 1
	time.sleep(5)