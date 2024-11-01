from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from PIL import Image
from io import BytesIO
from time import sleep
import random

"""
info:
author:CriseLYJ
github:https://github.com/CriseLYJ/
update_time:2019-3-7
现在b站已经更换了验证码的形式，不再是滑动验证，改成了点击文字验证，代码需要作出适当的修改才能成功登陆b站。
"""


class BiliBili():
    """
    登陆B站, 处理验证码
    电脑的缩放比例需要为100%, 否则验证码图片的获取会出现问题
    """

    def __init__(self, username, password):
        """
        初始化
        """
        options = webdriver.ChromeOptions()#用selenium启动Chrome浏览器时，启动的是裸浏览器，什么也没有;用ChromeOptions类接收selenium启动配置参数
        # 设置为开发者模式，避免被识别
        options.add_experimental_option('excludeSwitches',['enable-automation'])#用add_experimental_options方法添加实验性质的设置参数;enable-automation是指允许自动化操作
        self.browser = webdriver.Chrome(options=options)
        self.url = 'https://passport.bilibili.com/login'#bilibili登录界面网址
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 5, 0.2)
        """
        WebDriverWait其中的第一个参数是driver,指浏览器驱动;第二个参数是timeout，最长超时时间,默认以秒为单位;
        第三个参数是poll_frequency,检测的间隔步长,默认为0.5s;
        第四个参数是ignored_exceptions,指超时后抛出的异常信息，默认抛出NoSuchElementException异常.
        """
        self.username = username
        self.password = password

    def get_button(self):
        """
        获取滑动块, 并且返回
        :return: button
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#geetest-wrap > div > div.btn-box > a.btn.btn-login')))
        return button

    def get_screenshot(self, button):
        """
        获取网页两次截图:
            1. 鼠标悬停于button的截图
            2. 鼠标点击button后的截图
        :param button: 滑动块
        :return: 两次截图的结果
        """
        ActionChains(self.browser).move_to_element(button).perform()
        """ActionChains类用于模拟鼠标操作;调用ActionChains类时，不会立即执行，会将所有操作按顺序放在一个队列中，调用perform()方法时队列会按照时间执行
        move_to_element()方法是将鼠标移动到某一个元素"""
        screenshot1 = self.browser.get_screenshot_as_png()
        """用get_screenshot_as_png得到屏幕截图"""
        screenshot1 = Image.open(BytesIO(screenshot1))
        """Image.open()打开图片是PIL类型;BytesIO()函数是用于内存中读写bytes(二进制数据)"""
        ActionChains(self.browser).click_and_hold(button).perform()
        """click_and_hold()方法是点击鼠标左键不松开"""
        screenshot2 = self.browser.get_screenshot_as_png()
        screenshot2 = Image.open(BytesIO(screenshot2))

        return (screenshot1, screenshot2)
    def get_position(self, button):
        """
        获取验证码图片的位置
        :return: 位置的四个点参数
        """
        ActionChains(self.browser).move_to_element(button).perform()
        """
        调用ActionChains方法，可以模拟鼠标操作；
        但调用ActionChains方法时不会立即执行，而是会将所有的操作按顺序存放在一个队列里;
        当调用perform()方法时，队列中的时间会依次执行;
        分为链式写法和分步写法;
        move_to_element(button)指的是鼠标移动到button元素
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_box')))#class_name不能准确定位到元素
        sleep(2)#等待两秒
        location = img.location#获取图片位置
        size = img.size#获取图片的尺寸
        print(location, size)
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], \
                                   location['x'] + size['width']
        return top, bottom, left, right

    def get_geetest_image(self, button, name1='captcha1.png', name2='captcha2.png'):
        """
        获取两次验证码的截图:
            1. 鼠标悬停于button的截图
            2. 鼠标点击button后的截图
        :param button: 滑动块
        :param name1: 原始验证码保存的名字
        :param name2: 缺块验证码保存的名字
        :return: 两次验证码截图的结果
        """
        top, bottom, left, right = self.get_position(button)
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot(button)
        captcha1 = screenshot[0].crop((left, top, right, bottom))#使用crop函数可以对图片进行裁切
        captcha1.save(name1)#使用save函数可以对图片进行保存
        captcha2 = screenshot[1].crop((left, top, right, bottom))
        captcha2.save(name2)
        return (captcha1, captcha2)

    def login(self):
        """
        打开浏览器,并且输入账号密码
        :return: None
        """
        self.browser.get(self.url)
        username = self.wait.until(EC.element_to_be_clickable((By.ID, 'login-username')))#定位到输入用户名的位置
        password = self.wait.until(EC.element_to_be_clickable((By.ID, 'login-passwd')))#定位到输入密码的位置
        sleep(1)
        username.send_keys(self.username)#往需要输入用户名位置的地方输入用户名
        sleep(1)
        password.send_keys(self.password)#往需要输入密码位置的地方输入密码

    def is_pixel_equal(self, img1, img2, x, y):
        """
        判断两个像素是否相同
        :param img1: 原始验证码
        :param img2: 缺块验证码
        :param x: 像素点的x坐标
        :param y: 像素点的y坐标
        :return: 像素是否相同
        """
        pixel1 = img1.load()[x-1, y]#load()函数为图像分配存储空间并加载像素数据
        pixel2 = img2.load()[x-1, y]
        threshold = 100

        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:#abs()函数返回绝对值,pixel1.pixel2中数据是RGB数值,用判断语句判断两张图片的像素是否相同
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        """
        获取缺口偏移量
        :param img1: 原始验证码
        :param img2: 缺块验证码
        :return: 第二个缺块的左侧的x坐标
        """
        left = 60  # 大致忽略掉第一个缺块
        for i in range(left, img1.size[0]):#img.size[0]指图片的宽度,img.size[1]指图片的高度
            for j in range(img1.size[1]):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        """
        获取滑块移动轨迹的列表
        :param distance: 第二个缺块的左侧的x坐标
        :return: 滑块移动轨迹列表
        """
        track = []
        current = 0
        mid = distance * 2 / 3
        t = 0.2
        v = 0
        distance += 10  # 使滑块划过目标地点, 然后回退
        while current < distance:
            if current < mid:
                a = random.randint(1, 3)
            else:
                a = -random.randint(3, 5)
            v0 = v
            v = v0 + a * t
            move = v0 * t + 0.5 * a * t * t
            current += move
            track.append(round(move))#round()函数对浮点数进行四舍五入
        for i in range(2):
            track.append(-random.randint(2, 3))
        for i in range(2):
            track.append(-random.randint(1, 4))
        print(track)
        return track

    def move_button(self, button, track):
        """
        将滑块拖动到指定位置
        :param button: 滑动块
        :param track: 滑块运动轨迹列表
        :return: None
        """
        ActionChains(self.browser).click_and_hold(button).perform()#click_and_hold()模拟按住鼠标左键在源元素上点击并且不释放
        for i in track:
            ActionChains(self.browser).move_by_offset(xoffset=i, yoffset=0).perform()#move_by_offset()方法将鼠标从其当前位置（或 0,0）移动给定的偏移量.如果坐标在视图窗口之外，那么鼠标将在浏览器窗口之外结束。
            sleep(0.0005)
        sleep(0.5)
        ActionChains(self.browser).release().perform()#release()方法松开鼠标按键

    def crack(self):
        """
        串接整个流程:
            1. 输入账号密码
            2. 获取滑动块
            3. 获取两张验证码图片
            4. 获取滑块移动轨迹
            5. 将滑块拖动至指定位置
        :return:
        """
        self.login()
        button = self.get_button()#得到按钮的位置
        captcha = self.get_geetest_image(button)#获取两次验证码的截图
        left = self.get_gap(captcha[0], captcha[1])#获取缺口偏移量
        print(left)
        track = self.get_track(left)#获取滑块移动轨迹列表
        # 如果尝试登陆失败, 则重新验证, 最多三次
        times = 0
        while times < 3:
            self.move_button(button, track)#将滑块移动至指定位置
            try:
                success = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'gt_info_type'), '验证通过:'))#获取“验证成功”字符是否出现，若出现则验证通过
                print(success)
            except TimeoutException as e:#若出现超时错误，则验证失败
                times += 1
                print('fail')
            else:#不出现超时错误，验证成功
                print('success')
                return None


if __name__ == '__main__':
    ACCOUNT = input('请输入您的账号:')
    PASSWORD = input('请输入您的密码:')

    test = BiliBili(ACCOUNT, PASSWORD)  # 输入账号和密码
    test.crack()#执行整个流程
