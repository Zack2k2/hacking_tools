#!/usr/bin/python3

import sys
import argparse
import urllib.parse

def urlquerylist(link:str):
    parsed_url = urllib.parse.urlparse(link)

    return parsed_url.query.split('&')


#
# validate_URL(link) - returns True if URL structure is valid; False otherwise. 
#
def validate_URL(link):
    try:
        parsed_url = urlparse(link)
        return all([parsed_url.scheme,parsed_url.netloc])
    except:
        return False



def main():
    # command line handling for what to do if the input is cat links.txt | getcontext.py
    parser = argparse.ArgumentParser(description='get contexts of reflected XSS canary')
    parser.add_argument('-f','--input_file',help='input links file')

    args = parser.parse_args()

    if args.input_file:
        if os.path.isfile(args.output_file):
            with open(args.output_file,'r') as f:
                links = f.readlines()
        else:
            print("Error : There is no such file in "+str(args.input_file))
            sys.exit(1)

    else:
        links = sys.stdin.readlines()

    
    for link in links:
        quries_found = urlquerylist(link)

        # i trust sort -u to filter out the repeating 
        for query in quries_found:
            if query == '':
                continue
            print(str(query))


     

if __name__ == '__main__':
    main()
