#!/usr/bin/python3

import sys
import os
import urllib
import requests as req
import argparse
import csv
import json



#
# validate_URL(link) - returns True if URL structure is valid; False otherwise. 
#
def validate_URL(link):
    try:
        parsed_url = urlparse(link)
        return all([parsed_url.scheme,parsed_url.netloc])
    except:
        return False

#
# is_link_online(link) returns weather a link is online or offline.
#
def is_link_online(link:str):
    res = req.get(link)
    if res.status_code == 200:
        return True

    return False



def main():
    # command line handling for what to do if the input is cat links.txt | getcontext.py
    parser = argparse.ArgumentParser(description='takes a list of links and check weather they are online or offline')
    parser.add_argument('-i','--input_file',help='input links file')
    parser.add_argument('-o','--online_out_file',default='/tmp/online_links.txt',help='online links output file')
    parser.add_argument('-f','--offline_out_file',default='/tmp/offline_links.txt',help='offline links output file')

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
    

    if args.online_out_file != '/tmp/online_links.txt':
        if not os.path.isfile(args.online_out_file):
            print("output file not valid, defaulting")
            args.output_file = '/tmp/online_links.txt'


    if args.offline_out_file != '/tmp/offline_links.txt':
        if not os.path.isfile(args.offline_out_file):
            print("output file not valid, defaulting")
            args.output_file = '/tmp/offline_links.txt'


    online_links_fd = open(args.online_out_file,'a')
    offline_links_fd = open(args.offline_out_file,'a')

    
    for link in links:
        link = link.strip()
        if is_link_online(link):
            link += '\n'
            online_links_fd.write(link)
        else:
            link += '\n'
            offline_links_fd.write(link)



    online_links_fd.close()
    offline_links_fd.close()


if __name__ == '__main__':
    main()
