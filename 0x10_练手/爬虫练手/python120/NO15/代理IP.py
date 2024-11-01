
import requests
from lxml import etree
import random
import telnetlib

# 代理检测函数


def check_ip_port(ip_port):
    for item in ip_port:
        ip = item["ip"]
        port = item["port"]

        try:
            tn = telnetlib.Telnet(ip, port=port, timeout=3)
        except:
            print('[-] ip:{}:{}'.format(ip, port))
        else:
            print('[+] ip:{}:{}'.format(ip, port))
            with open('ipporxy.txt', 'a') as f:
                f.write(ip+':'+port+'\n')
    print("阶段性检测完毕")

# 代理IP的第二种检测办法


def check_proxy(ip_port):
    for item in ip_port:
        ip = item["ip"]
        port = item["port"]
        # url = 'https://api.ipify.org/?format=json'
        url = "http://icanhazip.com/"
        proxies = {
            "http": "http://{}:{}".format(ip, port),
            "https": "https://{}:{}".format(ip, port),
        }
        try:
            # res = requests.get(url, proxies=proxies, timeout=3).json()
            res = requests.get(url, proxies=proxies, timeout=3)
            # if 'ip' in res:
            #     print(res['ip'])
            if res.status_code == 200:
                print(res)

        except Exception as e:
            print(e)


def ip89(pagesize):

    url_format = "https://www.89ip.cn/index_{}.html"
    for page in range(1, pagesize+1):
        url = url_format.format(page)
        text = get_html(url)
        ip_xpath = '//tbody/tr/td[1]/text()'
        port_xpath = '//tbody/tr/td[2]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        # 检测代理是否可用
        check_ip_port(ret)
        # check_proxy(ret)


def ip66(pagesize):
    url_format = "http://www.66ip.cn/{}.html"
    for page in range(1, pagesize+1):
        url = url_format.format(page)
        text = get_html(url)
        ip_xpath = '//table/tr[position()>1]/td[1]/text()'
        port_xpath = '//table/tr[position()>1]/td[2]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        # 检测代理是否可用
        check_ip_port(ret)


def ip3366(pagesize):
    url_format = "https://proxy.ip3366.net/free/?action=china&page={}"
    for page in range(1, pagesize+1):
        url = url_format.format(page)

        text = get_html(url)
        ip_xpath = '//td[@data-title="IP"]/text()'
        port_xpath = '//td[@data-title="PORT"]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        # 检测代理是否可用
        check_ip_port(ret)


def ip_huan():
    urls = ["https://ip.ihuan.me/?page=b97827cc", "https://ip.ihuan.me/?page=4ce63706", "https://ip.ihuan.me/?page=5crfe930",
            "https://ip.ihuan.me/?page=f3k1d581", "https://ip.ihuan.me/?page=ce1d45977", "https://ip.ihuan.me/?page=881aaf7b5"]
    for url in urls:
        text = get_html(url)
        ip_xpath = '//tbody/tr/td[1]/a/text()'
        port_xpath = '//tbody/tr/td[2]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        check_ip_port(ret)


def ip_kuai(pagesize):
    url_format = "https://www.kuaidaili.com/free/inha/{}/"
    for page in range(1, pagesize+1):
        url = url_format.format(page)
        text = get_html(url)
        ip_xpath = '//td[@data-title="IP"]/text()'
        port_xpath = '//td[@data-title="PORT"]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        check_ip_port(ret)


def ip_jiangxi(pagesize):
    url_format = "https://ip.jiangxianli.com/?page={}"
    for page in range(1, pagesize+1):
        url = url_format.format(page)

        text = get_html(url)
        ip_xpath = '//tbody/tr[position()!=7]/td[1]/text()'
        port_xpath = '//tbody/tr[position()!=7]/td[2]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        check_ip_port(ret)


def ip_kaixin(pagesize):
    url_format = "http://www.kxdaili.com/dailiip/1/{}.html"
    for page in range(1, pagesize+1):
        url = url_format.format(page)

        text = get_html(url)
        ip_xpath = '//tbody/tr/td[1]/text()'
        port_xpath = '//tbody/tr/td[2]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        check_ip_port(ret)


def ip_nima(pagesize):
    url_format = "http://www.nimadaili.com/putong/{}/"
    for page in range(1, pagesize+1):
        url = url_format.format(page)

        text = get_html(url)
        ip_xpath = '//tbody/tr/td[1]/text()'
        ret = format_html_ext(text, ip_xpath)
        check_ip_port(ret)


def format_html_ext(text, ip_xpath):
    # 待返回的IP与端口列表
    ret = []
    html = etree.HTML(text)
    ips = html.xpath(ip_xpath)

    print(ips)

    for ip in ips:

        item_dict = {
            "ip": ip.split(":")[0],
            "port": ip.split(":")[1]
        }
        ret.append(item_dict)

    return ret


def format_html(text, ip_xpath, port_xpath):
    # 待返回的IP与端口列表
    ret = []
    html = etree.HTML(text)
    ips = html.xpath(ip_xpath)
    ports = html.xpath(port_xpath)
    # 测试，正式运行删除本部分代码
    print(ips, ports)
    ip_port = zip(ips, ports)
    for ip, port in ip_port:

        item_dict = {
            "ip": ip.strip(),
            "port": port.strip()
        }
        ret.append(item_dict)

    return ret


def get_html(url):
    headers = get_headers()
    try:
        res = requests.get(url, headers=headers, timeout=5)
        return res.text
    except Exception as e:
        print("请求网址异常", e)
        return None


def get_headers():
    uas = [
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
        "Baiduspider-image+(+http://www.baidu.com/search/spider.htm)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Googlebot-Image/1.0; +http://www.google.com/bot.html)",
        "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Sogou News Spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Sosospider+(+http://help.soso.com/webspider.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)"
    ]
    ua = random.choice(uas)
    headers = {
        "user-agent": ua,
        "referer": "https://www.baidu.com"
    }
    return headers


def run():
    ip89(10)
    ip66(10)
    ip3366(2)
    ip_huan()
    ip_kuai(4)
    ip_jiangxi(4)
    ip_kaixin(10)
    ip_nima(5)


if __name__ == "__main__":
    run()
