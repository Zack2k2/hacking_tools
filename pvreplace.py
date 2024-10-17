#!/usr/bin/python3

import sys
import urllib
import os
import urllib.parse
import argparse



#
# pvreplace.py - takes a list of links with parameters 
# one by one, it replaces every parameter value with a unique
# specified payload, every time a paramter value is replaced
# with payload it generates a new link is generated with 
# only its one or (one of its) parameter replaced with payload value.
#


def sanatize_pv_dict(parsed_pv_dict:dict):
    new_dict = {}
    for p,v in parsed_pv_dict.items():
        new_dict.update({p:v[0]})

    return new_dict



#
# takes a dict of query parameters, replaces the values of each item and does it over and over again unit end of dict
#
def pvreplace(query_dict,payload):
    query_list = []
    sanatized_query_dict = sanatize_pv_dict(query_dict)
    

    for k in sanatized_query_dict.keys():
        new_query_dict = sanatized_query_dict.copy()
        new_query_dict[k] = payload
        query_list.append(new_query_dict)

    return query_list




def main():
    # command line handling for what to do if the input is cat links.txt | pvreplace.py
    discript = 'takes a list of links with parameters, one by one \
            it replaces every parameter value with a unique specified payload \
            , every time a value is replaced, a new link is generated.'

    parser = argparse.ArgumentParser(description=discript)
    parser.add_argument('-i','--input_file',help='input freash links file')
    parser.add_argument('-p','--payload',default='myxsscanary',help='payload for the value of param')

    args = parser.parse_args()

    live_links_file = args.input_file
    payload = args.payload


    if live_links_file:
        if os.path.isfile(live_links_file):
            with open(live_links_file) as f:
                links = f.readlines()
        else:
            print("[Error] live find not found/invalid")
            sys.exit(1)

    else:
        links = sys.stdin.readlines()

    

    for live_link in links:
        parsed_url = urllib.parse.urlparse(live_link)
        parsed_query = urllib.parse.parse_qs(parsed_url.query)
        query_list_param = pvreplace(parsed_query,payload)
        
        for query_elem in query_list_param:
            parsed_url_link_postfix = urllib.parse.ParseResult(scheme= parsed_url.scheme,netloc=parsed_url.netloc, 
                                    path=parsed_url.path, params=parsed_url.params, 
                                    query= urllib.parse.urlencode(query_elem,doseq=True), 
                                    fragment=parsed_url.fragment )
            
           

            new_url_link_str = urllib.parse.urlunparse(parsed_url_link_postfix)
            print(new_url_link_str)
            


if __name__ == '__main__':
    main()
