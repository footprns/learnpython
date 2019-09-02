'''Read and print an integer series'''

import sys

# with block 
def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [ int(line.strip()) for line in f ]
    # try:
    #     f = open(filename, mode='rt', encoding='utf-8')
    #     return [ int(line.strip()) for line in f ]
    # finally:
    #     f.close()

def main(filename):
    series =  read_series(filename)
    print(series)

if __name__ == '__main__':
  main(sys.argv[1])