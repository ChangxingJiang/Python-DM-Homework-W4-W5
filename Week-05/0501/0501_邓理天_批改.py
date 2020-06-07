"""
说明:爬取知乎登录后首页的问题，以及问题页面的关注者数与回答数

1. 开头注释通常使用双引号
2. 变量名尽量注意使用下划线形式
3. 存储的数据结构可以考虑使用[<dict>,<dict>,...]的形式
"""

import re
import time

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 执行网页请求
    headers = {
        'cookie': '_zap=c5641679-b63b-4dfd-8771-c11476c2d964; _xsrf=bDLTg4eza0BWZOVhyWXWP1jXIdq9sTLC; d_c0="AACaZHS4YBGPTl5BdOGlQNbYYmuvLAfKmGU=|1591328580"; _ga=GA1.2.1605853349.1591328584; _gid=GA1.2.1883624308.1591328584; SESSIONID=WEtMfQoAfwvtvq5m9uodxrwPieGQyXNxeQWaUKl2Ob5; JOID=W1wWAE14Fu6c_QMVEXJ0POuNsXcKIlSa1JRffVARbJ_ojn0tezeuMsj_CRIUIiztrPkACByLDtUROVn5-2Y5FYg=; osd=W1kTAk94E-ue_wMQFHB2PO6Is3UKJ1GY1pRaeFITbJrtjH8tfjKsMMj6DBAWIinorvsADRmJDNUUPFv7-2M8F4o=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1591328584,1591343680; capsion_ticket="2|1:0|10:1591343703|14:capsion_ticket|44:NGQyZGE1NGU5ZWZkNGFmN2FjNmQwNTFlMGZhMmYzMDI=|100da9e0c657c3d4823504939315b129c46a20237c0819123f10617b720218b1"; z_c0="2|1:0|10:1591343783|4:z_c0|92:Mi4xWkhSMkF3QUFBQUFBQUpwa2RMaGdFU1lBQUFCZ0FsVk5wMGpIWHdDZmwwYUlDa1pZTVNhU0lpVl8teGVrOW1HbmFn|7bdc501cc8f98d5340e62ee607e2cf69ee995e4d5f42746889c8cd21ca57d3c6"; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1591371886; KLBRSID=ca494ee5d16b14b649673c122ff27291|1591372080|1591358488',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    url = 'https://www.zhihu.com/'
    response = requests.get(url, headers=headers)  # 请求网页

    html = response.text  # 获取网页内容
    soup = BeautifulSoup(html, 'html.parser')  # 解析网页内容
    divs = soup.find_all('div', {'class': 'ContentItem AnswerItem'})  # 寻找每个问题所在的位置

    questions = []
    follower_numbers = []
    answer_numbers = []  # 创建问题、关注者数、回答数列表

    # 遍历所有问题
    for index, div, in enumerate(divs):
        question = div.a.string
        questions.append(question)  # 将问题添加进列表
        href = div.a['href']
        id1 = href.split('/')[-3]
        id2 = href.split('/')[-1]
        new_url = 'https://www.zhihu.com/question/%s/answer/%s' % (id1, id2)  # 找到每个问题的链接

        response = requests.get(new_url, headers=headers)

        one_html = response.text
        one_soup = BeautifulSoup(one_html, 'html.parser')  # 解析新网页内容
        for follower_number in one_soup.find('strong', {'class': 'NumberBoard-itemValue'}):
            follower_numbers.append(follower_number.string)  # 添加关注者数列表
        for view_number in one_soup.find('a', {'class': 'QuestionMainAction ViewAll-QuestionMainAction'}):
            answer_number = re.findall(r'\d+', view_number.string)
            answer_numbers.append(answer_number[-1])  # 添加回答数列表

        time.sleep(2)

    result = zip(questions, follower_numbers, answer_numbers)  # 将三个列表压缩
    list1 = list(result)

    with open(r'zhihuOUT.txt', 'w', encoding='utf-8', errors='ignore', newline='') as f:  # 打开文件
        for item in list1:
            item_result = '问题：' + item[0] + '；关注者数：' + item[1] + '；回答数：' + item[2]
            print(item_result)  # 输出测试
            f.write(item_result)
            f.write('\n')  # 写入文件
    f.close()
