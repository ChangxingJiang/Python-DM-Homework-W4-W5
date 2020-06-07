import requests
from bs4 import BeautifulSoup
import re
import time
import json

headers = {
	"accept": "*/*",
	"accept-language": "zh-CN,zh;q=0.9",
	"cache-control": "no-cache",
	"cookie": "id=226b8537f3c100cf||t=1590297751|et=730|cs=002213fd487a008316d56b964a",
	"origin": "https://movie.douban.com",
	"pragma": "no-cache",
	"referer": "https://movie.douban.com/top250",
	"sec-fetch-dest": "empty",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "cross-site",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
	"x-client-data": "CI22yQEIo7bJAQjEtskBCKmdygEIy8fKARibvsoB"
}

movie_list = []

for i in range(10):
	url = "https://movie.douban.com/top250?start={}&filter=".format(i*25)
	response = requests.get(url,headers = headers)

	bs = BeautifulSoup(response.content.decode(errors="ignore"),"lxml")

	for i in bs.select("#content > div > div.article > ol > li"):
		movie_url = i.select_one("li > div > div.info > div.hd > a")["href"]#["href"]
		
		title = i.select_one("li > div > div.info > div.hd > a").text.replace("\n","")#select_one
		title_chinese = title.split("/")[0].replace(" ","")
		title_other = []
		for x in title.split("/")[1:]:
			title_other.append("".join(x.split()))#如果用x.repalce(" ","")会出现一个\xa0字符

		info = i.select_one("li > div > div.info > div.bd > p:nth-child(1)").text.replace(" ","")
		info = info.strip()#strip()去除首位空格，也就去除了开头的空行
		info_1 = info.split("\n")[0]#获取导演和主演
		info_2 = info.split("\n")[1]#获取年份等信息
		director = re.sub("主演.*", "", info_1)#导演

		year = int(re.search("[0-9]+",info_2.split("/")[0].replace(" ","")).group())
		country = info_2.split("/")[1].replace(" ","")
		classify = info_2.split("/")[2].split()#分类列表

		rate_num = i.select_one("li > div > div.info > div.bd > div > span.rating_num").text
		rate_num = float(re.search("[0-9.]+",rate_num).group())

		rate_people = i.select_one("li > div > div.info > div.bd > div > span:nth-child(4)").text
		rate_people = int(re.search("[0-9]+",rate_people).group())

		quote_label = i.select_one("li > div > div.info > div.bd > p.quote")#再加个>span会怎么样？
		if quote_label:
			quote = quote_label.text.replace("\n","")
		else:
			quote = None
		print(movie_url)
		print(title_chinese)
		print(title_other)
		print(director)
		print(year)
		print(country)
		print(classify)
		print(rate_num)
		print(rate_people)
		print(quote)

		movie_list.append({
			"title":{"chinese":title_chinese,"others":title_other},
			"director":director,
			"year":year,
			"country":country,
			"classify":classify,
			"rating":{"people":rate_people,"num":rate_num},
			"quote":quote})

	time.sleep(5)

with open("豆瓣电影前250.json","w+",encoding="utf-8") as file:
	file.write(json.dumps({"data":movie_list},ensure_ascii = False))