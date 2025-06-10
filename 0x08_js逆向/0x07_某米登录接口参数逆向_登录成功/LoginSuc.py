import requests
import execjs
from loguru import logger
from urllib.parse import unquote

session = requests.Session()

with open("Encrypt.js", "r", encoding='utf-8') as f:
    js_code = execjs.compile(f.read())

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

def get_index() -> str:
    url = "https://account.xiaomi.com/"
    response = requests.get(url, headers=headers, allow_redirects=False)
    logger.success(response)
    callback_url = response.headers.get("Location")
    logger.debug(callback_url)
    return callback_url

def get_second() -> str:
    callback_url = get_index()
    response = requests.get(callback_url, headers=headers, allow_redirects=False)
    logger.success(response)

    start_data = response.headers.get('Location')
    logger.debug(start_data)

    logger.debug(response.cookies)
    session.cookies.update(response.cookies)
    return start_data

def get_data(start_data: str):
    js_data = js_code.call("get_user_info", "", "")  # 账号密码
    logger.debug(js_data)

    data_dict = start_data.split("&")
    data_dict = [i.split("=") for i in data_dict]
    data_dict = {i[0]: i[1] for i in data_dict}
    logger.debug(data_dict)

    headers["Accept"] = "application/json, text/plain, */*"
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["Referer"] = start_data + "&_locale=zh_CN"
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["Origin"] = "https://account.xiaomi.com"
    
    url = "https://account.xiaomi.com/pass/serviceLoginAuth2"

    headers["EUI"] = js_data["EUI"]

    data = {
        "bizDeviceType": data_dict["bizDeviceType"],
        "needTheme": data_dict["needTheme"],
        "theme": data_dict["theme"],
        "showActiveX": data_dict["showActiveX"],
        "serviceParam": unquote(data_dict["serviceParam"]),
        "callback": unquote(data_dict["callback"]),
        "qs": unquote(data_dict["qs"]),
        "sid": data_dict["sid"],
        "_sign": unquote(data_dict["_sign"]),
        "user": js_data["user"],
        "cc": "+86",
        "hash": js_data["password"],
        "_json": "true",
        "policyName": "miaccount",
        "captCode": ""
    }

    response = session.post(url, headers=headers, data=data)

    logger.success(response)
    logger.info(response.text)
    logger.debug(response.cookies)

def main():
    start_data = get_second()
    get_data(start_data)

if __name__ == "__main__":
    main()
