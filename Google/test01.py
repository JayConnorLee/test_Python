
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
keyword = "Naver"
while pageNum < int(loopCount):
    pageNum += 1
    url  = 'https://www.google.com/search?q=' + keyword
    #url  = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=test'
    url  = 'https://www.google.com/search?q=%EA%B0%80%EA%B0%88%EA%B0%B1&rlz=1C1CHBF_enKR884KR884&hl=en&sxsrf=ALeKk01iR9abDtkTDsGwbJk0g_zzdVzq2w:1593259772628&ei=_Db3XvjzJdCC-QbOwr24Bg&start=0&sa=N&ved=2ahUKEwj44aCW-6HqAhVQQd4KHU5hD2c4FBDy0wN6BAgWECs&biw=1396&bih=620&dpr=1.38'
    source = requests.get(url)

    tree = lxml.html.fromstring(source.content)

    # ===================================
    # >>>   Get HTMLElements ByXpath
    # ===================================
    xpath_links = "//div[@class='g']//a[./h3]"
    xpath_h3 = "//div[@class='g']//h3"
    xpath_h3 = "//h3"
    xpath_summary = "//div[@class='g'][.//h3]//div[@class='s']//span[@class='st']"

    
    h3s = tree.xpath(xpath_h3)
    summaries = tree.xpath(xpath_summary)


    divs = tree.xpath("//div")
    # divs = tree.xpath("//div[@class='BNeawe s3v9rd AP7Wnd']")

    # for index, d in enumerate(divs):
    #     try:
    #         print(str(index) + " | " + d.attrib['class'])
    #     except Exception:
    #         pass

    # # for index, h in enumerate(h3s):
    #     try:
    #         if (d.text != None ):
    #             sprint(str(index) + " | " + d.text)
    #     except:
    #         pass




    # for index, h in enumerate(h3s):
    #     print(str(index) + " | " + str(h.text))

    # for index, d in enumerate(divs):
    #     try:
    #         print(str(index) + " | " + str(d.text))
    #     except:
    #         pass

    # for index, summary in enumerate(summaries):
    #     # print(str(index) + " | " + summary[0].text)
    #     try:
    #         print(summary[0].text)
    #     except Exception:
    #         pass
    
    for ix, d in enumerate(divs):
        try:
            if (d.text != None):
                print(d.text)
        except:
            pass