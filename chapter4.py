#!/usr/bin/python3

# srt variable with single or double quote
# Multiple string or Escape sequences
print("""this is
a multiline string""")
a = """this is
a multiline string"""
print(a)

m = "this string\nspan multiline\nlines"
print(m)

# no need to differentiate in windows vs linux. python use Universal newlines \n
m = "This is a \" in the string"
print(m)
m = 'This is a \' in the string'
print(m)
# list of excapte is in http://docs.python.org/3/refrerence/lexical_analysis.html#strings
# Below is raw string (what you see is what you get)
path = r'C:\Users\imank'
print(path)

print(str(496))
print(str(6.02))

# string is sequence of unicode
s = "parrot"
print(s[4])
print(type(s[4])) # it show the type of variable is string
# to get help
# help(str) 

c = "oslo"
print(c.capitalize())
print(c)

# bytes is immuitable sequence of bytes
d = b'some bytes'
print(d.split())

# list of encoding http://docs.python.org/3/library/codec.html#standard-encodings
norsk = "sdergre sdfger"
data = norsk.encode('utf-8')
print(data)
norwegian = data.decode('utf-8')
print(norwegian)
# file, network, http are transmitted using bytes

#  list is mutable requences of objects
l = [1, 2, 3, 4]
print(l)
print(l[1])
l[1] = "pear"
print(l)
l = ["apple", "orange"]
print(l[1])

# start empty variable
b = []
b.append(1.618)
print(b)
b.append(1.1414)
print(b)

print(list("characters"))
c = ["cat",
"dog",] # with and without comma, comma is to maintain expand list
print(c)

#  dict mutable mapping of keys to values
d = {'alice': '856-8648-555', 'bob': '989-8655-531', 'eve': '568-8645-533'}
print(d)
print(d['alice'])
d['alice'] = 'new value'
print(d['alice'])
print(d)
d['charles'] = 'new entry'
print(d)
e = {} # create empty dict

# for - loop is visit each item in an iterable series
cities = ["London","New York","Paris"]
for city in cities:
    print(city)

colors = {'crimson': 0xdc143c, 'coral': 0xdc143f, 'teal': 0xdc143a,}
for color in colors:
    print(color, colors[color])

# combine all the information
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
print(story_words)
    
with urlopen('http://sixty-north.com/c/t.txt') as story:
  story_words = []
  for line in story:
      line_words = line.decode('utf-8').split()
      for word in line_words:
          story_words.append(word)
print(story_words)