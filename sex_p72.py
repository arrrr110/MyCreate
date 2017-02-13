# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql


#warnings.simplefilter('ignore')
conn = pymysql.connect(
    host='localhost',
    #unix_socket='/tmp/mysql.sock',
    user='root',
    passwd='password',
    db='mysql',
    charset='utf8mb4'
)
cur = conn.cursor()
cur.execute("USE python")

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute(
        "INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")",
        (title, content)
            )
    cur.connection.commit()

def getLinks(articleUrl):
    html = ("http://en.wikipedia.org" + articleUrl)
   # bsObj = BeautifulSoup(html, "html.parser")
    bsObj = BeautifulSoup(urlopen(html), "html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find('p').get_text()
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/kevin_Bacon")

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()