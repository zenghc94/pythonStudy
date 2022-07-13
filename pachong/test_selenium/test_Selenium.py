# Python 爬虫（四）：Selenium 框架
# 原创 程序员野客 Python小二 2019-10-14 08:00
# 点击上方“蓝色文字”关注我
#
# 回复“Python”免费领取Python学习资料！
#
# 图片
#
#
#
# 图片
#
# Selenium 是一个用于测试 Web 应用程序的框架，该框架测试直接在浏览器中运行，就像真实用户操作一样。它支持多种平台：Windows、Linux、Mac，支持多种语言：Python、Perl、PHP、C# 等，支持多种浏览器：Chrome、IE、Firefox、Safari 等。
#
# 1 安装
# 1）安装 Selenium
#
# pip install selenium
#
# 2）安装 WebDriver
#
# 主要浏览器 WebDriver 地址如下：
#
# Chrome：http://chromedriver.storage.googleapis.com/index.html
#
# Firefox：https://github.com/mozilla/geckodriver/releases/
#
# IE：http://selenium-release.storage.googleapis.com/index.html
#
# 本文以 Chrome 为例，本机为 Windows 系统，WebDriver 使用版本 78.0.3904.11，Chrome 浏览器版本为 78.0.3880.4 驱动程序下载好后解压，将 chromedriver.exe 放到 Python 安装目录下即可。

#
# import os
# print(os.getcwd()) #这是文件目录，不是安装目录

# 2 操作浏览器
# 2.1 打开浏览器
# 1）普通方式
#
# 以打开去 163 邮箱为例，使用 Chrome 浏览器
#webDriver大版本对了就行，103,104后面的小版本号没对不影响
'''from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://mail.163.com/')
'''
# # 使用 Firefox 浏览器
#
# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('https://mail.163.com/')
# # 使用 IE 浏览器
#
# from selenium import webdriver
#
# browser = webdriver.Ie()
# browser.get('https://mail.163.com/')

# 2）加载配置方式
#
# 以 Chrome 为例，在 Chrome 浏览器地址栏输入 chrome://version/ 打开，如图所示：
#
# 图片
#
# 我们可以看到个人资料路径这一项，取到路径：C:\Users\admin\AppData\Local\Google\Chrome\User Data，取到 User Data 使用自己设置的配置，取到 Default 使用默认配置。看下示例：
'''from selenium import webdriver

option = webdriver.ChromeOptions()
# 自己的数据目录（需要将复制的路径中的 \ 替换成 / 或进行转义 \\）
# option.add_argument('--user-data-dir=C:/Users/admin/AppData/Local/Google/Chrome/User Data')
# option.add_argument('--user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data')
option.add_argument('--user-data-dir=C:\\Users\\zenghc\\AppData\\Local\\Google\\Chrome\\User Data')

browser = webdriver.Chrome(chrome_options=option)
browser.get('https://mail.163.com/')
# 关闭
browser.quit() #可以就是有个警告，，，要退出浏览器后再执行
# 如果执行时报错没有打开指定页面，可先将浏览器关闭再执行。'''

# 3）Headless 方式
#
# 前两种方式都是有浏览器界面的方式，Headless 模式是 Chrome 浏览器的无界面形态，可以在不打开浏览器的前提下，使用所有 Chrome 支持的特性运行我们的程序。这种方式更加方便测试 Web 应用、获得网站的截图、做爬虫抓取信息等。看下示例：
'''
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# 使用 headless 无界面浏览器模式
chrome_options.add_argument('--headless')
# 禁用 gpu 加速
chrome_options.add_argument('--disable-gpu')

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://mail.163.com/'
browser.get(url)
print('browser text = ',browser.page_source)
browser.quit()
'''
# 2.2 设置浏览器窗口
# 最大化显示
#
# browser.maximize_window()
# 最小化显示
#
# browser.minimize_window()
# 自定义大小
#
# # 宽 500，高 800
# browser.set_window_size(500,800)
# 2.3 前进后退
# 前进
#
# browser.forward()
# 后退
#
# browser.back()
# 3 元素定位
# 当我们想要操作一个元素时，首先需要找到它，Selenium 提供了多种元素定位方式，
# 我们以 Chrome 浏览器 Headless 方式为例。看下示例：


# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# url = 'https://xxx.xxx.com/'
# browser.get(url)
# data = browser.page_source
# 假设访问地址 https://xxx.xxx.com/，返回 data 为如下内容。
#
# <html>
#  <body>
#   <form>
#    <input id="fid" name="fid" type="text" />
#    <input id="firstName" name="fname" class="fname" type="text" />
#    <input id="lastName" name="fname" class="fname" type="text" />
#    <a href="index.html">index</a>
#   </form>
#  </body>
# <html>
# 1）根据 id 定位
#
# browser.find_element_by_id('fid')
# 2）根据 name 定位
#
# # 返回第一个元素
# browser.find_element_by_name('fname')
# # 返回所有元素
# browser.find_elements_by_name('fname')
# 3）根据 class 定位
#
# # 返回第一个元素
# browser.find_element_by_class_name('fname')
# # 返回所有元素
# browser.find_elements_by_class_name('fname')
# 4）根据标签名定位
#
# # 返回第一个元素
# browser.find_element_by_tag_name('input')
# # 返回所有元素
# browser.find_elements_by_tag_name('input')
# 5）使用 CSS 定位
#
# # 返回第一个元素
# browser.find_element_by_css_selector('.fname')
# # 返回所有元素
# browser.find_elements_by_css_selector('.fname')

