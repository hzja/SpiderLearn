# -*- coding: utf-8 -*-
# @Author: CriseLYJ
# @Date:   2020-08-14 12:13:11
#曾运行成功过一次，但无法得到username
import re
import requests


class GithubLogin(object):

    def __init__(self, email, password):
        # 初始化信息
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://github.com/',
            'Host': 'github.com'
        }

        self.session = requests.Session()
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.email = email
        self.password = password

    def login_GitHub(self):
        # 登录入口
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': self.email,
            'password': self.password
        }
        resp = self.session.post(
            self.post_url, data=post_data, headers=self.headers)
        
        print('StatusCode:', resp.status_code)#resp.status_code指响应状态码
        if resp.status_code != 200:
            print('Login Fail')
        match = re.search(r'"user-login" content="(.*?)"', resp.text)
        user_name = match.group(1)
        print('UserName:', user_name)



    # Get login token
    def get_token(self):

        response = self.session.get(self.login_url, headers=self.headers)

        if response.status_code != 200:
            print('Get token fail')
            return None
        match = re.search(
            r'name="authenticity_token" value="(.*?)"', response.text)# re.search(pattern,string,[flags])；其中，pattern指模式字符串，string指要匹配的字符串，flags指可选参数,比如re.I 不区分大小写
        if not match:
            print('Get Token Fail')
            return None
        return match.group(1)


if __name__ == '__main__':
    email = '3154990254@qq.com'#input('Account:')
    password = '647561hzj' #input('Password:')

    login = GithubLogin(email, password)
    login.login_GitHub()
