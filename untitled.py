#-*- coding utf-8 -*-
import string
import urllib2


def baidu_tieba(url, beginpage, endpage):
    for page in range(beginpage, endpage + 1):
        sName = string.zfill(page, 4) + ".html"
        print "start download page" + str(page) + " to :" + sName
        response = urllib2.urlopen(url + str((page - 1) * 50))
        f = open(sName, "w+")
        f.write(response.read())
        f.close()

url = str(raw_input("type the url of the tiebar\n"))
beginpage = int(raw_input("input the beginpage\n"))
endpage = int(raw_input("input the endpage\n"))
baidu_tieba(url, beginpage, endpage)
