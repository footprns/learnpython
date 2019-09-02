import sys
sys.getdefaultencoding()

f = open('wasteland.txt', mode='wt', encoding='utf-8')
# help(f)

f.write('What are the roots that clutch, ')
f.write('what branches grow\n')
f.write('Out of this stony rubbish? ')
f.close()

g = open('wasteland.txt', mode='rt', encoding='utf-8')
print('----------')
print(g.read(32))
print('----------')
print(g.read())
print('----------')
g.seek(0)
print(g.readline())
print(g.readline())
g.seek(0)
print(g.readlines())
g.close()

# append file
h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['Son of man,\n',
    'for you know only,\n',
    'A heap of broken images, ',
    'where the sun beats\n']
)
h.close()