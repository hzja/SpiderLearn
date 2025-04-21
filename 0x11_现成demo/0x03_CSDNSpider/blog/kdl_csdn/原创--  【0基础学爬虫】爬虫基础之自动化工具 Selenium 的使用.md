# 原创
：  【0基础学爬虫】爬虫基础之自动化工具 Selenium 的使用

# 【0基础学爬虫】爬虫基础之自动化工具 Selenium 的使用

> 
大数据时代，各行各业对数据采集的需求日益增多，网络爬虫的运用也更为广泛，越来越多的人开始学习网络爬虫这项技术，K哥爬虫此前已经推出不少爬虫进阶、逆向相关文章，为实现从易到难全方位覆盖，特设【0基础学爬虫】专栏，帮助小白快速入门爬虫，本期为自动化工具 Selenium 的使用。


### 概述

目前，很多网站都采用 Ajax 等技术进行动态加载数据，想要采集这类网站的数据，需要通过抓包对网站的数据接口进行分析，去寻找想要采集的数据由哪个接口传输。而且，就算找到了数据接口，这些接口可能也是被加密过的，想要通过接口获取数据，需要对加密参数进行逆向分析，这个过程对于初学者来说非常复杂。

为了解决这些问题，能够更加简单的进行爬取数据，我们可以使用到一些自动化工具，如 Selenium、playwright、pyppeteer 等，这些工具可以模拟浏览器运行，直接获取到数据加载完成后的网页源码，这样我们就可以省去复杂的抓包、逆向流程，直接拿到数据。

### Selenium 的使用

#### 介绍

Selenium 是一个流行的自动化测试框架，可用于测试 Web 应用程序的用户界面。它支持多种编程语言，如Java、Python、Ruby等，并提供了一系列 API，可以直接操作浏览器进行测试。

#### 安装

