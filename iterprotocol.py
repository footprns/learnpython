#!/usr/bin/env python3

def main():
    iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
    iterator = iter(iterable)
    print(next(iterator))

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

if __name__ == "__main__":
    main()
    iter = ["1st", "2nd"]
    first(iter)
    
    first(set())