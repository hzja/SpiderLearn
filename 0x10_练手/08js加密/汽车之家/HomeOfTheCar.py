# search_after参数设计到js加密,爬取失败
from urllib.parse import urlencode
import requests

base_url = "https://ev.autohome.com.cn/ashx/getMaindataList?1=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76",
    "Referer": "https://car.autohome.com.cn/",
    "Cookie":"fvlid=1701178639001b8ezP0MVmq; sessionid=FE58C1C3-1FB5-4043-9123-1D3FDC82F67F%7C%7C2023-11-28+21%3A37%3A21.620%7C%7C0; autoid=4177688a99cefd1c6ab0d838c0ddd02c; area=469026; __ah_uuid_ng=c_FE58C1C3-1FB5-4043-9123-1D3FDC82F67F; historybbsName4=c-272%7C%E8%B7%AF%E7%89%B9%E6%96%AF; sessionuid=FE58C1C3-1FB5-4043-9123-1D3FDC82F67F%7C%7C2023-11-28+21%3A37%3A21.620%7C%7C0; cookieCityId=110100; sessionip=220.174.153.58; sessionvid=0D105DDE-B3B0-4B0E-8A77-0EABADEC4200; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1709810515; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1709810515; ahsids=5179; historyseries=5179; ahpvno=8; pvidchain=3311421,3311257,3311257; v_no=8; visit_info_ad=FE58C1C3-1FB5-4043-9123-1D3FDC82F67F||0D105DDE-B3B0-4B0E-8A77-0EABADEC4200||-1||-1||8; ref=cn.bing.com%7C0%7C0%7C0%7C2024-03-07+19%3A22%3A37.375%7C2024-03-07+19%3A20%3A06.377; ahrlid=1709810554318SyMkIxM14d-1709810562904",
}
params = {
    "search_after": "1709315122000,1293920",
    "type": "1",
    "sort": "0"
    }
url = base_url + urlencode(params)

response = requests.get(url,headers=headers)
print(response.json())
