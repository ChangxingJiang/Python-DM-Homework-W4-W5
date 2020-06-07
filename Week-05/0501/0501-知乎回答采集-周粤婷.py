import requests
from bs4 import BeautifulSoup
import re
import json
def main():
    url = "https://www.zhihu.com/api/v4/questions/358242872/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,"html.parser")
    json_data = json.loads(html.text)["data"]
    total = json.loads(html.text)["paging"]['totals']
    count = 0
    while count<total:
        update_url = 'https://www.zhihu.com/api/v4/questions/358242872/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset='+str(count)+'&platform=desktop&sort_by=default'
        update_html = requests.get(update_url, headers=headers)
        update_soup = BeautifulSoup(update_html.text, "html.parser")
        update_json_data = json.loads(update_html.text)["data"]
        for item in update_json_data:
            author = item['author']['name']
            content = item['content']
            content = content.replace('<p>','')
            content = content.replace('</p>', '')
            content = content.replace('<b>', '')
            content = content.replace('</b>', '')
            print(author+"："+content)
        count += 5
if __name__ == '__main__':
    main()