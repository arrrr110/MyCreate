from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    try:
        print(bsObj.h1.get_text())
        #以下代码会出现错误，暂时搁置
        #print(bsObj.find(id = 'mw-content-text').findAll('p')[0])
        print(bsObj.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("页面缺少一些属性，不过不用担心")

    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                #我们遇到了新页面
                newPage = link.attrs["href"]
                print("-----------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")
