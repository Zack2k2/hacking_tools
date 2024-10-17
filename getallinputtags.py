import sys
import bs4
import requests as req
import os
import urllib.parse as parse
import json
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s ')
#logging.disable(logging.DEBUG)

#
# validate_URL(link) - returns True if URL structure is valid; False otherwise. 
#
def validate_URL(link):
    try:
        parsed_url = parse.urlparse(link)
        return all([parsed_url.scheme,parsed_url.netloc])
    except:
        return False


#
# Gets cookies from ~/.cookie_jar 
#
#
def getCookie(url:str,root_directory=''):
    parseable_url = parse.urlparse(url)

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
def getwebpage(link):
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
# sortFreqDict - takes a dict `freqdict` 
# returns a dict of freqdict.keys() sorted by there freqdict.values()
# function to sort a dictionary's keys based on their corresponding values. 
#
def sortFreqDict(freqdict,order=True):
    sortedFreqDict = {}
    sorted_keys = sorted(freqdict,key=lambda k:freqdict[k], reverse=order)
    
    for key in sorted_keys:
        sortedFreqDict.update({key:freqdict[key]})

    return sortedFreqDict



#
# getAllInputTags - returns a link of 
#
def getAllInputTags(link,css):
    webpage = getwebpage()

def main():
    # command line handling for what to do if the input is cat links.txt | getcontext.py
    parser = argparse.ArgumentParser(description='get contexts of reflected XSS canary')
    parser.add_argument('-f','--input_file',help='input links file')
    parser.add_argument('-o','--output_file',default='/tmp/input_tags',help='output result file name')
    parser.add_argument('-s','--css',default="input[type=\"text\"],input[type=\"password\"],input[type=\"email\"],input[type=\"search\"]",help='Css selector for finding input tag')
    parser.add_argument('-t','--format', choices=['csv', 'json'], default='csv', help='Output format (csv/json)')
    parser.add_argument('-v','--verbose',help="Print in verbose",action='store_true')

    args = parser.parse_args()

    if args.input_file:
        if os.path.isfile(args.input_file):
            with open(args.input_file,'r') as fd:
                links = fd.readlines()
        else:
            links = sys.stdin.readlines()
    else:
        links = sys.stdin.readlines()


       # -- Local variables
    # -c unique_canary, -f links
    # -o outputfile -csv -json 

    freq_tags = {}

    sanitized_links = []
    for link in links:
        sanitized_links.append(link.strip())

    for link in sanitized_links:
        freq_tags.update({link:0})

    css_sel = args.css
    for link in sanitized_links:
        webpage = getwebpage(link)
        soup = bs4.BeautifulSoup(webpage,'html.parser')
    
        inputTags = soup.select(css_sel)

        
        numberInputTags = len(inputTags)
        if args.verbose:
            print(link+","+str(numberInputTags))
            continue 


        freq_tags[link] = numberInputTags;

    if args.verbose:
        sys.exit(0)


    

    sorted_freq_tags = sortFreqDict(freq_tags)

    if args.format == 'csv':
        for link,N_tag in sorted_freq_tags.items():
            print(link + "," + str(N_tag))

    if args.format == 'json':
        jsoned_data = json.dumps(sorted_freq_tags,indent=4)
        print(jsoned_data)

if __name__ == '__main__':
    main()


