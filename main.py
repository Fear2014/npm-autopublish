# encoding=utf8
import os
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import urllib.request as r
from bs4 import BeautifulSoup
from xlutils.copy import copy
import re
import importlib
import sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#
def weburl(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置useragent
    dcap['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ')  # 根据需要设置具体的浏览器信息
    driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=false'])  # 封装浏览器信息
    # 设定页面加载限制时间,以获取动态加载数据
    driver.set_page_load_timeout(3)
    script = "phantom.setProxy('{ip}', {port})".format(ip='119.39.238.34', port='9999')
    try:
        # 设置代理
        driver.get(url)
    except:
        pass
    return driver.page_source


#调用IP设置函数
#自定义npm地址
url = 'http://www.npm.com:4873/-/verdaccio/packages'

data = weburl(url)
soup=BeautifulSoup(data,'html.parser')
for area1_title in soup:
    #print (str(area1_title))
    for area1_title in re.findall('"name": "clc.*?"',str(soup),flags=0):
        print(str(area1_title).replace('"name": "','').replace('"',''))
        package=str(area1_title).replace('"name": "','').replace('"','')
        os.system("npm_test.bat "+ package)


