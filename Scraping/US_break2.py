
import os
import sys
import lxml.html
import requests
import csv
import datetime


if len(sys.argv) > 1:
    loopCount = sys.argv[1]
else:
    loopCount = 1

pageNum, i, j = 0, 0, 0


print("Script Starts")


date = datetime.datetime.today().strftime("%Y%m%d")
while pageNum< int(loopCount):
    pageNum += 1
    url = 'https://edition.cnn.com/world'
    source = requests.get(url)

    tree = liml.html.formstring(source.content)

# ========================================
# >>>   Get HTMLElements ByXPath
# ========================================
xpath_spans = "//section[@class='zn zn-world-zone-7 zn-balanced zn--idx-6 zn--ordinary t-light zn-has-one-container']//div[@class='l-container zn__background--content-relative']//div[@class='zn__containers']//div[@class='cd__content']//span[@class='cd__headline-text']"

xpath_links = xpath_spans + "/parent::a"

links = tree.xpath(xpath_links)

basename = os.path.basename(__file__).split('.')[0]
path_folder = os.path.dirname(os.path.realpath_file__))
path_csv = path_folder + "==" + basename + ".csv"
for index, link in enumerate(links):
    j += 1
    if j ==1 :
        OPTION = 'w'
    else:
        OPTION = 'a'
    
    with openpath_csv, OPTION, newline='') as csvfile:
        f = csv.writer(csvfile, delimiter=',')
        if j == 1:
            # ==================
            # >>>   Header
            # ==================
            f.writerow(["","","","",""])

        xpath_summary = "(" + xpath_links + ")[" + str(index+1) + "]" + "/span"

        summary = tree.xpath(xpath_summary)
        