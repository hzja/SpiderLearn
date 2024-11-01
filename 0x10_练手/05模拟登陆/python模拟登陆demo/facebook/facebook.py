from __future__ import print_function

import argparse
import requests
import pyquery
#运行失败,难点：如何给email和password两个变量赋值

def login(session, email, password):
    """
    获取cookie
    """
    response = session.get('https://m.facebook.com')

    # 尝试登陆
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)#allow_redirects=False表示禁止重定向

    if 'c_user' in response.cookies:
        # 说明登陆成功
        homepage_resp = session.get('https://m.facebook.com/home.php')

        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))#初始化pyquery.PyQuery()对象
        fb_dtsg = dom('input[name="fb_dtsg"]').val()#dom()创建DOM集合，返回只有第一个元素的value的值,.val()用于获取相关元素的val值

        return fb_dtsg, response.cookies['c_user'], response.cookies['xs']
    else:
        return False


if __name__ == "__main__":
    email = '315499024@qq.com'
    password = '647561hzj'
    parser = argparse.ArgumentParser(description='Login to Facebook')#argparse.ArgumentParser()创建一个解析对象
    parser.add_argument('email', help='Email address')#parser.add_argument()用于向该对象中添加关注的命令行参数和选项
    parser.add_argument('password', help='Login password')

    args = parser.parse_args()#args = parser.parse_args()   进行解析

    session = requests.session()#session会话对象可以跨请求保持某些参数
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    })

    fb_dtsg, user_id, xs = login(session, args.email, args.password)

    if user_id:
        print('{0}:{1}:{2}'.format(fb_dtsg, user_id, xs))#{}.format() 输出格式化方法
    else:
        print('Login Failed')
