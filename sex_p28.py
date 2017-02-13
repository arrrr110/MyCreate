from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

#随机种子利用了当前的时间，呈现出一种伪随机
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                    href = re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

#这是一个简单地构建一个从一个页面到另外一个页面的爬虫，在wiki页面中不断的随机跳转