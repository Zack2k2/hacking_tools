#!/usr/bin/python3

import re
import urllib 
import sys
import pprint

#
# The following functions returns a tuple (url_path:str,params:dict)
# returns negative 1 if it doesn't find a query.
def get_url_path_and_params(url_str:str):
    
    start_query_index = -1;

    try:
        start_query_index = url_str.index('?')
    except ValueError:
        return -1
    path_param = (url_str[:start_query_index],{})
    
    query_params = url_str[start_query_index+1:]
    

    try:
        query_params_list = query_params.split('&')

    except ValueError: # there are just one parameters in the link.
        path_param[1].update({query_params.split('=')[0]:query_params.split('=')[1]})
        return path_param;
    
    try:
        for param in query_params_list:
            path_param[1].update({param.split('=')[0]:param.split('=')[1]})
    except IndexError:
        print(url_str)
        return -1# i tired today most of links wouldn't cause a problem 
                 # and work properly

    return path_param


def left_most_split(query:str):
    spited_string = []
    loc = query.index('=')
    spited_string.append(query[:loc])
    spited_string.append(query[loc+1:])
    return spited_string


def get_url_path_and_params_by_dict(link:str):
    
    param_values_dict = {}

    parsed_url = urllib.parse.urlparse(link)
    query_segments = parsed_url.query

    param_segments = query_segments.split('&')

    for param in param_segments:
        par_val = left_most_split(param)
        param_values_dict.update({par_val[0]:par_val[1]})


    return param_values_dict

def get_url_param_query_by_list(link:str):

    parsed_url = urllib.parse.urlparse(link)

    parsed_url = urllib.parse.urlparse(link)
    query_segments = parsed_url.query

    param_segments = query_segments.split('&')

    return param_segments


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
        line_url = get_url_path_and_params(line)

        if line_url != -1:

            print('='*len(line_url[0])+'\n')
            print("[LINK]:"+line);
            print("[PATH:]"+line_url[0])
            print('\n')
            pprint.pprint(line_url[1])

 
if __name__ == '__main__':
    main()









