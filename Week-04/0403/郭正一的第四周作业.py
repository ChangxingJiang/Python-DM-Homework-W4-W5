#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

movie_list = []


def getRequests():
    urls = [
        "https://movie.douban.com/top250?start={}".format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        data = requests.get(url, headers=headers)
        html = etree.HTML(data.text)
        count = html.xpath("//div[@class='item']")  # 这里是共有的xpath
        for info in count:
            titles = info.xpath("div[2]/div[1]/a/span/text()")  # 电影名称
            directors = info.xpath("div[2]/div[2]/p[1]/text()[1]")  # 导演
            year_country_classify = info.xpath(
                "div[2]/div[2]/p[1]/text()[2]")  # 信息
            stars = info.xpath("div[2]/div[2]/div/span[2]/text()")  # 电影星评
            starpeople = info.xpath("div[2]/div[2]/div/span[4]/text()")  # 电影人数
            details = info.xpath("div[2]/div[2]/p[2]/span/text()")  # 电影的简介
            # print(titles)
            # 标题
            other_title = ""
            for i in range(len(titles)):
                if i == 0:
                    continue
                else:
                    other_title += titles[i].replace("\xa0",
                                                     "").replace("/", "").strip()+" "

            # 导演
            director = temp = ""
            flag = 0
            temp = directors[0].replace("/", " ").replace("\n", "").strip()
            for i in temp:
                if i == ':':
                    flag = (flag+1) % 2
                elif i == "主":
                    break
                elif flag == 1:
                    director += i
            director = director.strip()

            year_country_classify = year_country_classify[0].replace(
                "\xa0", " ").replace("\n", "").strip()
            temp = year_country_classify.split("/")
            people = starpeople[0].replace("人评价", "")
            if not details:
                details.append("")

            movie_list.append({
                "title": {
                    "chinese": titles[0],
                    "others": other_title
                },
                "director": director,
                "year": temp[0].strip(),
                "country": temp[1].strip(),
                "classify": temp[2].strip(),
                "rating": {
                    "num": stars[0],
                    "people": people
                },
                "quote": details[0]
            })

    # for i in movie_list:
    #     print(i)


def output():
    with open("豆瓣TOP250电影.json", "w+", encoding="UTF-8") as file:
        file.write(json.dumps({"data": movie_list}, ensure_ascii=False))
    print("end")


if __name__ == '__main__':
    getRequests()
    output()