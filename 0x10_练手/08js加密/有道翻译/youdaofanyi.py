import requests
import time
import hashlib
import random
###获取目标失败,暂时不清楚原因,但基本的逆向加密过程已经了解,参考链接是https://mp.weixin.qq.com/s?__biz=Mzg2NzYyNjg2Nw==&mid=2247490003&idx=1&sn=81080d79b623871033c4ebd3b9f1690a&source=41#wechat_redirect

def get_ts():
    #获取时间戳
    ts = int(time.time()*1000)
    return ts

def get_bv():
    #生成bv
    appVersion = "5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
    m = hashlib.md5()#获取一个md5加密算法对象
    m.update(appVersion.encode("utf-8"))#制定需要加密的字符串,encode("utf-8")将字符串转码成二进制格式
    bv=m.hexdigest()#获取加密后的16进制字符串
    return bv

def get_salt(ts):
    #生成salt
    num = int(random.random()*10)
    salt = str(ts) + str(num)
    return salt

def get_sign(salt,content):
    #生成sign
    a="fanyideskweb"
    b=str(content)
    c=salt
    d="Y2FYu%TNSbMCxc3t2u^XT"

    e = a+b+str(c)+d
    m=hashlib.md5()
    m.update(e.encode("utf-8"))
    sign=m.hexdigest()

    return sign

def get_form_data(content):
    ts = get_ts()
    bv = get_bv()
    salt = get_salt(str(ts))
    sign = get_sign(salt,content)

    form_data = {
        "i":str(content),
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": str(sign),
        "ts": str(ts),
        "bv": str(bv),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    return form_data


url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
    "Cookie":"OUTFOX_SEARCH_USER_ID=-635335213@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=140246323.98572144; JSESSIONID=aaarfpjwaVzM14QEU834x; ___rl__test__cookies=1641615678473",
    "Rerferer":"https://fanyi.youdao.com/",
    "User-Agent":"5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"

}

content = input("请输入要翻译的内容:")

form_data = get_form_data(content)
print(form_data)
response = requests.post(url=url,data=form_data,headers=headers)
print(response.content)