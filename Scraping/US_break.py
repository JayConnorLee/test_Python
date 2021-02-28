


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



if len(sys.argv) > 1:
    loopCount = sys.argv[1]
else:
    loopCount = 1

# while (1):
pageNum, i, j = 0, 0, 0 
print("Script Starts")

date = datetime.datetime.today().strftime("%Y%m%d")
# print("loopCount : " + loopCount)
while pageNum < int(loopCount):
    pageNum += 1
    #url  = 'https://edition.cnn.com/world' + str(date) + '&page=' + str(pageNum)
    url  = 'https://edition.cnn.com/world'
    source = requests.get(url)

    tree = lxml.html.fromstring(source.content)

    # ===================================
    # >>>   Get HTMLElements ByXpath
    # ===================================
    xpath_spans = "//section[@class='zn zn-world-zone-7 zn-balanced zn--idx-6 zn--ordinary t-light zn-has-one-container']//div[@class='l-container zn__background--content-relative']//div[@class='zn__containers']//div[@class='cd__content']//span[@class='cd__headline-text']"

    xpath_links = xpath_spans + "/parent::a"


    links = tree.xpath(xpath_links)

    basename = os.path.basename(__file__).split('.')[0]
    path_folder = os.path.dirname(os.path.realpath(__file__))
    path_csv = path_folder + "\\" + basename + ".csv" 
    for index, link in enumerate(links):
        j += 1
        if j == 1 :
            OPTION = 'w'
        else:
            OPTION = 'a'
        
        
        with open(path_csv, OPTION, newline='') as csvfile:
            f = csv.writer(csvfile, delimiter=',')
            if j == 1:
                # ==================
                # >>>   Header
                # ==================
                f.writerow(["index", "title", "temp", "time", "summary", "link"])

            # xpath_summary = "(" + xpath_links + ")[" + str(index + 1)+ "]" + "/parent::dt/following-sibling::dd//span[@class='lede']"
            xpath_summary = "(" + xpath_links + ")[" + str(index + 1)+ "]" + "/span"

            #xpath_time = "(" + xpath_links + ")[" + str(index + 1)+ "]" + "/parent::dt/following-sibling::dd//span[@class='date is_new' or @class='date is_outdated']"

            # date is_outdated
            

            summary = tree.xpath(xpath_summary)
            #time = tree.xpath(xpath_time)

            # print(unicode.encode('utf-8'))            
            # print(link.text.encode('utf-8'))
            # f.writerow([j, link.text.strip(), summary[0].text.strip(), time[0].text.strip()] )

            # f.writerow([j, link.text.strip(), summary[0].text.strip(), link.attrib['href']])    
            f.writerow([j, summary[0].text.strip(), 'https://edition.cnn.com/' + link.attrib['href']])


            # try:
            #     f.writerow([j, '', link.text.strip(), time[0].text.strip(), summary[0].text.strip(), link.attrib['href']] )
            #     # f.writerow([j, link.text.strip().encode('utf-8'), summary[0].text.strip().encode('utf-8'), time[0].text.strip().encode('utf-8')] )
            # except Exception as e:
            #     print(e)
            #     pass

            # try:
            #     f.writerow([j, link.text.strip(), summary[0].text.strip(), time[0].text.strip()] )
            # except Exception:
            #     print(str(j) + ", " + str(index))
    print(pageNum)
            




