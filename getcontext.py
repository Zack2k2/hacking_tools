#!/usr/bin/python3

#
# getcontext.py - find and prints the context with in which 
# HTML context(tags, tag attribute or between tags) the reflected parameter
# and value occurs in.
#

import re 
import sys
import bs4
import requests as req
import time
import os
from urllib.parse import urlparse
import urllib.parse as url
from requests_html import HTMLSession
import csv
import shelve
import argparse
import json



#
# help_msg() - print help message.
#
def help_msg():
    print("Usage: "+sys.argv[0]+" file|link")
    print(sys.argv[0]+" - get the context of the reflecetd parameter and value")
    print("that exist with in the HTML context, like tags, attribte and node name")
    sys.exit(1)


#Class of Errors to come

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
# Gets cookies from ~/.cookie_jar 
#
#
def getCookie(url:str,root_directory=''):
    parseable_url = urlparse(url)

    # get the part of url/link with only domain part
    urldomain = parseable_url.netloc 
    
    # custom directory 
    basepath = '/home/plank/.cookies_jar/'
    if os.path.isdir(root_directory):
        basepath = root_directory
    else:
        basepath = '/home/plank/.cookies_jar/'


    cookie_file_string = urldomain + '.json'
    filepathname = basepath + cookie_file_string 
    cookie_jar = req.cookies.RequestsCookieJar()

    if os.path.isfile(filepathname):
        json_cookie_fd = open(filepathname)
        jsonable_cookie_data = json_cookie_fd.read()
    else:
        # Found no cookie file.
        raise FileNotFoundError

    json_cookie_data = json.loads(jsonable_cookie_data)

    for cookie_section in json_cookie_data:
        cookie_jar.set(cookie_section['name'],cookie_section['value'],domain=urldomain)

    return cookie_jar;
        


#
# getwebpage(session, link) - returs full JS rendered HTML page 
# provided of link `link` request_html.HTMLSession `session` 
#
def getwebpage(session,link):
    try:
        mycookies = getCookie(link)
        res = req.get(link,cookies=mycookies )
    except FileNotFoundError:
        res = req.get(link)
    
    if res.ok:
        return res.text
    else:
        print("DEBUG" +link+" not found")
        return ""



#
# findcontext(link,uniqcanary) - returns a list of tags HTML context
# with in which `uniqcanary` exist from the web page of `link`.
#
def findcontext(session,link,uniqcanary):
    contexts = []

    raw_regex = r'<[^>]*?'+uniqcanary+'[^>]*>'
    inside_tag_regex = re.compile(r'<[^>]*?myxsscanary[^>]*>')
    rendered_webpagetext = getwebpage(session,link)
    attr_tags = inside_tag_regex.findall(rendered_webpagetext)
    for attr_tag in attr_tags:
        tagstr = bs4.BeautifulSoup(attr_tag,'html.parser')
        if tagstr.find() == None:
            continue
        tagname = tagstr.find().name
        contexts.append(tagname+"[inside]")

    page_soup = bs4.BeautifulSoup(rendered_webpagetext,'html.parser')
    outside_tags = page_soup.find_all(string=lambda string: uniqcanary in string)

    for tag in outside_tags:
        contexts.append(tag.parent.name+"[outside]")

    return contexts



def main():
    csv_file_name = '/tmp/contexts.csv'
    
    output_writer = open(csv_file_name,'w',newline='')


    argc = len(sys.argv)
    unique_canary = "myxsscanary"
    links = []  # list of valid links that needs to be check for reflected XSS.
    session = HTMLSession()
    csv_writer = csv.writer(output_writer)

    # command line handling for what to do if the input is cat links.txt | getcontext.py
    parser = argparse.ArgumentParser(description='get contexts of reflected XSS canary')
    parser.add_argument('-f','--input_file',help='input links file')
    parser.add_argument('-o','--output_file',default='/tmp/contexts',help='output result file name')
    parser.add_argument('-p','--payload',default=unique_canary,help='unique canary payload')
    parser.add_argument('-t','--format', choices=['csv', 'json'], default='csv', help='Output format (csv/json)')

    args = parser.parse_args()

    if args.input_file:
        if os.path.isfile(args.output_file):
            with open(args.output_file,'r') as f:
                links = f.readlines()
        else:
            links = sys.stdin.readlines()
    else:
        links = sys.stdin.readlines()

    if args.output_file != '/tmp/contexts':
        if not os.path.isfile(args.output_file):
            print("output file not valid, defaulting")
            args.output_file = '/tmp/contexts'

        
    # -- Local variables
    # -c unique_canary, -f links
    # -o outputfile -csv -json 

    context_db = {}
    for link in links:
        line = [link.strip()]

        contexts = findcontext(session,link,unique_canary)
        if len(contexts) == 0:
            continue
        else:
            for context in contexts:
                line.append(context)

        print("URL:["+link.strip()+"] contexts:["+str(contexts)+"]")
        context_db.update({link:contexts})

    
    unique_context_dict = {}

    for link,contexts in context_db.items():
        link_a = url.urlparse(link.strip());
                
        link_a_parts = url.ParseResult(link_a.scheme,link_a.netloc,link_a.path,"","","")
        new_a_url = url.urlunparse(link_a_parts)
        if new_a_url not in unique_context_dict.keys():
            unique_context_dict.update({new_a_url:set()})
            for c in contexts:
                unique_context_dict.get(new_a_url).add(c)
        else:
            for c in contexts:
                unique_context_dict.get(new_a_url).add(c)

    if args.format == 'csv':
        for link, contexts in unique_context_dict.items():
            csvline = []
            unique_context_dict[link] = list(unique_context_dict[link])
            csvline.append(link)
            for c in unique_context_dict[link]:
                csvline.append(c)
            csv_writer.writerow(csvline)

    else:
        for link, contexts in unique_context_dict.items():
            unique_context_dict[link] = list(unique_context_dict[link])
        json_object = json.dumps(unique_context_dict, indent=4)

        with open("/tmp/unique_contexts.json","w") as outfile:
            outfile.write(json_object)



if __name__ == '__main__':
    main()
