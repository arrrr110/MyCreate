from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html5lib")
#处理子标签和后代标签,下面这个是子标签，后代标签是descendants()
#for child in bsObj.find("table", {'id':'giftList'}).children:
    #print(child)
    #pass
#处理兄弟标签
#for sibling in bsObj.find("table", {'id':'giftList'}).tr.next_siblings:
    #print(sibling)
#父标签处理
print(bsObj.find('img',{'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
#print(bsObj.attrs)
