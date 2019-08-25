#!/usr/bin/env python3
from math import factorial
from pprint import pprint as pp
import os
import glob

def main():
    words = "Why sometimes I have believed".split()
    print(words)

    wordlen = [len(word) for word in words]
    print(wordlen)

    lengths = []
    for word in words:
        lengths.append(len(word))
    print(lengths)

def others():
    numbers = {len(str(factorial(x))) for x in range(20)}
    print(numbers)

def setiter():
    country_to_capital = {'United Kingdom': 'London',
                        'Indonesia': 'Jakarta'}
    capital_to_country = {capital: country for country, capital in country_to_capital.items()}
    pp(capital_to_country)

def file_size():
    file_sizes = {os.path.realpath(p): os.stat(p).st_size
    for p in glob.glob('*.py')}
    pp(file_sizes)
if __name__ == "__main__":
    main()
    others()
    setiter()
    file_size()