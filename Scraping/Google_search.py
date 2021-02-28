


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
# from lxml.html import unicode



# if len(sys.argv) > 1:
    # loopCount = sys.argv[1]
# else:
loopCount = 1

# while (1):
pageNum, i, j = 0, 0, 0 
print("Script Starts")

date = datetime.datetime.today().strftime("%Y%m%d")
# print("loopCount : " + loopCount)
keyword = "Google+Search+Query"
while pageNum < int(loopCount):
    pageNum += 1
    url  = 'https://www.google.com/search?q=' + keyword
    source = requests.get(url)

    tree = lxml.html.fromstring(source.content)

    # ===================================
    # >>>   Get HTMLElements ByXpath
    # ===================================
    xpath_links = "//div[contains(@class, 'list_body')]//ul[contains(@class, 'headline')]//dt[not(@class)]/a[1]"
    xpath_h3 = "//*[@class='BNeawe vvjwJb AP7Wnd']"
    xpath_summary = "//div[@class='BNeawe s3v9rd AP7Wnd' and not(text())]"
    xpath_summary = "//div[@class='BNeawe s3v9rd AP7Wnd']"


    h3s = tree.xpath(xpath_h3)
    summaries = tree.xpath(xpath_summary)

    for index, h3 in enumerate(h3s):
        print(str(index) + " | " +  h3.text)

    for index, summary in enumerate(summaries):
        # print(str(index) + " | " + summary[0].text)
        try:
            print(summary[0].text)
        except Exception:
            pass
    
    # basename = os.path.basename(__file__).split('.')[0]
    # path_folder = os.path.dirname(os.path.realpath(__file__))
    # path_csv = path_folder + "\\" + basename + ".csv" 


    # for index, h3 in enumerate(h3s):
    #     j += 1
    #     if j == 1 :
    #         OPTION = 'w'
    #     else:
    #         OPTION = 'a'
        
    #     # with open(path_csv, OPTION, newline='', encoding='utf-8', ) as csvfile:
    #     # with open(path_csv, OPTION, newline='', encoding='cp949', errors='ignore') as csvfile:
    #     with open(path_csv, OPTION, newline='', encoding='cp949', errors='replace') as csvfile:
    #     # with open(path_csv, OPTION, newline='', encoding='cp949') as csvfile:
    #         f = csv.writer(csvfile, delimiter=',')
    #         if j == 1:
    #             # ==================
    #             # >>>   Header
    #             # ==================
    #             f.writerow(["index", "title", "temp", "time", "summary", "link"])

    #         xpath_summary = "(" + xpath_links + ")[" + str(index + 1)+ "]" + "/parent::dt/following-sibling::dd//span[@class='lede']"
    #         xpath_time = "(" + xpath_links + ")[" + str(index + 1)+ "]" + "/parent::dt/following-sibling::dd//span[@class='date is_new' or @class='date is_outdated']"

    #         # date is_outdated
            
    
    #         summary = tree.xpath(xpath_summary)
    #         time = tree.xpath(xpath_time)

    #         # print(unicode.encode('utf-8'))            
    #         # print(link.text.encode('utf-8'))
    #         # f.writerow([j, link.text.strip(), summary[0].text.strip(), time[0].text.strip()] )
    #         try:
    #             f.writerow([j, '', link.text.strip(), time[0].text.strip(), summary[0].text.strip(), link.attrib['href']] )
    #             # f.writerow([j, link.text.strip().encode('utf-8'), summary[0].text.strip().encode('utf-8'), time[0].text.strip().encode('utf-8')] )
    #         except Exception as e:
    #             print(e)
    #             pass

    #         # try:
    #         #     f.writerow([j, link.text.strip(), summary[0].text.strip(), time[0].text.strip()] )
    #         # except Exception:
    #         #     print(str(j) + ", " + str(index))
    # print(pageNum)
            




