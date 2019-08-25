import os
import sys
p = '/tmp'
# def eafp(f):
# try:
#   process_file(f)
# except OSError as e:
#   print('Could not process file because {}'\
#     .format(str(e)))

def make_at(path, dir_name):
  original_path = os.getcwd()
  try:
    os.chdir(path)
    os.mkdir(dir_name)
  except OSError as e:
    print(e, file=sys.stderr)
    raise
  finally:
    os.chdir(original_path)
  
  