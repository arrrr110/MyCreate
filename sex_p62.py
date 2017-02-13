from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

#html = urlopen("HTTP://www.pythonscraping.com/")
#bsObj = BeautifulSoup(html, 'html.parser')
#imageLocation = bsObj.find("a",{"id": "logo"}).find("img")["src"]
#urlretrieve(imageLocation, "logo.jpg")

#--------第二个脚本

import os
import re

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://"+source[4:]
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    #实际文件是有小尾巴？ v = 1.4.4 的，因此要用正则表达式替换
    path = re.sub("\?.*", "", path)#把问号开头的字符串都替换为空
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

html = urlopen("HTTP://www.pythonscraping.com/")
bsObj = BeautifulSoup(html, 'html.parser')
downloadList = bsObj.findAll(src = True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))