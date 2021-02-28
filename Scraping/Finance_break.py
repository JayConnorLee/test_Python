

import os
import sys
import lxml.html
import urllib3
import requests
import csv



loopCount, pageNum, i, j = 4, 0, 0, 0 
print("Script Starts")
while pageNum < loopCount:
    pageNum += 1
    url  = 'https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258&page=' + str(pageNum)
    source = requests.get(url)
    # tree = lxml.html.fromstring(source.content.decode('euc-kr', 'replace'))
    tree = lxml.html.fromstring(source.content.decode('euc-kr'))
    # tree = lxml.html.fromstring(source.content.decode('utf-8', 'ignore'))


    xpath_links = "//li[contains(@class, 'newsList')]//dd[@class='articleSubject']/a"
    xpath_summaries = "//li[@class='newsList top']//dd[@class='articleSummary']"

    links = tree.xpath(xpath_links)
    summaries = tree.xpath(xpath_summaries)
    times = tree.xpath("//li[contains(@class, 'newsList')]//dd[@class='articleSummary']/span[@class='wdate']")

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
            # f = csv.writer(csvfile, delimiter =',',quotechar ='|',quoting=csv.QUOTE_MINIMAL)
            f = csv.writer(csvfile, delimiter=',')
            if j == 1:
                # ==================
                # >>>   Header
                # ==================
                # f.writerow(["index", "time", "title", "summary"])
                f.writerow(["index", "time", "title", "summary"])

            xpath_summary = "(//li[contains(@class, 'newsList')]//dd[@class='articleSubject']/a[1])[" + str(index + 1) + "]/parent::dd/following-sibling::dd[1]"
            xpath_time = xpath_summary + "/span[@class='wdate']"
            summary = tree.xpath(xpath_summary)
            time = tree.xpath(xpath_time)

     
            f.writerow([j, link.text, summary[0].text.strip(), time[0].text.strip() + "1"] )
    print(pageNum)
            
    

