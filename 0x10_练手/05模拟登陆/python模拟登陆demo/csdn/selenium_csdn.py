# -*- coding: utf-8 -*-
# @Author: Kris
# @Mail: criselyj@163.com
# @Date:   2020-08-14 17:40:11
import os
import random
import asyncio
from pyppeteer import launch

"""现在没有验证，代码运行成功"""
base_url = 'https://passport.csdn.net/login'#基本路径
current_dir = os.path.dirname(os.path.realpath(__file__))
# os.path.dirname()函数去除文件名,返回文件所属目录;
# os.path.realpath(__file__)函数用于获取当前执行脚本的绝对路径

# Fix:https://github.com/miyakogi/pyppeteer/issues/183 文件权限问题。
cache_dir = os.path.join(current_dir, 'cache')

#os.path.join()函数功能：连接两个或更多的路径名组件;如果各组件名首字母不包含’/’，则函数会自动加上;

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)

# os.path.exists()用于判断括号里的文件是否存在,返回布尔值
# os.mkdir()用于创建一级目录


class Api(object):
    def __init__(self, account, password):
        self.url = base_url
        self.account = account
        self.password = password
        self.browser = None
        self.page = None

    async def send_key(self):
        await asyncio.sleep(random.randint(2, 3))
# await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误;
# await语法可以挂起自声协程，等待另一个协程完成直到返回结果.
# sleep()函数指等待一些时间

        switch_btn = await self.page.xpath('//*[@id="tabOne"]')
        """page可打开一个新的页面,xpath匹配目标."""
        await switch_btn[0].click()
        print("账号:%s\n密码:%s"%(self.account,self.password))
        input_account = await self.page.xpath('//*[@id="all"]')
        await input_account[0].type(self.account,{'delay': random.randint(100, 200) - 50})
        """type() 函数中若只有第一个参数则返回对象的类型，有三个参数返回新的类型对象"""
        await self.page.type('#password-number', self.password,{'delay': random.randint(100, 200) - 50})
        await self.page.click('button[data-type=account]')
        await asyncio.sleep(random.randint(5, 10))
        # scroll_btn = await self.page.xpath('//*[@id="nc_1_n1z"]')
        # scroll_kuangjia = await self.page.xpath('//*[@id="nc_1__scale_text"]/span')


    async def crawl(self):
        # 测试环境下 headless 设置为 False
        # 生产环境可以修改为无头浏览器
        self.browser = await launch({
#launch用来启动一个子协程并立即返回，协程像线程一样异步执行,协程中的未捕获异常会导致进程的crash;
# launch返回一个Job对象，通过Job.join方法可以同步等待协程的完成，就像thread的join一样
            'headless': False,
            'userDataDir': cache_dir,
            'defaultViewport': {'width': 1440, 'height': 1000},
            'args': ['--no-sandbox']
        })
        self.page = await self.browser.newPage()#avait self.browser.newPage()用于打开一个新的页面;
        await self.page.goto(self.url)
#avait self.page.goto(self.url)用于输入网址回车

# 伪造当前浏览状态 防止自动化工具检测
        codes = (
            "() =>{ Object.defineProperties(navigator,{ webdriver:"
            "{ get: () => false } }) }",
            "() =>{ window.navigator.chrome = { runtime: {},  }; }",
            "() =>{ Object.defineProperty(navigator, 'languages', "
            "{ get: () => ['en-US', 'en'] }); }",
            "() =>{ Object.defineProperty(navigator, 'plugins', { "
            "get: () => [1, 2, 3, 4, 5,6], }); }"
        )
        for code in codes:
            await self.page.evaluate(code)
        await self.send_key()
# page.evaluate(pageFunction [,...args]), 返回pageFunction执行的结果,
# pageFunction表示要在页面执行的函数或表达式，args表示传入给pageFunction的参数；
# send_keys()函数用于发送数据



def main():
    print('[*] 模拟登陆 CSDN 程序启动...')
    account = input('[*] 请输入账号：')
    password = input('[*] 请输入密码：')
    login = Api(account, password)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(login.crawl())
    

if __name__ == '__main__':
    main()
