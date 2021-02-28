


# pip install lxml
# pip install urllib3
# pip install requests
# 

import os
import sys
import lxml.html
import urllib3
import requests
import csv
import datetime
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()

pathProfile = r'C:\Users\Connor\AppData\Local\Google\Chrome\User Data'

options = webdriver.ChromeOptions() 
options.add_argument("--user-data-dir="+ pathProfile) #Path to your chrome profile
try:
    d= webdriver.Chrome("C:\\Windows\\chromedriver.exe", chrome_options=options)
except:
    print(';;')

sk = 'https://www.jobplanet.co.kr/companies/23717/reviews/%EC%B9%B4%ED%8E%9824'
d.get(sk)

for i in range(1, 100):
    page = d.find_element_by_xpath("//*[@class='txtlink_page' and text()="+ str(i) +"]")
    page.click()
    
    print(i)
    # print(d.current_url)
    d.get(d.current_url)

    basename = os.path.basename(__file__).split('.')[0]
    path_folder = os.path.dirname(os.path.realpath(__file__))
    path_csv = path_folder + "\\" + basename + ".csv" 
    for index, link in enumerate(links):
        j += 1
        if j == 1 :
            OPTION = 'w'
        else:
            OPTION = 'a'
        
        # with open(path_csv, OPTION, newline='', encoding='utf-8', ) as csvfile:
        # with open(path_csv, OPTION, newline='', encoding='cp949', errors='ignore') as csvfile:
        with open(path_csv, OPTION, newline='', encoding='cp949', errors='replace') as csvfile:
        # with open(path_csv, OPTION, newline='', encoding='cp949') as csvfile:
            f = csv.writer(csvfile, delimiter=',')
            if j == 1:
                # ==================
                # >>>   Header
                # ==================
                f.writerow(["index", "title", "temp", "time", "summary", "link"])

            xpath_summary = "(" + xpath_links + ")[" + str(index + 1)+ "]" + "/parent::dt/following-sibling::dd//span[@class='lede']"
            xpath_time = "(" + xpath_links + ")[" + str(index + 1)+ "]" + "/parent::dt/following-sibling::dd//span[@class='date is_new' or @class='date is_outdated']"

            # date is_outdated
            
    
            summary = tree.xpath(xpath_summary)
            time = tree.xpath(xpath_time)

            # print(unicode.encode('utf-8'))            
            # print(link.text.encode('utf-8'))
            # f.writerow([j, link.text.strip(), summary[0].text.strip(), time[0].text.strip()] )
            try:
                f.writerow([j, '', link.text.strip(), time[0].text.strip(), summary[0].text.strip(), link.attrib['href']] )
                # f.writerow([j, link.text.strip().encode('utf-8'), summary[0].text.strip().encode('utf-8'), time[0].text.strip().encode('utf-8')] )
            except Exception as e:
                print(e)
                pass

            # try:
            #     f.writerow([j, link.text.strip(), summary[0].text.strip(), time[0].text.strip()] )
            # except Exception:
            #     print(str(j) + ", " + str(index))
    print(pageNum)
                

# d.close()
