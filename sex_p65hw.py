import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ftchinese.com/channel/2016highlight.html")
bsObj = BeautifulSoup(html, "html.parser")

headlines = bsObj.findAll("div",{"class":"items"})[0]
rows = headlines.findAll("h2")

csvFile = open("C:/Users/aorui/Documents/aorick/my word/datafiles/fthl.csv", "wt", newline="", encoding=None)
writer = csv.writer(csvFile)

try:
    for row in rows:
        writer.writerow(row)#.get_text())
        #遇到问题：.get_text()之后，汉字分离
        #csvRow = []
        #for cell in row.findAll(['h2']):
            #csvRow.append(cell.get_text())
        #writer.writerow(csvRow)
finally:
    csvFile.close()