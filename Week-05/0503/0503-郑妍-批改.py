"""
说明：#微信已支持改微信号# 超话内容


"""

import re
import time

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    headers = {
        'Cookie': '_s_tentry=-; Apache=8462619024391.334.1591362686179; SINAGLOBAL=8462619024391.334.1591362686179; ULV=1591362686190:1:1:1:8462619024391.334.1591362686179:; SUB=_2A25z3iJUDeRhGeNG7VQT8CvNzTWIHXVQqhScrDV8PUNbmtANLWT2kW9NSyB3HwgfnrXXVTpQCOIX3zjraRmhvzwS; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Gz5rA1Z-9xM.oTLYLZ.K55JpX5KzhUgL.Fo-RSoqEeh-pSo.2dJLoI7RLxKML1-eLB.SEMriEMntt; SUHB=0D-1putkCGLCxu; ALF=1622902147; SSOLoginState=1591366148',
    }

    start_page = int(input('请输入抓取的起始页码'))
    stop_page = int(input('请输入抓取的终止页码'))
    for page in range(start_page, stop_page + 1):
        print('现在是第', page, '页')
        response = requests.get(
            "https://s.weibo.com/weibo?q=%23%E5%BE%AE%E4%BF%A1%E5%B7%B2%E6%94%AF%E6%8C%81%E6%94%B9%E5%BE%AE%E4%BF%A1%E5%8F%B7%23&from=trendtop_api&refer=index_hot_new&page={}".format(
                page), headers=headers)
        bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        for label in bs.select(
                "#pl_feedlist_index > div:nth-child(1) > div > div > div.card-feed > div.content > p.txt"):
            # 内容整理
            space = re.compile("^\s+|\s+$")
            label1 = re.sub(space, "", label.text)  # 清除空格
            pattern1 = '展开全文c+$'
            pattern2 = '收起全文d+$'
            if re.search(pattern1, label1) is not None:
                pass
            else:
                label2 = re.sub(pattern2, '', label1)  # 整理展开全文&收起全文
                print(label2 + '\n')
                time.sleep(1)
