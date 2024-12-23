import time
from selenium import webdriver
"""代码已看懂"""

login_url = "http://account.youdao.com/login?service=dict"

xpaths = {'usernameTxtBox': ".//*[@id='username']",
          'passwordTxtBox': ".//*[@id='password']",
          'submitButton': '//*[@id="login"]/div[2]/div/div[1]/form/p[5]/nobr/input',
          }


def login():
    mydriver = webdriver.Chrome()
    mydriver.get(login_url)
    mydriver.maximize_window()

    # Clear Username TextBox if already allowed "Remember Me"
    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

    username = input('Please type your user name:\n')

    # Write Username in Username TextBox
    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

    # Clear Password TextBox if already allowed "Remember Me"
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

    password = input('Please type your password:\n')

    # Write Password in password TextBox
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

    mydriver.find_element_by_xpath('//*[@id="agreePrRule"]').click()#定位到保护规则和隐私条款的勾选框并点击，选中保护规则和隐私条款
    mydriver.find_element_by_xpath(xpaths['submitButton']).click()#定位到登录按钮，并点击
    cookies = mydriver.get_cookies()#得到页面返回的cookies信息
    print(cookies)

    # add sleep
    print('登录成功')
    time.sleep(5)
          

if __name__ == '__main__':
    login()
