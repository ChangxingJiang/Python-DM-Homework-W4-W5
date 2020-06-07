import requests
from bs4 import BeautifulSoup
import json
import re
count = 0
for i in range(100):
    url = "https://so.iqiyi.com/so/q_%E4%B8%AD%E5%9B%BD%E4%BC%A0%E5%AA%92%E5%A4%A7%E5%AD%A6_ctg__t_0_page_"+str(count)+"_p_1_qc_0_rd__site__m_1_bitrate__af_0"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,"html.parser")
    for card in soup.find_all(attrs={'desc':'card'}):
        result = card.find_all("a",attrs={"class":'main-tit'})
        for result_item in result:
            url = result_item['href']
            url = url.replace("/","")
            title = result_item["title"]
        print(url,title)
    count += 1