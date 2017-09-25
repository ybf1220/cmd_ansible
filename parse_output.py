#!/usr/bin/env python
import sys,re,json

def parse_str(one_line):
  if one_line != "":
    hostname = one_line.split('|')[0]
    ret_code = re.search('(?<=\|).*(?=\=)',one_line)
    if ret_code.group().strip() == "SUCCESS":
      json_str = re.search('{.*}',one_line)
      data = json.loads(json_str.group())
      for line in data['stdout_lines']:
        print line
  else:
    print "input str is null"

    
def main():
  str = sys.argv[1]
  str = str.replace("\r\n"," ")
  parse_str(str)

if __name__ == "__main__":
  main()
