#!/usr/bin/python3

print(2 + 2)
print(6 * 7)
x = 5
print(x)
print('Hello, Python')

for i in range(5):
    x = i * 10
    print(x)

import math
print(math.sqrt(81))

# How to get help form the module and function
# help(math)
# help(math.sqrt)

print(math.factorial(5))
n = 5
k = 3
result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(result)

from math import factorial
result02 = factorial(n) / (factorial(k) * factorial(n - k))
print(result02)

from math import factorial as fac
result03 = fac(n) / (fac(k) * fac(n - k))
print(result03)

# Note division will generate floating point. The factorial itself generate integer
# integer division is using double forward slash //
result04 = fac(n) // (fac(k) * fac(n - k))
print(result04)

print(fac(100))
print(len(str(fac(100))))

# int
print(10) 
print (0b10) # in binary
print(0o10) # in octal
print(0x10) # in hexadesimal
print(int(3.5)) # rounding is always towards zero
print(int(-3.5))
print(int("496"))
print(int("10000", 3))
# float
print(3.125)
print(3e8)
print(1.1616e-35)
print(float(7))
print(float("1.618"))
print(float("nan")) # not a number
print(float("inf")) # positive number
print(float("-inf")) # negative number
print(3.0 + 1) # operation between int and float will end with float
# None --> represent the absent of value
print(None)
a = None
print(a is None)
# bool -> logical state
# in int  0 = false, and the other number if true. samething with float. Emtpy list is false. Only empty string is false
print(bool(0))
print(bool(0.0))
print(bool(42))
print(bool(-42))
print(bool([]))
print(bool([1, 5, 9]))
print(bool(""))
print(bool("Not empty"))
# == != < > <= >=

g = 20
print(g == 20)
print(g == 13)
print(g != 20)
print(g != 13)
print(g < 30)
print(g > 30)

# if statement
if True:
    print("It's true!")
if False:
    print("It's true!")

if bool("eggs"):
    print("Yes please!")
if "eggs":
    print("Yes please!")

h = 42
if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("50 or smaller")

# for loops and while loop (follow with bool)
c = 5
while c != 0:
    print(c)
    c -= 1 # autmented assignment
c = 5
while c:  # this is not readable
    print(c)
    c -= 1
# Breaking loop
while True:
    response = input()
    if int(response) % 7 == 0:
        break