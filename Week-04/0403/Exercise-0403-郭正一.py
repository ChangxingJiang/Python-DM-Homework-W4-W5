import requests
import re
import json
import time
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "Connection": "keep-alive",
    "host": "movie.douban.com",
    "pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
}

response = requests.get('https://movie.douban.com/top250',headers=headers)
print(response.content.decode(errors='ignore'))

for page_num in range(10):
    url = "https://movie.douban.com/top250?start={0}&filter=".format(page_num * 25)
    response = requests.get(url, headers=headers)

from bs4 import BeautifulSoup
x = BeautifulSoup(response.content.decode(errors='ignore'),'lxml')
for movie_label in x.select('#content > div > div.article > ol > li'):
    movie_lin = movie_label.select_one('li> div > div.pic > a')['href']
    title_txt = movie_label.select_one('li > div > div.info > div.hd > a').text.replace('\n','h')
    info_text = movie_label.select_one("li > div > div.info > div.bd > p:nth-child(1)").text
    rating_num = movie_label.select_one("li > div > div.info > div.bd > div > span.rating_num").text
    rating_people = movie_label.select_one("li > div > div.info > div.bd > div > span:nth-child(4)").text
    if quote_label := movie_label.select_one("li > div > div.info > div.bd > p.quote"):
        quote = quote_label.text
    print(movie_lin, title_txt, info_text, rating_num, rating_people, quote)

def clear(text):
    '''
    自定义函数消除空行
    '''
    text = re.sub("^[ \xa0]*", "", text)
    text = re.sub("[ \xa0]*$", "", text)
    return text
if __name__ == '__main__':
    movie_list = list()

#解析并清洗标题行
    title_text = movie_label.select_one("li > div > div.info > div.hd > a").text.replace("\n", "") #从标签中挑出标题，之后消除换行
    Chinese_title =  clear(title_txt.split("/")[0])#提取出中文标题并消除换行和空格前后
    title_other = [clear(title) for title in title_txt.split("/")[1:]]#提取出其他标题并消除空格前后

#解析导演信息
    director_show =  movie_label.select_one(' li > div > div.info > div.bd > p:nth-child(1)').text#获取导演说明
    director_show = re.sub('\n *','\n',director_show)#re.sub加正则表达式，除去行前空格
    director_show = re.sub('^\n','',director_show)#除去开头空行
    #此时可以搞定导演那一个块块
    director_1 = director_show.split("\n")[0] #第一行
    director_2 = director_show.split('\n')[1]#第二行
    director = re.sub(" *(主演|主\\.{3}|\\.{3}).*$", "", director_1)#保留导演
    years = re.search("[0-9]+", director_2.split("/")[0]).group()#年份提取
    year = int(years)#转化数字
    country = clear(director_2.split("/")[1]) if len(director_2.split("/")) >= 2 else None
    classify = clear(director_2.split("/")[2]) if len(director_2.split("/")) >= 3 else None  # 提取电影类型
    classify = re.split(" +", classify)  # 将电影类型转换为list形式
    #解析评分星级模块
    score = movie_label.select_one('li > div > div.info > div.bd > div > span.rating_num').text#评分提取~不知道提取星级会发生什么，一会试一试
    i = re.search('[0-9].+',score).group()
    score = float(i)
    #此时评分和评价人数还在一起，我要把它们分开
    comment = movie_label.select_one(' li > div > div.info > div.bd > div > span:nth-child(4)').text
    j = re.search('[0-9]+',comment).group()
    comment = int(j)
    #评价
    if quote_label := movie_label.select_one("li > div > div.info > div.bd > p.quote"):#提取评价
        quote = quote_label.text.replace("\n", "")  # 清除换行符
    else:
        quote = None

    movie_list.append({
        "title": {
            "chinese":Chinese_title,
            "others": title_other
        },
        "director": director,
        "year": year,
        "country": country,
        "classify": classify,
        "rating": {
            "num": score,
            "people": comment
        },
        "quote": quote
    })

time.sleep(5)
print(page_num)


print(movie_list)
with open("豆瓣TOP250电影.json", "w+", encoding="UTF-8") as file:
    file.write(json.dumps({"data": movie_list}, ensure_ascii=False))
