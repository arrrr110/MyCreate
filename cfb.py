#!/usr/bin/env python3
x = 1
print("~"*50)
while x < 10:
    for y in range(1, 10):
        if y <= x:
            print("%d * %d = %d    "  % (x, y, x*y), end = '' )
            #print("{} * {} = {}   ".format(x, y, x*y), end = '')
    x += 1
    print()
print("~"*50)