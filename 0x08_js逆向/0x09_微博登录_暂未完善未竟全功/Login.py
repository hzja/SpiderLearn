import requests
# verify='path/to/certfile.pem'
import urllib3
import re
import random
import time
from dateutil import parser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.session()

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}
url = "https://passport.weibo.com/visitor/genvisitor2"
data = {
    "cb": "visitor_gray_callback",
    "tid": "01AUXHE0uWNcmbV0Qlq3L-R4dZHGS_3E7eKqUtdA9HiUgQ",
    "from": "weibo",
    "webdriver": "false"
}
response = session.post(url, headers=headers, data=data, verify=False)
sub = match = re.search(r'"sub":"([^"]+)"', str(response.text)).group(1)

cookies = {
    'SUB': sub,
}
page = input('请输入您想看到的页数： ')
params = {
    'refresh': '2',
    'group_id': '102803',
    'containerid': '102803',
    'extparam': 'discover|new_feed',
    'max_id': page,  # 第几页
    'count': '10',
}

response = session.get('https://weibo.com/ajax/feed/hottimeline', params=params, cookies=cookies, headers=headers,
                       verify=False)
wait_time = random.uniform(1, 3)
time.sleep(wait_time)
data_news = response.json()['statuses']


def get_comments(index, item):
    params = {'flow': 0, 'is_reload': '1', 'id': item['id'], 'is_show_bulletin': '2', 'is_mix': '0', 'count': '20',
              'uid': '1700720163', 'fetch_level': '0', 'locale': 'zh-CN'}

    response = session.get('https://weibo.com/ajax/statuses/buildComments', params=params,
                           headers=headers, verify=False).json()
    time.sleep(random.uniform(1, 3))
    conmments = response['data']
    for item in conmments:
        time_1 = item["created_at"]
        dt_1 = parser.parse(time_1)  # 自动解析
        time_2 = dt_1.strftime("%Y-%m-%d")
        name = item["user"]["screen_name"]
        result = item["text"].replace('\n', '').strip()
        results = clean_weibo_text(result)
        f.write(f"用户：{name}  内容：{results}   时间：{time_2}\n")
        f.write('\n')


def clean_weibo_text(text):
    # 去除<img>标签，但保留alt中的表情文字如[微笑]
    text = re.sub(r'<img\s+[^>]*alt="(\[[^\]]+\])"[^>]*>', r'\1', text)
    # 去除其他HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    # 去除用户卡片的特殊标记（保留@用户名）
    text = re.sub(r' usercard="[^"]*"', '', text)
    # 去除href属性（保留链接文本）
    text = re.sub(r'<a\s+[^>]*href=[^>]*>([^<]+)</a>', r'\1', text)
    return text


with open('新浪微博.txt', 'a', encoding='utf-8') as f:
    for index, item in enumerate(data_news, start=1):
        time_str = item['created_at']
        dt = parser.parse(time_str)  # 自动解析
        formatted_date = dt.strftime("%Y-%m-%d")
        f.write(str(item['id']) + '\n')
        f.write(f"{item['user']['screen_name']} {item['source']}\n")
        f.write(f"{item['text_raw']} {formatted_date}\n")
        f.write(f"转发：{item['reposts_count']}  评论：{item['comments_count']}  点赞：{item['attitudes_count']}\n")
        print(f"第{index}条微博内容下载完成")
        f.write('\n')
        f.write('\n')
        get_comments(index, item)
        print(f"第{index}条微博评论内容下载完成")
#         # 添加空行分隔不同条目