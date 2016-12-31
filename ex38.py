#! /usr/bin/env python3

ten_things = "Apples Oranges Crows Telephone Light Suger"

print ("Wait there's not 10 things in that list, Let's fix that.")

stuff = ten_things.split(' ')#split(' ', ten_things)
#split the str with ' '. Also can .split('.',1) 'www.baidu.com' into 'www' 'baidu.com'
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()#pop(more_stuff(-1))
    print ("Adding:", next_one)
    stuff.append(next_one)#append(next_one, stuff)
    print ("There's %d item now." % len(stuff))

print ("There we go:",stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1])
print (stuff.pop())#pop(stuff(-1))
print (' '.join(stuff))#make the items gethering into str
print ('#'.join(stuff[3:8]))#join('#',stuff[3:8])