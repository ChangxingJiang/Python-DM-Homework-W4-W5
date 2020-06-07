"""
抓取的Url:https://so.iqiyi.com/so/q_%E4%B8%AD%E5%9B%BD%E4%BC%A0%E5%AA%92%E5%A4%A7%E5%AD%A6_ctg__t_0_page_0_p_1_qc_0_rd__site__m_1_bitrate__af_0
在爱奇艺搜索"中国传媒大学"

1. 有一些多余的代码建议删除(可以参考PyCharm的标注，灰色标注的代码为多余的)
2. 可以补充一些注释，尤其是你的代码时干什么的
3. 顺序序号就是循环中的i，不需要单独的计数器
4. 每次请求之间建议有一定的延时时间
5. 循环中定义的变量不建议在循环外使用【变量的作用域】
6. 不同的内容不建议用相同的变量名
"""

import time

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    for i in range(100):
        # 执行网页请求
        url = "https://so.iqiyi.com/so/q_%E4%B8%AD%E5%9B%BD%E4%BC%A0%E5%AA%92%E5%A4%A7%E5%AD%A6_ctg__t_0_page_" + str(
            i) + "_p_1_qc_0_rd__site__m_1_bitrate__af_0"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        }
        html = requests.get(url, headers=headers)

        # 网页解析
        soup = BeautifulSoup(html.text, "html.parser")
        for card in soup.find_all(attrs={'desc': 'card'}):
            result = card.find_all("a", attrs={"class": 'main-tit'})
            video_url = None
            video_title = None
            for result_item in result:
                video_url = result_item['href'].replace("/", "")
                video_title = result_item["title"]
            print(video_url, video_title)

        time.sleep(2)
