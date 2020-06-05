import requests
import xlwt
from bs4 import BeautifulSoup

# 解析网页

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "SINAGLOBAL=5320937724813.084.1588775806588; login_sid_t=dcda0435461015c2bc360a2da387ad79; cross_origin_proto=SSL; Ugrow-G0=9ec894e3c5cc0435786b4ee8ec8a55cc; TC-V5-G0=4de7df00d4dc12eb0897c97413797808; _s_tentry=www.baidu.com; Apache=2352044882672.3726.1591352630659; ULV=1591352630670:9:4:4:2352044882672.3726.1591352630659:1591279810169; wb_view_log=1600*9001; WBtopGlobal_register_version=fd6b3a12bb72ffed; UOR=login.sina.com.cn,widget.weibo.com,graph.qq.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhkiDAEoIhVX2S1i-ummLY35JpX5K2hUgL.FoqpeonE1Ke7ShM2dJLoIpLKIgpcIg8ki--4i-8FiK.Ri--4i-8FiK.R; SSOLoginState=1591353497; un=18555018098; SCF=AkFcYD0ueTcaLeY0fcbB2pvkTIq1wmJ7x5KSaeC_ROrddBvB4Q8zl6XGqpHcXxF1sF5sBmqoldhya0j7r9Gq5ro.; SUB=_2A25z3lDuDeRhGeBP6VoT-S3MzzuIHXVQqsUmrDV8PUNbmtAKLUPgkW9NRWQtbaJ3bziLJ0wnv4g8lJhFp2oAhlM0; SUHB=0jB4V1dFyCMYQ9; ALF=1591958334; wb_view_log_6128293047=1600*9001; webim_unReadCount=%7B%22time%22%3A1591354285208%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; TC-Page-G0=f5dfed3e2940fb811083b36cf9149343|1591354289|1591354220",
    "Host": "weibo.com",
    "Referer": "https://weibo.com/p/1005051260555362/home?profile_ftype=1&is_ori=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
response = requests.get("https://weibo.com/p/1005051260555362/home?is_search=0&visible=0&is_ori=1&is_tag=0&profile_ftype=1&page=1#feedtop", headers=headers)
# print(response.content.decode(errors="ignore"))
bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')

# 打开excel并初始化

# 打开excel
book = xlwt.Workbook(encoding = 'utf-8')
# 创建一个工作表
sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok = True)
# 创建标题样式
style = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 为样式创建字体
font.name = '宋体'
font.bold = True # 加粗
style.font = font
# 创建标题单元格背景
pat = xlwt.Pattern()
pat.pattern = xlwt.Pattern.SOLID_PATTERN
pat.pattern_fore_colour = 5
style.pattern = pat
# 居中
alignment = xlwt.Alignment()
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment
# 写入初始化标题
sheet1.write(0,0,'类别',style)
sheet1.write(0,1,'发布时间',style)
sheet1.write(0,2,'转',style)
sheet1.write(0,3,'评',style)
sheet1.write(0,4,'赞',style)
sheet1.write(0,5,'内容',style)
sheet1.write(0,6,'图片',style)

'''
# 读取用户信息
user_name = bs.select_one("#Pl_Official_Headerv6__1 > div.PCD_header > div > div.shadow > div.pf_username > h1").text
user_att = bs.select_one("#Pl_Core_T8CustomTriColumn__3 > div > div > div > table > tbody > tr > td:nth-child(1) > a > strong").text
user_fans = bs.select_one("#Pl_Core_T8CustomTriColumn__3 > div > div > div > table > tbody > tr > td:nth-child(2) > a > strong").text
user_total = bs.select_one("#Pl_Core_T8CustomTriColumn__3 > div > div > div > table > tbody > tr > td:nth-child(3) > a > strong").text
name = user_name + '_关注' + user_att + '_粉丝' + user_fans + '_微博' + user_total + '.xls'
'''

# 开始循环，询问读取多少页
total_page = int(input("亲亲，宁想读取几页鸭："))

print("亲亲，我们开始读取了哟~~~")

for i in range(total_page):

    p = i + 1
    # 解析页面
    response_page = requests.get(
        "https://weibo.com/p/1005051260555362/home?is_search=0&visible=0&is_ori=1&is_tag=0&profile_ftype=1&page="+str(p)+"#feedtop",
        headers=headers)
    page = BeautifulSoup(response_page.content.decode(errors="ignore"), 'lxml')

    # 解析每一条内容
    for q in page.select("#Pl_Official_MyProfileFeed__19 > div > div"):

        num = 1

        if q["action-data"]:

            weibo_time = q.select_one("# div > div.WB_feed_detail.clearfix > div.WB_detail > div.WB_from.S_txt2 > a:nth-child(1)").text
            weibo_forward = q.select_one("# div > div.WB_feed_handle > div > ul > li:nth-child(2) > a > span > span > span > em:nth-child(2)").text
            weibo_comment = q.select_one("# div > div.WB_feed_handle > div > ul > li:nth-child(3) > a > span > span > span > em:nth-child(2)").text
            weibo_like = q.select_one("# div > div.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span > span > em:nth-child(2)").text
            weibo_content = q.select_one("# div > div.WB_feed_detail.clearfix > div.WB_detail > div:nth-child(5)").text
            if type := q.select_one("# div > div.WB_feed_detail.clearfix > div.WB_detail > div.WB_media_wrap.clearfix"):
                weibo_type = "图文"
                weibo_picture = []
                for z in type.select("# div.WB_media_wrap.clearfix > div > ul"):
                    picture = z.select_one("# li > img")["src"]
                    weibo_picture.append(picture)
            else:
                weibo_type = "文字"

            print(weibo_time)
            print(weibo_forward)
            print(weibo_comment)
            print(weibo_like)
            print(content)


            sheet1.write(num, 0 , weibo_type)
            sheet1.write(num, 1 , weibo_time)
            sheet1.write(num, 2 , weibo_forward)
            sheet1.write(num, 3 , weibo_comment)
            sheet1.write(num, 4 , weibo_like)
            sheet1.write(num, 5 , weibo_content)
            if weibo_type == "图文":
                for n in weibo_picture:
                    m = 6
                    sheet1.write(num, m , n)
                    m += 1
            else:
                sheet1.write(num, 6 , "无")

            num += 1

        else:
            print("读取失败")

    print('第%d页 读取完成' % p)

book.save("E:\大学\项目\华榜\培训\Exercise\MJTT木头.xls")
# book.save("E:\大学\项目\华榜\培训\Exercise\\"+name)
print("亲亲，读取完毕了哟~~~")