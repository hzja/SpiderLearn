import json
import execjs
import requests

data_url = 'http://jzsc.mohurd.gov.cn/Api/webApi/dataservice/query/comp/list?pg=%s&pgsz=15&total=450'

def get_encrypted_data(page):
    headers = {
        'Host': 'jzsc.mohurd.gov.cn',
        'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        "cookie": "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1730455823; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1730455823; HMACCOUNT=44EE8126B8FA6958",
        "timeout":"30000",
        "V":"231012",
        "Accept": "application/json, text/plain, * / *",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN, zh;q = 0.9, en;q = 0.8, en - GB;q = 0.7, en - US;q = 0.6",
        "Accesstoken":"",
        "cache-control":"no-cache",
        "connection":"keep-alive",
        "pragma":"no-cache",
        "sec-ch-ua":'"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":'"Windows"',
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin"
    }
    url = data_url % page
    # url = data_url
    encrypted_data = requests.post(url=url, headers=headers).text
    return encrypted_data


def get_decrypted_data(encrypted_data):
    with open('ReWriteFunc.js', 'r', encoding='utf-8') as f:
        jzsc_mohurd_js = f.read()
    decrypted_data = execjs.compile(jzsc_mohurd_js).call('GetDecryptedData', encrypted_data)
    return json.loads(decrypted_data)


def main():
    # 30页数据
    for page in range(1,30):
        encrypted_data = get_encrypted_data(page)
        decrypted_data = get_decrypted_data(encrypted_data)
        print(decrypted_data)


if __name__ == '__main__':
    main()