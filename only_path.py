#!/usr/bin/python3

import sys
import urllib.parse

def main():
    
    if len(sys.argv) == 1:
        file_obj = sys.stdin
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
        try:
            file_obj = open(file_name)
        except FileNotFoundError:
            msg = "Sorry, the file "+file_name+" does not exist."
            print(msg)
            file_obj.close()
            sys.exit(0)
        
    for line in file_obj.readlines():
        p_url = urllib.parse.urlparse(line)
        only_path_link = urllib.parse.ParseResult(scheme=p_url.scheme, netloc=p_url.netloc,path=p_url.path,
                                                  query="",params="",fragment="")

        new_link = urllib.parse.urlunparse(only_path_link)
        
        print(new_link)


if __name__ == '__main__':

    main()
