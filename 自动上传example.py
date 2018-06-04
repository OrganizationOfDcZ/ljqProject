# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
import win32gui
import win32con
import time

chrome = webdriver.Chrome(r'E:\chromedriver.exe')
chrome.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = chrome.find_element_by_id('file')
upload.click()
#等待上传框打开
time.sleep(1)

# win32gui
#找到windows对话框，参数是（className，title）,注意title并修改
dialog = win32gui.FindWindow('#32770', u'打开')                       
#下面三句依次寻找对象，直到找到输入框Edit对象的句柄                             
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None) 
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
#确定按钮Button
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  

#往输入框输入绝对地址
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'E:\123.txt')
#按button  
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  
#等待上传完成
time.sleep(5)

print(upload.get_attribute('value'))
chrome.quit()
