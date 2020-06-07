import requests
def get_replies(page_number):
    headers = {
        'cookie': 'CURRENT_FNVAL=16; _uuid=221941B2-66DC-C19C-E872-F1385AD7FFA091362infoc; buvid3=F05DD1FB-8A7F-4D6B-B921-6B6B864FEFD8155822infoc; PVID=2; sid=d6unv9ma; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f',
        'referer': 'https://www.bilibili.com/video/BV1Ki4y187pp?from=search&seid=7147633400336821574',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    url = 'https://api.bilibili.com/x/v2/reply?'
    for number in range(page_number):
        try:
            video_url_params = {
                'jsonp': 'jsonp',
                'pn': number + 1,
                'type': '1',
                'oid': 540179417,
                'sort': '0',
            }
            repliesall = requests.get(url, params=video_url_params, headers=headers).json()['data']['replies']
            for replies in repliesall:
                text = replies['content']['message']
                print('评论：', text)
        except:
            print("无法获取该视频评论")
get_replies(21)


