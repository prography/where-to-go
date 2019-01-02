# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.request import urlopen
from selenium import webdriver
import time
import re
import pandas as pd
import openpyxl

# ???? + ???? ?? + ???? ?? + ??(? ?? ? 100? ????, ????? 3??)
# ???? 1: ???? ??? ?? ??/??/??

driver = webdriver.Chrome(executable_path='C:/Program Files/Microsoft VS Code/myproject/FinalChatbot/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.earthtory.com/ko/area")
time.sleep(1)

country_list=[]
# ??? 
for i in range(1,21):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[3]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)
        print("asia",i)
# ??
for i in range(1,30):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[5]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)
        print("eu",i)
# ????
for i in range(1,8):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[7]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)
        print("oc",i)
# ??
for i in range(1,3):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)
        print("na",i)
# ???
for i in range(1,12):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[11]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)
        print("na",i)
        
print(country_list)
df = pd.DataFrame(country_list,columns=["country"])
df.to_excel("./crawling_data1.xlsx")





