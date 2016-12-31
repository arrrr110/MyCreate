#! /usr/bin/env python3
# --*-- coding: utf-8 --*--
import random
from random import shuffle
from urllib.request import urlopen
#from urllib import urlopen
import sys
import re

PATH = 'C:/Users/aorui/Documents/aorick/my word/opp.txt'
WORD_URL = re.findall('\w+',open(PATH).read().lower())

print (WORD_URL)