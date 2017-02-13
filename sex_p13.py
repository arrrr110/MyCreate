from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html5lib")
nameList = bsObj.findAll("span", {"class":"green"})
nameNum = bsObj.findAll(text = 'the prince')
allText = bsObj.findAll(id = 'text')
allWords = bsObj.findAll(text = 'with')
for name in nameList:
    #pass
    print(name.get_text())
#print(len(nameNum))
#print(allText[0].get_text())
#print(len(allWords))