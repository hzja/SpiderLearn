import requests
import urllib.parse
import hashlib
import execjs

def get_encrypted_params(user):
        with open('Encrypt.js', 'r', encoding='utf-8') as f:
                www_xiaomiaccount_js = f.read()
        encrypted_params = execjs.compile(www_xiaomiaccount_js).call('EncryptParams', {"user":user})
        return encrypted_params

def Login(user,password):
    headers = {
        'Host': 'account.xiaomi.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    }

    index_url = 'https://account.xiaomi.com/'
    response = requests.get(url=index_url, headers=headers)
    location_url = response.history[1].headers['Location']
    referer = location_url.replace("https://account.xiaomi.com/fe/service/login","https://account.xiaomi.com/fe/service/login/password") + "&_locale=zh_CN"
    cookie = response.history[1].headers['set-cookie'].split(";")[0] + ";pass_ua=web; uLocale=zh_CN; passInfo=login-end;"
    cookies = {
        "deviceId": response.history[1].headers['set-cookie'].split(";")[0],
        "pass_ua":"web",
        "uLocale":"zh_CN",
        "passInfo":"login-end"
    }
    urlparse = urllib.parse.urlparse(location_url)
    query_dict  = urllib.parse.parse_qs(urlparse.query)

    EncryptParams = get_encrypted_params(user)
    user = EncryptParams["encryptedParams"]["user"]

    encrypted_password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest().upper()

    data = {
        "bizDeviceType": '',
        "need_theme": query_dict['needTheme'][0],
        "theme": '',
        "show_active_x":query_dict['showActiveX'][0],
        "service_param": query_dict['serviceParam'][0],
        "callback": query_dict['callback'][0],
        "qs": query_dict['qs'][0],
        "sid": query_dict['sid'][0],
        "_sign": query_dict['_sign'][0],
        "user": user,
        'cc': '+86',
        "password": encrypted_password,
        '_json': True,
        "policyName": "miaccount",
        "captCode": ""
    }

    login_url = "https://account.xiaomi.com/pass/serviceLoginAuth2"

    login_headers = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Encoding": "gzip,deflate,br,zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection":"keep-alive",
        "Content-Length": "878",
        'Host': 'account.xiaomi.com',
        "Origin":"https://account.xiaomi.com",
        "EUI": EncryptParams["EUI"],
        "Referer":referer,
        "Cookie":cookie,
        "sec-ch-ua":'"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":'"Windows"',
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        "x-requested-with":"XMLHttpRequest"
    }
    login_headers["Content-Length"] = "880"

    response = requests.session().post(url=login_url, headers=login_headers,cookies=cookies, data=data)
    print(response.text)

user = "2533105837"
password = "647561hzj"

Login(user, password)
