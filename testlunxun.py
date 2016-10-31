# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


print(DesiredCapabilities.CHROME)
lists = ['chrome','firefox','internet explorer']
for browser in lists:
    driver = webdriver.Remote(
        command_executor= 'http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': browser,
                              'javascriptEnabled': 'true'})
    first_url = 'http://117.135.196.139:13000/NetMaintain/login'
    print ("now access %s" % (first_url))
    driver.get(first_url)
    print(driver.title)
    # print ("设置浏览器宽800、高600显示")
    driver.set_window_size(800,600)  # 参数数字为像素点
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('password_').clear()
    driver.find_element_by_id('username').send_keys('xitong')
    driver.find_element_by_id('password_').send_keys('123456')
    driver.find_element_by_class_name("loginbox-submit").submit()
    time.sleep(2)
    print(driver.title)
    #检查cookie有效时间
    driver.back()
    time.sleep(1)
    driver.forward()
    time.sleep(5)
    driver.quit()













# def getconfig():
#     info={'http://127.0.0.1:4444/wd/hub':'firefox',
#            'http://127.0.0.1:5555/wd/hub':'chrome',}
#     print ("success read host and browser!!")
#     return info
#
# for host,browser in getconfig().items():
#     driver = webdriver.Remote(
#         command_executor= host,
#         desired_capabilities={'platfrom': 'ANY', 'browserName': browser, 'version': '',
#                               'javascriptenabled': True})
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw1").clear()
#     driver.find_element_by_id("kw1").send_keys("selenium grid")
#     driver.find_element_by_id("sul").click()
#     driver.quit()

# 判断名字输入是否符合要求并返回会话
# from pip._vendor.distlib.compat import raw_input
# name = raw_input('What is your name?')
# if name.endswith('tank'):
#     print ('hello tank!')
# elif name.endswith('xiao'):
#     print ('hello xiao!')
# else:
#     print ('hello strange!')