import requests

"""
爬取京东网页商品
url="https://item.jd.com/55433151417.html"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding#返回是200时不产生异常
    print(r.text[:1000])
except:
    print("爬取失败！")
    

    爬取亚马逊的商品信息
url = "https://www.amazon.cn/dp/B07614RGGQ"
try:
    kv = {"User-Agent":"Mozilla/5.0"}
    r=requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # 返回是200时不产生异常
    print(r.text[1000:2000])
except:
    print("爬取失败！")
    
    
    爬取百度关键词条数
keyword="包包"
try:
    kv = {"wd":keyword}
    r=requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    # 返回是200时不产生异常
    print(len(r.text))
except:
    print("爬取失败！")



获取”图片、动画、视频“均可
import os

url = "http://c2.haibao.cn/img/400_400_100_0/1490095808.7839/2e0ede0e7065512f17769bf96de9eb13.jpg"
root = "E:\\pycharm工作台\\"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):  # 判断根目录是否存在，不存在则新建一个这样的根目录
        os.mkdir(root)
    if not os.path.exists(path):  # 接下来判断这个图片文件是否已经存在，如果不存在的话就用requests库去爬取
        r = requests.get(url)
        with open(path, 'wb')as f:
            f.write(r.content)  # r.content表示爬取的respense内容中的二进制形式
            f.close()
            print("文件保存成功！")
    else:
        print("文件已存在！")
except:
    print("爬取失败！")
    """
from bs4 import BeautifulSoup
if __name__ == "__main__":
    response = requests.get("https://s.weibo.com/top/summary")
    bs = BeautifulSoup(response.content.decode(), 'lxml')
    for keyword_label in bs.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        print(keyword_label.text)