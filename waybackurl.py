#!/usr/bin/python3

import sys
import requests as req
import json


def waybackurl(host,with_subs):
    if with_subs == True:
        url = 'https://web.archive.org/cdx/search/cdx?url=*.{0}/*&output=json&fl=original&collapse=urlkey'
    else:
        url = 'https://web.archive.org/cdx/search/cdx?url={0}/*&output=json&fl=original&collapse=urlkey'

    full_url = url.format(host)
    res = req.get(full_url)
    #print(res.text)
    results = res.json()

    return results[1:]



def main():
    argc = len(sys.argv)

         
    if sys.argv[0] == '--help' or sys.argv[0] == '-h' or argc > 3:
        print("{0} <host> <include subdomain: True|False>".format(sys.argv[0]))
        sys.exit(0)

    if argc == 1:
        host_name = sys.stdin.readlines[0] # just first line of the file.
    elif argc == 2:
        host_name = sys.argv[1]
        with_subs = False
    if argc == 3 and (sys.argv[2][0] in 'Tt'):
        host_name = sys.argv[1]
        with_subs = True


    urls = waybackurl(host_name, with_subs)
    
    n_urls = len(urls)

    # quite out put only paste the out put in the file.
    if "-q" not in sys.argv:
        for url in urls:
            print(url[0])

    json_urls = json.dumps(urls)

    if urls != 0:
        file_name = "{0}-wayback-urls".format(sys.argv[1])
        with open(file_name, 'w+') as fd:
            for url in urls:
                fd.write(url[0]+'\n')
        print("[*] Saved results to {0}".format(file_name))
    else:
        print("[-] Found Nothing!!")
        


if __name__ == '__main__':
    main()



