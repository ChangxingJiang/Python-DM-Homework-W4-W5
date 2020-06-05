import requests
import json
import time
def get_one_comment(offset):
    headers={'Cookie':'_iuqxldmzr_=32; _ntes_nnid=bdaab01e87ee929b3a9a91ea44b5cd45,1534172699282; _ntes_nuid=bdaab01e87ee929b3a9a91ea44b5cd45; __utmc=94650624; WM_TID=M4E4ToHGUg4EetTbOjxEC5J%2BuODh%2B0jj; abt=66; WM_NI=cRw1E4mJtjv9dwKem8xCMaYzUgNNyu8qqM25igmzBYDj%2FJGjHnYTJFFFqen2XIq%2FlCdRUdQxmdIvxSl84%2BvraOwnH1lJboEwOdL6UrZhnx030tzRng9NfOIBNXgIUx7GMUI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6b15cf88bb8ade56a8eb48291f97ca5b9e1d2c45bf6ed9cb9e659b1be8e89ca2af0fea7c3b92aa18eb9d2c840af96bc8bf533a8a98586f034bc9d8382dc7297b982affc7ffcafbfaeb13fabb9a39bc15388b6e1abc6628cb297b5c94e869abf86ed3a9c97bfd0ef49a88e9b85d474afbc8797fb59b0e8fcccf57aa391b98fcb3bb096ae90c87d8dbc84d7d87a9ab8a299b339f4acb6b3ed6dfb92aab0cc4a8e88a9aad874f59983b6cc37e2a3; __utma=94650624.827593374.1534172700.1535852507.1535857189.3; __utmz=94650624.1535857189.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=kgbbgMKEcRf18SvvxZVqNTmWZD%2Fdn8BpA%2F7aMH7vv4mSpiDaE%5CfkC5xPu5hFv0nk5X7PpvlEJJ97%2BC3WyE5Qv50EW%2FdNPQQPenibqq%2F5IyHkuuMlCTkpkb7TRMl9oBEdFi68ktMI8m%2F5Ilyub4P204bpG0qBv4yx9vvw8CmCJ%2B9vCaSd%3A1535859527007; __utmb=94650624.7.10.1535857189',	'Referer':'https://music.163.com/song?id=1299557768',	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'	}
    url='http://music.163.com/api/v1/resource/comments/R_SO_4_35804605?offset='+str(offset)+'&limit=20'
    try:
        time.sleep(2)
        response=requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print('出错啦！')
        return None
def parse_json_data(contents):
    if contents:
        contents=contents.decode('utf-8')
        comments=json.loads(contents)['comments']
        for comment in comments:
            content=comment['content']
            print(content)
if __name__ == '__main__':
    for number in range(0,1900,20):
        parse_json_data(get_one_comment(number))

