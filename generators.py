#!/usr/bin/env python3

# elegan way to iterable sequences
# lazily evaluated

from itertools import islice, count
from filterpredicate import is_prime

def gen123():
    yield 1
    yield 2
    yield 3

def battery():
    # islice(all_primes, 1000)
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(list(thousand_primes))
    result = sum(islice((x for x in count() if is_prime(x)), 1000))
    print(result)

def temp():
    sunday = [2, 3, 5]
    monday = [5, 3, 8]
    for item in zip(sunday, monday):
        print(item)
        print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(
            min(item), max(item), sum(item) / len(item)))

    for sun, mon in zip(sunday, monday):
        print("average =", (sun + mon) / 2)
if __name__ == "__main__":
    g = gen123()
    print(g)
    print(next(g))
    print(next(g))
    print(next(g))
    # print(next(g))
    
    for v in gen123():
        print(v)
    
    battery()
    print(any([False, False, True]))
    print(all([False, False, True]))
    print(all(name == name.title() for name in ['London', 'New York', 'Jakarta']))
    temp()


