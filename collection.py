#!/usr/bin/env python3
# str -- immutable
# list -- mutable
# dict -- immutable key to mutable object
# tupple -- immutable
# range -- list of int
# set -- immutable object

# tuple
t = ("Norway", 4.953, 3)
print(t[0])
print(t[1])
print(len(t))
for item in t:
    print(item)

print(t + (333.0, 2e6))
print(t *3)
print(type(t))

# nested tuple
a = ((220, 284), (1184, 1210), (2620, 2924), (5020, 5564))
print(a[2])
print(a[2][1])

# single tuple
k = (391,)
print(k)
print(type(k))
e = () # empty tuple
print(type(e))

def minmax(items):
    return min(items), max(items)

print(minmax([84,63,96,100]))
# help(min)
# tuple unpacking -- destructure directly into named references
lower, upper = minmax([84,63,96,100])
print(lower)
print(upper)
(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a)
print(b)
print(c)
print(d)
a = 'jelly'
b = 'bean'
a, b = b, a # this is python swap
print(a)
print(b)
tuple([2.61, 1105, 1729, 2465]) # from list to tuple
tuple("Charmichael") # from string to tuple

print(5 in (3, 5, 17))
print(5 not in (3, 5, 17))

# String
print(len("sdfagegersgs"))
print("New" + "Zea" + "land") # concatenation is not preferable. try use join
s = "New"
s += "Zea"
s += "land"
print(s) 

colors = ';'.join(['#45ff23','#45ff25','#45ff21']) # using join
print(colors)
print(colors.split(';'))
road = ''.join(['high', 'way'])
print(road)
# partition become tuple of prefix, separator, suffix
par = "unforgetable".partition("forget")
print(par)

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)

origin, _, destination = "Seattle-Boston".partition('-') # _ not special, but used commonly for dummy value
print(origin)
print(destination)

# format
print("The age of {0} is {1}".format('Jim', 32))
print("Reticulating spline {} of {}".format(4, 23))
output = "Current position {latitude} {longitude}".format(latitude="60N",       longitude="5E")
print(output)

pos = (65.2, 23.1, 82.2)
output = "Galactic position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos)
print(output)

import math
output = "Math constants: pi={m.pi}, e={m.e}".format(m=math)
print(output)
output = "Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math) # 3 decimal
print(output)

# Range