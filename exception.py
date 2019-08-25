#!/usr/bin/env python3

import sys
from math import log

def convert(s):
  '''Convert to an integer'''
  
  try:
    return int(s)
    print("Converstion success x=", x)
  except (ValueError, TypeError) as e:
    print("Conversion error: {}"\
      .format(str(e)),
      file=sys.stderr)
    raise

def string_log(s):
  v = convert(s)
  return log(v)

def main(input):
  item = convert(input)
  print(item)
  item = string_log(input)
  print(item)
  
if __name__ == "__main__":
    main(sys.argv[1])

# not to catch TypeError