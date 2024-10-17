import xclipy as clip
import sys
import json
import urllib.parse as parse


                                                                                                                                                                  
#                                                                                                                                                                   
# validate_URL(link) - returns True if URL structure is valid; False otherwise.                                                                                     
#                                                                                                                                                                   
def validate_URL(link):                                                                                                                                             
    try:                                                                                                                                                            
        parsed_url = parse.urlparse(link)                                                                                                                                 
        return all([parsed_url.scheme,parsed_url.netloc])                                                                                                           
    except:                                                                                                                                                         
        return False   


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    jsonableCookieData = clip.paste()
    try:
        jsonCookieData = json.loads(jsonableCookieData)
    except json.JSONDecodeError:
        sys.exit(1)
        
    basename = '/home/plank/.cookies_jar/'
    parsedurl = parse.urlparse(sys.argv[1])
    


    if not all([parsedurl.scheme,parsedurl.netloc]):
        print("fdvsd")
        exit(1)

    domainname = parsedurl.netloc
    filename = basename + domainname + '.json'
    print('fas')
    with open(filename,"w") as json_fd:
        json.dump(jsonCookieData,json_fd)


if __name__ == '__main__':
    main()