# 6）使用链接文本定位超链接
#
# # 返回第一个元素
# browser.find_element_by_link_text('index')
# # 返回所有元素
# browser.find_elements_by_link_text('index')
#
# # 返回第一个元素
# browser.find_element_by_partial_link_text('index')
# # 返回所有元素
# browser.find_elements_by_partial_link_text('index')
# 7）使用 xpath 定位
#
# # 返回第一个元素
# browser.find_elements_by_xpath("//input[@id='fid']")
# # 返回所有元素
# browser.find_elements_by_xpath("//input[@name='fname']")

# 4 等待事件
# Web 应用大多都使用 AJAX 技术进行加载，浏览器载入一个页面时，页面内的元素可能会在不同的时间载入，这会加大定位元素的困难程度，因为元素不在 DOM 里，会抛出 ElementNotVisibleException 异常，使用 Waits，我们就可以解决这个问题。
#
# Selenium WebDriver 提供了显式和隐式两种 Waits 方式，显式的 Waits 会让 WebDriver 在更深一步的执行前等待一个确定的条件触发，隐式的 Waits 则会让 WebDriver 试图定位元素的时候对 DOM 进行指定次数的轮询。
# __init__(driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
#
# driver: 传入 WebDriver 实例；
#
# timeout: 超时时间，单位为秒；
#
# poll_frequency: 调用 until 或 until_not 中方法的间隔时间，默认是 0.5 秒；
#
# ignored_exceptions: 忽略的异常，如果在调用 until 或 until_not 的过程中抛出这个元组中的异常，则不中断代码，继续等待，如果抛出的是这个元组外的异常，则中断代码，抛出异常。默认只有 NoSuchElementException。
#
# until(method, message='')
#
# method: 在等待期间，每隔一段时间（init 中的 poll_frequency）调用这个方法，直到返回值不是 False；
#
# message: 如果超时，抛出 TimeoutException，将 message 传入异常。
#
# until_not(method, message='')
#
# until 方法是当某条件成立则继续执行，until_not 方法与之相反，它是当某条件不成立则继续执行，参数与 until 方法相同。
#
# 以去 163 邮箱为例，看一下示例：

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://mail.163.com/')
try:
    # 超时时间为 5 秒
    data = WebDriverWait(browser,5).until(
        EC.presence_of_element_located((By.ID,'lbNormal'))
    )
    print(data)
finally:
    browser.quit()
'''
# 示例中代码会等待 5 秒，如果 5 秒内找到元素则立即返回，否则会抛出 TimeoutException 异常，WebDriverWait
# 默认每 0.5 秒调用一下 ExpectedCondition 直到它返回成功为止。

# 4.2 隐式等待
# 当我们要找一个或者一些不能立即可用的元素的时候，隐式 Waits 会告诉 WebDriver 轮询 DOM 指定的次数，默认设置是 0 次，一旦设定，WebDriver 对象实例的整个生命周期的隐式调用也就设定好了。看一下方法：
#
# implicitly_wait(time_to_wait)
#
# 隐式等待是设置了一个最长等待时间 time_to_wait，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步。看到了这里，我们会感觉有点像 time.sleep()，它们的区别是：time.sleep() 必须等待指定时间后才能继续执行， time_to_wait 是在指定的时间范围加载完成即执行，time_to_wait 比 time.sleep() 更灵活一些。
#
# 看下示例：
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://mail.163.com/')
# data = browser.find_element_by_id('lbNormal')##这个方法艺报错了
data = browser.find_element(by=By.ID,value='lbNormal')#用这种
print(data)
browser.quit()'''

# 5 登录 163 邮箱
# 最后，我们用 Selenium 来做个登录 163 邮箱的实战例子。
#
# 5.1 方式一
# 我们通过地址 https://email2.163.com/ 登录，如图所示：
#
# 图片
#
# 从图中我们发现直接进了 163 邮箱用户名、密码登录页，我们直接输入用户名、密码，点击登录按钮即可。示例如下：

#这可以
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://email2.163.com/')
# browser.switch_to.frame(browser.find_element_by_xpath('//iframe[starts-with(@id,"x-URS")]'))
# browser.switch_to.frame(browser.find_element(by=By.XPATH,value='//iframe[starts-with(@id,"x-URS")]'))
# browser.switch_to.frame(browser.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/iframe'))#我为什么是copy full xpath才行？？
browser.switch_to.frame(browser.find_element(by=By.XPATH,value='//iframe[starts-with(@id,"x-URS")]'))


browser.implicitly_wait(2)
# 自己的用户名
# browser.find_element_by_xpath('//input[@name="email"]').send_keys('chur_z')
browser.find_element(by=By.XPATH,value='//input[@name="email"]').send_keys('chur_z')
# 自己的密码
# browser.find_element_by_xpath('//input[@name="password"]').send_keys('z118476')
browser.find_element(by=By.XPATH,value='//input[@name="password"]').send_keys('z118476')
# browser.find_element_by_xpath('//*[@id="dologin"]').click()
browser.find_element(by=By.XPATH, value='//*[@id="dologin"]').click()
browser.implicitly_wait(2)
print(browser.page_source)
browser.implicitly_wait(2)
# 关闭
time.sleep(6)
browser.quit()