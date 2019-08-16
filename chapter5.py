#!/usr/bin/env python3

#  id is to check the id of object
a = 1000
print(id(a))
b = 1729
print(id(b))

a = 5
b = 5
print(a == b)
print(a is b)

m = [9, 15, 24]
def modify(k):
    k.append(39)
    print("k =", k)

modify(m)

f = [14, 23, 37]
def replace(g):
    g = [17, 28, 45]
    print("g =", g)

replace(f)

def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g =", g)
print(f)
replace_contents(f)

def banner(message, border='-'): # this is with default value
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Iman Kurniawan")
banner("Iman Kurniawan","*")
banner("Iman Kurniawan", border="*") # this is using keyword argument. Keyword argument is after positional argument

import time
print(time.ctime())

def show_default(arg=time.ctime()):
    print(arg)

show_default() # might be danger in REPL. def only process once time

def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ['bacon', 'eggs']
print(add_spam(breakfast))
lunch = ['baked bean']
print(add_spam(lunch))
print(add_spam())

def add_spam(menu=None): # always use immutable object such as integer or string for default value
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

def add(a, b): # Dynamic typying
    return a + b

print(add(5, 7))
print(add(1.5, 7.1))
print(add("news", "paper"))
print(add([1, 4], [6, 8]))

# add("The anser is", 42) # this will fail this is strong typing, no implicit conversion

# scope
# local -- inside current function
# enclosing -- any and all enclosing function
# global -- top level of module
# build-in --  provided by buildin module (language)

# show attribute of an object
import math
print(type(math))
print(dir(math))
print(type(math.factorial))