from selenium import webdriver

driverPath = r'F:\Google\GoogleChrome_80.0.3987.106_PortableSoft\ChromePortable\App\Google Chrome\chromedriver.exe'
driver = webdriver.Chrome(driverPath)
driver.get('https://www.baidu.com/')

input = driver.find_element_by_css_selector('#kw')
input.send_keys('苍老师')

button = driver.find_element_by_css_selector('#su')
button.click()

