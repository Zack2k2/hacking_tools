#!/usr/bin/python3

# endswith.py - only fetch subdomains whos names ends with the suplied words.
# those words must be in a list.
# like:
# word.png
# word2.txt

# it will read from stdin and fetch lines that ends with endswords.txt | "word"
# file one can only be provided with stdin.


import sys
from os import path


def main():
    endswithlist = []
    if len(sys.argv) == 1:
        print("{0} <endswith file>".format(sys.argv[0]))
        print("example: cat domainslist.txt | {0} endswithwords.txt".format(sys.argv[0]))
        print("example: cat domainslist.txt | {0} endword".format(sys.argv[0]))
        sys.exit(1)
    
    if len(sys.argv) == 2:
        if path.isfile(sys.argv[1]):
            file = sys.argv[1]
            with open(file) as fd:
                for line in fd:
                    endswithlist.append(line.strip())
        else:
            endswithlist.append(sys.argv[1].strip())


    rawlist = sys.stdin.readlines()

    for listline in rawlist:
        for endword in endswithlist:        # O(n**2)
            if listline.strip().endswith(endword.strip()):   # yes i know i am a bad programmer
                print(listline.strip())


if __name__ == '__main__':
    main()











