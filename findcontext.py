
#!/usr/bin/python3

import re
import bs4
import sys
import argparse



def help_msg():
    print("{0} - a tool to find the contexts with in the unique cannary exist.".format(sys.argv[0]))
    print("Example Usage:")
    print("$cat file.html | {0} -c \"mystring\"".format(sys.argv[0]))
    print("#find all instences of context with in which `mystring` exist")
    print("$cat file.html | {0}".format(sys.argv[0]))
    print("#find all instences of context with in which `myxsscanary` exist")

    sys.exit(1)

#
# findcontext(link,uniqcanary) - returns a list of tags HTML context
# with in which `uniqcanary` exist from the web page of `link`.
#
def findcontext(htmlcontent,uniqcanary='myxsscanary'):
    contexts = []

    raw_regex = r'<[^>]*?'+uniqcanary+'[^>]*>'
    inside_tag_regex = re.compile(r'<[^>]*?'+uniqcanary+'[^>]*>')
    rendered_webpagetext = htmlcontent 
    attr_tags = inside_tag_regex.findall(htmlcontent)

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
    
    # Check if the --help flag is provided
    if "--help" in sys.argv or "-h" in sys.argv:
        help_msg()

    # command line handling for what to do if the input is cat links.txt | getcontext.py
    parser = argparse.ArgumentParser(description='get contexts of reflected XSS canary')
    parser.add_argument('-c','--canary',default="myxsscanary",help='input links file')
    #parser.add_argument('-o','--output_file',default='/tmp/contexts',help='output result file name')
    #parser.add_argument('-p','--payload',default=unique_canary,help='unique canary payload')
    #parser.add_argument('-t','--format', choices=['csv', 'json'], default='csv', help='Output format (csv/json)')

    args = parser.parse_args()

    # get html content from STDIN
    html_content = sys.stdin.read()
    
    contexts = findcontext(html_content.strip(),args.canary) 

    for context in contexts:
        print(context)

if __name__ == '__main__':
    main()


