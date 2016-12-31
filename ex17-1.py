#!/usr/bin/env python3

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ('Go?')
input('>')
#一行代码搞定ex17，失败
to_file.write(from_file.read(),'w')
