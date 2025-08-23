import requests
import json
import execjs
from loguru import logger

def Get_X_CSRF_TOKEN():
    headers = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding":"gzip, deflate, br, zstd",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"

    }
    response = requests.get(url="https://passport.weibo.com/sso/signin",headers=headers)
    X_CSRF_TOKEN = response.headers.get("set-cookie").split("X-CSRF-TOKEN=")[1]
    return X_CSRF_TOKEN

def Get_Config_Params(X_CSRF_TOKEN):
    headers={
        "X-CSRF-TOKEN":X_CSRF_TOKEN,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    url = "https://passport.weibo.com/sso/v2/web/config"
    response = requests.post(url = url, headers = headers).text
    results = json.loads(response)
    params ={
        "nonce":results["data"]["nonce"],
        "reg_url":results["data"]["reg_url"],
        "pubkey":results["data"]["pubkey"],
        "rsakv":results["data"]["rsakv"],
        "servertime":results["data"]["servertime"]
    }
    return params

if __name__ == "__main__":
    X_CSRF_TOKEN = Get_X_CSRF_TOKEN()
    Config_Params = Get_Config_Params(X_CSRF_TOKEN)
