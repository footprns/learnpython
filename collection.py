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
range(5)
for i in range(5):
    print(i)
range(5, 10) # with starting point
for i in range(5, 10):
    print(i)
print(list(range(5, 10)))
print(list(range(0, 10, 2))) # skip counting

s = [0, 1, 4, 6, 13]
for v in s:
    print(v)

t = [5, 372, 8862, 148800]
for p in enumerate(t):      # use enumerate() for counter
    print(p)

for i, v in enumerate(t):    # use tuple unpacking
    print("i = {}, v = {}".format(i, v)) 

# LIST --> mutable
s = "show how to index into sequences".split()
print(s)
print(s[4])
print(s[-2])
print(s[1:4]) # slicing...
print(s[1:-1])
print(s[3:]) # until the end
print(s[:3])
full_slice = s[:] # important to copy list
print(full_slice)
u = s.copy() # to copy list
print(u)
v = list(s) # copyt list
print(v)

c = [21, 37]
d = c * 4
print(d)

w = "the quick brown fox jumps over the lazy dog".split()
i = w.index('fox') # finding element
print(i)
print(w[i])

# i = w.index('unicorn')
print(w.count('the'))# how many matching number
# membership and non membership
print(37 in [1, 37, 76])
print(37 not in [1, 37, 76])

# delete index element
u = "jackdaws love my big sphinx of quartz".split()
print(u)
del u[3]
print(u)
u.remove('jackdaws')
print(u)
del u[u.index('quartz')]
print(u)
# u.remove('pyramid') # error
a = "I accidentally the whole universe".split()
print(a)
a.insert(2, "destroyed")
print(a)
print(' '.join(a))

m = [2, 1, 3]
n = [4, 7, 11]
k = m + n
print(k)
k += [18, 29, 47]
print(k)
k.extend([76, 129, 199])
print(k)

# reverse and sorting list
g = [1, 11, 21, 1211, 1121111]
g.reverse()
print(g)
g.sort()
print(g)
g.sort(reverse=True)
print(g)

h = 'not perplexing do handwriting family where I illegiby know doctor'.split()
h.sort(key=len)
print(h)
print(' '.join(h))

x = [4, 9, 2, 21]
y = sorted(x)
print(x)
print(y)

p = [9, 3, 1, 0]
q = reversed(p)
print(list(q))

# Dictionary. Key have to unique in a dictionary
urls = {'Google': 'http://google.com',
        'Pluralsight': 'http://pluralsight.com',
        'Sixty North': 'http://sixtynorth.com'}
print(urls['Pluralsight'])

names_and_ages = [('Alice', 32), ('Bob', 48), ('Charles', 28)]
d = dict(names_and_ages)
print(d)
phonetic = dict(a='alfa', b='bravo', c='charlie')
print(phonetic)

# copy dictionary
d = dict(golden=0xDAA520, indigo=0x4B0082)
print(d)
e = d.copy()
print(e)
f = dict(e)
print(f)

g = dict(wheat=0xF5DEB3, khaki=0xF0E68C)
f.update(g)
print(f)
