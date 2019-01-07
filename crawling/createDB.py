# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.request import urlopen
from selenium import webdriver
import os
import time
import re
import pandas as pd
import openpyxl
import csv
import platform


if "Ubuntu" in platform.platform():
    driver = webdriver.Chrome('./chromedriver')
else:
    driver = webdriver.Chrome(executable_path='C:/Program Files/Microsoft VS Code/myproject/FinalChatbot/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.earthtory.com/ko/area")
time.sleep(1)

country_list=[]

for i in range(1,21):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[3]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)


for i in range(1,30):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[5]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)


for i in range(1,8):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[7]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)


for i in range(1,3):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)


for i in range(1,12):
        country = driver.find_element_by_xpath("/html/body/div[7]/div/div[11]/a[%i]"%i).text
        a = re.findall(r'[a-zA-Z]', country)
        b = ''.join(a)
        country_list.append(b)



url_all={}
for enum,country in enumerate(country_list):
    for iter in range(1,11):
        try:
            url_lst_sub=[]
            driver.implicitly_wait(10)
            driver.get("https://www.earthtory.com/ko/area/{}/attraction#{}".format(country,iter))
            time.sleep(3)


            for i in range(1,12):
                try:
                    landmark_name = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[1]/div[2]/div[%i]/div[1]/a"%i).text
                    landmark_url = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[1]/div[2]/div[%i]/a"%i).get_attribute("href")
                    url_lst_sub.append((landmark_name,landmark_url))
                except Exception as e:
                    break
            url_all[country]=url_lst_sub

        except:
            break


with open('landmark_db.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['id','landmark_name', 'country'])
    index=0
    for country,landmark_list in url_all.items():
        for (landmark_name, landmark_url) in landmark_list:
            csv_writer.writerow([index,landmark_name, country])
            index+=1

try:
    os.mkdir("landmark")
except:
    pass

with open('image_db.csv', 'w', newline='') as csv_file2:
    csv_writer2 = csv.writer(csv_file2)
    csv_writer2.writerow(['landmark_name', 'image_url'])

    for country,landmark_list in url_all.items():
        for (landmark_name, landmark_url) in landmark_list:
            try:
                driver.get(landmark_url)
                time.sleep(1)



                src = []
                url1 = driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[1]/img')
                src.append(url1.get_attribute('src'))
                url2 = driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[2]/img')
                src.append(url2.get_attribute('src'))
                url3 = driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[3]/img')
                src.append(url3.get_attribute('src'))
                try:
                    os.mkdir("landmark/{}".format(landmark_name))
                except:
                    pass

                img_path = "landmark/{}/".format(landmark_name)

                for i in range(0,3):
                    if src[i] == "https://www.earthtory.com/res/img/city/spot_info/spot_photo_add.gif":
                        continue

                    try:
                        urllib.request.urlretrieve(src[i], img_path+str(i+1)+".jpg")

                        img_url='landmark/{}/{}'.format(landmark_name,i)
                        row=[landmark_name, img_url]
                        csv_writer2.writerow(row)

                    except:
                        pass
            except:
                pass
