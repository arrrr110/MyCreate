#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import csv
import codecs
with open('C://Users//aorui//Desktop//result-2.csv', 'wb') as csvfile:
    csvfile.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['测试'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])