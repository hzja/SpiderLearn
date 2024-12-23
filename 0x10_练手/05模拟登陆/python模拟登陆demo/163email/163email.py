import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
"""代码已看懂"""

def login():
    acount_num = input('请输入账号:\n')
    passwd_str = input('请输入密码:\n')
    driver = webdriver.Chrome()
    url = 'http://mail.163.com/'
    driver.get(url)


    # # 等待页面加载完成，出现可以点击到密码登录的button
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.element_to_be_clickable((By.ID, 'lbNormal')))
    # driver.find_element_by_id('lbNormal').click()


    elem = driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")#定位iframe
    driver.switch_to.frame(elem)#切换到iframe
    # 使用CSSSelector正则匹配头部
    # 163登陆框是使用iframe进行嵌套的，所以需要先定位到iframe,再切换到iframe进行操作

    account_el = driver.find_element_by_xpath('//input[@name="email"]')
    account_el.clear()
    account_el.send_keys(acount_num)

    password_el = driver.find_element_by_xpath('//input[@name="password"]')
    password_el.clear()
    password_el.send_keys(passwd_str)

    login_el = driver.find_element_by_xpath('//a[@id="dologin"]')
    login_el.click()

    time.sleep(10)
    cur_cookies = driver.get_cookies()#得到页面返回的cookies，并可用于下一次直接登录
    print(cur_cookies)
    return cur_cookies


if __name__ == '__main__':
    login()
