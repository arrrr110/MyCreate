import codecs

with codecs.open('C://Users//aorui//Desktop//result-2.csv','r','gb2312') as csvfile:

    for line in csvfile:

        print(line.encode('utf8'))