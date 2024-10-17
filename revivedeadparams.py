#!/usr/bin/python3

import os
import sys
import urllib.parse
import requests
import argparse


def main():
    # command line handling for what to do if the input is cat links.txt | getcontext.py
    parser = argparse.ArgumentParser(description='takes a list of links and check weather they are online or offline')
    parser.add_argument('-i','--input_file',help='input freash links file')
    parser.add_argument('-d','--dead_param',default='/tmp/offline_param.txt',help='offline links dead paramerters')

    args = parser.parse_args()

    live_links_file = args.input_file
    dead_param_file = args.dead_param


    if live_links_file:
        if os.path.isfile(live_links_file):
            with open(live_links_file) as f:
                links = f.readlines()
        else:
            print("[Error] live find not found/invalid")
            sys.exit(1)

    else:
        links = sys.stdin.readlines()

    if dead_param_file:
        if os.path.isfile(dead_param_file):
            with open(dead_param_file) as f:
                dead_parameters = f.readlines()
        else:
            print("[Error] dead parameter files not found")
            sys.exit(1)

    for live_link in links:
        parsed_url = urllib.parse.urlparse(live_link.strip())
        for param in dead_parameters:
            if parsed_url.query == '':
                new_query_postfix = param
            else:
                new_query_postfix = parsed_url.query + '&' + param
            
            parsed_url_link_postfix = urllib.parse.ParseResult(scheme= parsed_url.scheme,netloc=parsed_url.netloc, 
                                                    path=parsed_url.path, params=parsed_url.params, 
                                                    query=new_query_postfix, 
                                                    fragment=parsed_url.fragment )
            
           

            new_url_link_postfix = urllib.parse.urlunparse(parsed_url_link_postfix)
            print(new_url_link_postfix.strip())






if __name__ == '__main__':
    main()
