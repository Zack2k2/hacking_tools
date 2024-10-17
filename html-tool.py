
#!/usr/bin/python3



import os
import bs4
import sys
import argparse
from bs4 import Comment
from bs4 import BeautifulSoup
import pprint


def extract_tags(html_content, tag_name,text=False):
    soup = BeautifulSoup(html_content, 'html.parser')
    result = []

    tags = soup.select(tag_name)
    
    if text == True:
        for tag in tags:
            result.append(tag.text)
    else:
        for tag in tags:
            result.append(tag)

    return result


def extract_attribs(html_content, attrib_names, text=False):
    soup = BeautifulSoup(html_content, 'html.parser')
    result = []

    for attrib_name in attrib_names.split(" "):
        elements = soup.find_all(attrs={attrib_name: True})

        for element in elements:
            result.append(element)

    return result



def extract_comments(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    return comments



def help_msg():
    print("{0} tags --css <css selector> --index <number>".format(sys.argv[0]))
    print("{0} tags --css <css selector> ".format(sys.argv[0]))
    sys.exit(1)



def main():
    if '-h' in sys.argv[:] or '--help' in sys.argv[:]:
        help_msg()


    html_content = sys.stdin.read()
    
    parser = argparse.ArgumentParser(description="HTML Tool")
    parser.add_argument("mode", choices=["tags", "attribs", "comments"], help="Mode to operate in")
    parser.add_argument("--css","-c", nargs="?", help="Tag names, attribute names, or 'comments' (depending on mode)")
    parser.add_argument("--index","-i" ,nargs="?", help="Tag names, attribute names, or 'comments' (depending on mode)")
    parser.add_argument("--text","-t", action="store_true", help="get the content text")
    args = parser.parse_args()


    if args.mode == "comments":
        comments = extract_comments(html_content)
        for comment in comments:
            print(comment)
        sys.exit(0)

    if args.mode == "tags":
        if args.css == None:
            help_msg()
        else:
            css_selector = args.css
            elements = extract_tags(html_content,css_selector,args.text)

    
    if args.mode == "attribs":
        if args.css == None:
            help_msg()
        else:
            css_selector = args.css
            elements = extract_attribs(html_content,css_selector,args.text)
        


    if args.index == None:
        pprint.pprint(elements) 
    else:
        try:
            elem_index = int(args.index)
            print(str(elements[elem_index]))
        except ValueError:
            for line in elements:
                print(line)



if __name__ == '__main__':
    main()
