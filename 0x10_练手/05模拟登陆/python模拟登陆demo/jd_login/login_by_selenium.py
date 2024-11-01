# tested on ubuntu15.04
import time
from selenium import webdriver
#登录失败,暂时没想到别的方法
login_url = 'https://passport.jd.com/new/login.aspx'
driver = webdriver.PhantomJS()
driver.get(login_url)
time.sleep(5)

account = driver.find_element_by_id('loginname')
password = driver.find_element_by_id('nloginpwd')
submit = driver.find_element_by_id('loginsubmit')

account.send_keys('jd158312uto')
password.send_keys('647561hzj')

submit.click()
time.sleep(5)

# cookie和前面一样的方式获取和保存
cookies = driver.get_cookies()
print(type(cookies))
driver.close()