使用 selenium 首先需要下载浏览器驱动文件，这里以谷歌浏览器为例。在[驱动下载](http://chromedriver.storage.googleapis.com/index.html)页面找到与自己浏览器版本最为接近的文件，如我的谷歌浏览器版本为 `112.0.5615.86`，最接近的文件为 `112.0.5615.49`，选择此文件，下载对应系统版本的压缩包，将压缩包中的chromedriver.exe程序放到python目录中。因为正常情况下Python在安装时就会被添加到系统环境变量之中，将chromedriver.exe放到Python目录下它就可以在任意位置被执行。

添加好驱动文件后需要安装 Python 的第三方库 selenium。

`pip install selenium`

#### 使用

Selenium 支持多种浏览器，如谷歌、火狐、Edge、Safari等，这里我们以谷歌浏览器为例。

```
from selenium import webdriver

# 初始化浏览器对象
driver = webdriver.Chrome()
# 驱动浏览器打开目标网址
driver.get('https://www.baidu.com/')
# 打印当前页面的源代码
print(driver.page_source)
# 关闭浏览器
driver.quit()
```

运行代码后我们会发现自动打开了一个浏览器，访问了目标网址，在控制台输出了页面的源代码，然后自动关闭。

Selenium 提供了一系列实用的 Api，通过它我们可以实现更多操作。

##### 元素查找

在之前的文章《解析库的使用》中，我们已经讲到了 Xpath、bs4 这两个库的使用方法，讲到了 Xpath 的路径表达式和 CSS 选择器，因此这里主要讲解定位方法，路径表达式与 CSS 选择器的使用可以去前文中了解。

以京东首页为例，想要获取秒杀栏目的商品信息，我们可以通过多种方法来进行定位。

```
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.jd.com/')
# 根据 Xpath 定位
goods_xpath = driver.find_elements(By.XPATH, '//div[@class="slider_list"]/div/a[@class="slider_item seckill-item slider_active"]')

# 根据 Css 选择器定位
goods_css = driver.find_elements(By.CSS_SELECTOR, 'a[class="slider_item seckill-item slider_active"]')

# 根据类名定位
goods_class_name = driver.find_elements(By.CLASS_NAME,'seckill-item')

print(goods_xpath)

for goods in goods_xpath:
    # 输出节点的文本信息
    print(goods.text)

driver.quit()
# [&lt;selenium.webdriver.remote.webelement.WebElement(session="f49c1906753e404ca0a017...]
# 欧臻廷保湿修护亮颜银霜面霜70ml护肤品化妆品乳液滋润送女友礼物礼盒款
# ¥1380.00
# Redmi K50Pro 天玑9000 AMOLED 2K柔性直屏 OIS光学防抖 120W快充 幻镜 8GB+256GB 5G智能手机 小米红米
# ¥2619.00
# 卡诗（KERASTASE）黑钻钥源鱼子酱洗发水250ml 改善毛躁呵护受损
# ¥219.00
```

除了示例代码中的，还有其它定位方法：

> 
driver.find_elements(By.ID,'ID') driver.find_elements(By.LINK_TEXT,'LINK_TEXT') driver.find_elements(By.PARTIAL_LINK_TEXT,'PARTIAL_LINK_TEXT') driver.find_elements(By.TAG_NAME,'TAG_NAME')


##### 元素交互

Selenium 可以实现对页面中元素的点击、输入等操作。

想要采集京东的指定商品信息，首先需要在输入框输入商品名称，然后点击搜索按钮，网页就会跳转到搜索页面，展示我们搜索的商品信息。这个流程我们也可以通过 Selenium 来模拟实现。

```
driver.get('https://www.jd.com/')
# 获取搜索框
search = driver.find_element(By.XPATH,'//div[@role="serachbox"]/input')
# 获取查询按钮
button = driver.find_element(By.XPATH,'//div[@role="serachbox"]/button')
# 在搜索框中输入 Python
search.send_keys('Python')
# 点击查询按钮
button.click()
```

##### 等待

在我们使用 Selenium 时会遇到以下两种情况：
1. 页面未加载完毕，但是我们需要的元素已经加载完毕1. 页面加载完毕，但是我们需要的元素为加载完毕
Selenium 的 get 方法是默认等待页面加载完毕后再执行下面的操作。在遇到第一种情况时，要采集的数据已经生成了，但是可能由于某个资源加载缓慢导致页面一直在加载中状态，这样 Selenium 就会一直等待页面完全加载，造成采集速度缓慢等问题。而情况二，页面已经加载完成了，但是要采集的数据依旧没有渲染出来，这就使 Selenium 定位元素失败导致程序异常。为了避免解决这两种情况，我们可以设置不等待页面完全加载，只等待目标元素加载完毕。

```
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities().CHROME
#不等待页面加载
caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps)
```

**强制等待**

使用 time.sleep() 实现强制等待。不推荐使用。

```
driver.get('https://www.jd.com/')
# 强制休眠6秒
time.sleep(6)
```

**隐式等待**

等待页面加载的时间，当页面加载完成后执行下一步，如果加载时间超过设置的时间时直接执行下一步。不推荐使用。

```
# 隐式等待10秒
driver.implicitly_wait(10)
driver.get('https://www.jd.com/')
```

**显式等待**

等待条件满足后执行下一步，条件不满足则一直等待，当超过设置的时间时抛出异常。推荐使用。

```
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.jd.com/')
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'a[class="slider_item seckill-item slider_active"]')
        )
    )
except selenium.common.exceptions.TimeoutException:
    print('元素加载超时')
```

当 CSS 选择器指向的元素存在时则执行下一部，不存在则继续等待，直到超过设置的10秒，抛出超时异常。

##### Actions

上文中讲到了元素交互，其中点击、输入行为都是属于 Selenium 的动作 Api 之中的，除此之外，Selenium还提供了非常丰富的动作 Api，这里只介绍常用的方法。

**鼠标操作**

```
from selenium.webdriver import ActionChains

# 单击元素并按住
clickable = driver.find_element(By.ID, "clickable")
ActionChains(driver).click_and_hold(clickable).perform()

# 双击，将鼠标移动到元素中心并双击
clickable = driver.find_element(By.ID, "clickable")
ActionChains(driver).double_click(clickable).perform()

# 按偏移量移动鼠标
mouse_tracker = driver.find_element(By.ID, "mouse-tracker")
ActionChains(driver).move_to_element_with_offset(mouse_tracker, 8, 0).perform()

# 按当前指针位置进行偏移，如之前没有移动鼠标，则默认在窗口的左上角。(13, 15)为横纵坐标的偏移值，13为向右移动13，15为向下移动15，负数则反之。
ActionChains(driver).move_by_offset( 13, 15).perform()

# 按偏移拖放。点击元素并按钮，移动指定偏移量，然后释放鼠标
draggable = driver.find_element(By.ID, "draggable")
start = draggable.location
finish = driver.find_element(By.ID, "droppable").location
ActionChains(driver).drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']).perform()
```

**滚轮**

```
# 滚动到指定元素
iframe = driver.find_element(By.TAG_NAME, "iframe")
ActionChains(driver).scroll_to_element(iframe).perform()
# 按给定值滚动，(0, delta_y) 为向右和向下滚动的量，负值则反之。
footer = driver.find_element(By.TAG_NAME, "footer")
delta_y = footer.rect['y']
ActionChains(driver).scroll_by_amount(0, delta_y).perform()
```

##### 反检测

Selenium 有着非常明显的缺陷，就是容易被网站检测到。我们通过 Selenium 打开网页时会发现，窗口上方会显示浏览器正受到自动测试软件的控制，这就说明 Selenium 驱动浏览器与用户正常打开浏览器是不同的，它存在着许多 WebDriver 的特征，网站可以通过检测这些特征来禁止 Selenium 访问。

我们可以通过一些特征值检测的网站来对比正常访问与 Selenium 访问的区别。

上面是正常访问，下面是 Selenium 访问，可以很清晰的看到 WebDriver 一栏标红了，这就说明 Selenium 被检测到了。网站的检测原理主要是通过检查 window.navigator 对象中是否存在 webdriver 属性。我们了解到这一点后，可以通过一些操作来修改window.navigator 对象，在页面未加载时将它的 webdriver 属性设置为 false，这样或许就能避开网站的检测机制。

```
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
# 以最高权限运行
options.add_argument('--no-sandbox')
# navigator.webdriver 设置为 false
options.add_argument("--disable-blink-features=AutomationControlled")
# 隐藏"Chrome正在受到自动软件的控制"提示
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
with open('./stealth.min.js', 'r') as f:
    js = f.read()
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
```

可以看到，我们进行了一些隐藏特征的操作，但在最后我们读取一个文件，然后将这个文件信息传入到了execute_cdp_cmd()方法中，这个操作其实也是在隐藏特征。

stealth.min.js 来自于 puppeteer 的一个插件，puppeteer 是一个控制 headless Chrome 的 Node.js API ，puppeteer 有一个插件名为 puppeteer-extra-plugin-stealth，它的开发目的就是为了防止 puppeteer 被检测，它可以隐藏许多自动化特征。puppeteer-extra 的作者也编写了一个脚本，用于将最新的特征隐藏方法puppeteer-extra-stealth 提取到 JS 文件之中，生成的 JS 文件可以用于纯 CDP 实现，也可以用于测试开发工具中的检测规避。而 Selenium 正好支持 CDP 的调用，CDP 全称（Chrome DevTools Protocol），利用它可以在浏览器加载之前执行 JS 语句。

如果你已经安装了 node.js ，`npx extract-stealth-evasions` 执行此命令就可以生成 stealth.min.js 文件。下图就隐藏特征后访问结果。

##### 无头模式

无头模式下网站运行不会弹出窗口，可以减少一些资源消耗，也避免了浏览器窗口运行时对设备正常使用带来的影响，在服务器上运行需要用到。但是无头模式下被网站检测的特征点非常多，因此需要根据自己的应用场景来使用。

```
options = ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
```

### 总结

使用 Selenium 来进行数据的爬取是一种优势与劣势都非常明显的选择。它的优势就是简单，不需要对网站进行调试，不需要关注数据的来源，大大减少了爬虫程序的开发时间。它的劣势有多种：采集效率低，资源占用大，不稳定，容易被检测，且需要依赖于 WebDriver，当浏览器更新后就需要更新对应的 WebDriver。因此 Selenium 适用于那些逆向难度较大，且对采集效率要求不高的场景。 <img alt="" src="https://i-blog.csdnimg.cn/blog_migrate/b2811fd8dedfa96b8fe2cc26e920c71f.png"/>
