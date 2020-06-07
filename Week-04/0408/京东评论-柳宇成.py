from selenium import webdriver
import time

browser = webdriver.Chrome(
    executable_path="C:\Python\chromedriver.exe")  # 使用selenium启动浏览器，打开url
browser.get("https://item.jd.com/12413059.html#comment")
time.sleep(3)
x = 0

print("----------京东评论----------")
while x < 5:  # x的数即位评论想要抓取的页数
    for movie_label in browser.find_elements_by_css_selector(
            "#comment-0 > div > div.comment-column.J-comment-column > p"):
        print(movie_label.text)
    time.sleep(3)
    # NextPageButton = browser.find_element_by_link_text("下一页")
    NextPageButton = browser.find_element_by_css_selector(
        "#comment-0 > div.com-table-footer > div > div > a.ui-pager-next")  # 定位到“下一页”
    browser.execute_script("arguments[0].click();",
                           NextPageButton)  # 查到的JavaScript的翻页方法，nextpagebutton.click()为啥不行不是很清楚
    time.sleep(5)  # 表格中数据有变化时，页面会自动刷新，导致找不到元素,页面还没加载好就点击下一页了，就会报错
    x += 1
print("----------End----------")
