#!/usr/bin/python3
# collection function (dev) is module. module is file

# return will give output

def square(x):
    return x * x

print(square(5))

def launch_missiles():
    print("Missiles lanched!")

launch_missiles()

# implicint return will give none

def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")

even_or_odd(4)
even_or_odd(5)