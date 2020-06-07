# 因为知乎随着滚动条下拉会更新回答，用selenium模仿操作

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import math

# 模拟网页 知乎问题：在中国传媒大学就读是什么样的体验？
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
browser = webdriver.Chrome(options=option)
browser.get("https://www.zhihu.com/question/31098913")
time.sleep(2)

# 对滚动条进行下拉操作，获取页面
browser.find_element_by_xpath('//body[@class="nimbus-is-editor"]').send_keys(Keys.HOME)
browser.find_element_by_xpath('//body[@class="nimbus-is-editor"]').send_keys(Keys.DOWN)

# 解析页面

print("读取中…")
f = open("知乎回答提取.txt","w",encoding='utf-8')

# 1. 读取问题，写入到txt中
ques = browser.find_element_by_css_selector("#root > div > main > div > div:nth-child(10) > div:nth-child(2) > div > div.QuestionHeader-content > div.QuestionHeader-main > h1").text
ques_des = browser.find_element_by_css_selector("#root > div > main > div > div:nth-child(10) > div:nth-child(2) > div > div.QuestionHeader-content > div.QuestionHeader-main > div:nth-child(3) > div > div > div > span").text
ques_num = browser.find_element_by_css_selector("#QuestionAnswers-answers > div > div > div > div.List-header > h4 > span").text
f.write("======================问题======================")
f.write("\n")
f.write("问题： "+ques)
f.write("\n")
f.write("问题描述： "+ques_des)
f.write("\n")
f.write("共有："+ques_num)

# 2. 读取回答（提取作者，回答的文字内容，赞同人数）

i = 1

# 尝试多页读取

# 计算总共需要拉取的次数
total_num = int(re.search(r"[1-9]\d*", str(ques_num)).group())
total_num = math.floor(total_num/5)

for z in range(total_num):

    for q in range(5):
        answer = browser.find_element_by_css_selector(
            "#QuestionAnswers-answers > div > div > div > div:nth-child(2) > div > div:nth-child(%d)" % i)
        f.write("\n")
        f.write("\n回答%d" % i)
        author = answer.find_element_by_class_name('AuthorInfo-name')
        if author_link := author.find_elements_by_class_name("UserLink-link"):
            author_name = author.find_element_by_class_name("UserLink-link").text
            f.write("\n作者：" + author_name)
        else:
            f.write("\n作者：匿名用户")
        like = answer.find_element_by_class_name("Voters")
        like = like.find_element_by_class_name("Button--plain").text
        like = re.search(r"[1-9]\d*", str(like)).group()
        f.write("\n赞同：" + like + "\n")
        for ans in answer.find_elements_by_class_name("CopyrightRichText-richText"):
            ans = ans.text
            ans = ans.encode("utf-8")
            ans = ans.decode("utf-8")
            f.write("\n" + ans)
        f.write("\n")
        i += 1

    # 每次读取完当前界面，向下拉取获得更多回答
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element_by_xpath('//body[@class="nimbus-is-editor"]').send_keys(Keys.DOWN)
    time.sleep(10)

f.write("======================完毕======================")
f.close()
print("读取完成！")