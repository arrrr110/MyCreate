#!/usr/bin/env python3
print("Hello World!")
print("this is a test git commit")

import shelve
a = 0
data = shelve.open('data')


while a<3:
    c = 0

    b = input("B >")
    if a==int(b):
        
        print ("a=",a)
    else:
        pass