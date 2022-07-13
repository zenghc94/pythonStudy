from selenium import webdriver

option = webdriver.ChromeOptions()
# 自己的数据目录（需要将复制的路径中的 \ 替换成 / 或进行转义 \\）
# option.add_argument('--user-data-dir=C:/Users/admin/AppData/Local/Google/Chrome/User Data')
# option.add_argument('--user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data')
option.add_argument('--user-data-dir=C:\\Users\\zenghc\\AppData\\Local\\Google\\Chrome\\User Data')

browser = webdriver.Chrome(chrome_options=option)
browser.get('https://mail.163.com/')
# 关闭
browser.quit()