# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:56:46 2020

@author: www69
"""
from selenium import webdriver
import time
#browser=webdriver.Chrome(executable_path='c:\Program Files (x86)\Google\Chrome\Application\chromedriver')
browser=webdriver.PhantomJS()
with open("d:/info.txt",mode="r") as file:
    info=file.readlines()
username=info[0].strip("\n")
password=info[1].strip("\n")
website=info[2].strip("\n")
browser.get(website)
uinput=browser.find_element_by_id('username')
pinput=browser.find_element_by_id('password')
login=browser.find_element_by_tag_name('button')
uinput.send_keys(username)
pinput.send_keys(password)
login.click()
time.sleep(10)
new=browser.find_element_by_xpath('/html/body/main/article/section/div[2]/div[1]')
new.click()
time.sleep(10)
save=browser.find_element_by_xpath('/html/body/div[11]/div/div[2]/footer/div')
save.click()
time.sleep(1)
try:
    save.click()
except Exception:
    pass
else: 
    pass
time.sleep(5)
confirm=browser.find_element_by_xpath('/html/body/div[55]/div[1]/div[1]/div[2]/div[2]/a[1]')
confirm.click()
time.sleep(1)
try:
    confirm.click()
except Exception:
    pass
else: 
    pass
print('succeeded')
