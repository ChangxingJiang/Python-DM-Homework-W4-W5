import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    response = requests.get("https://s.weibo.com/top/summary")
    print(response.content.decode())
    # pl_top_realtimehot > table > tbody > tr:nth-child(2) > td.td-02 > a
    # pl_top_realtimehot > table > tbody > tr:nth-child(3) > td.td-02 > a
    bs = BeautifulSoup(response.content.decode(),'html.parser')
    for keyword_label in bs.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        print(keyword_label.text)
header={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "__mta=55506452.1590679944691.1590679944691.1590679944691.1; _lxsdk_cuid=1725be9bd18c8-06a996575a374f-f7d1d38-e1000-1725be9bd18c8; _lxsdk=1725be9bd18c8-06a996575a374f-f7d1d38-e1000-1725be9bd18c8; _lxsdk_s=1725be9bd1b-73f-2a1-f88%7C%7C2",
    "Host": "piaofang.maoyan.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
