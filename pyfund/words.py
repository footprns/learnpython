import sys
from urllib.request import urlopen


def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # running from command line argument need sys module

# command line argument passing
# python standard library: argparse
# many third-party option such as docopt
# basically all funtion need to be able to import in repl and run
# print(__name__) # will give the module name

# two way to run from repl
# import words
# words.fetch_words()
# from words import fetch_words
# fetch_words()

# other way 
# from word import (fetch_words, print_words)
# from word import *   --> it will import all function