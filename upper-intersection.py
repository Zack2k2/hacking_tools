#!/usr/bin/python3

import sys
import os

    
def usage():
    print("Description: upper-intersection.py prints lines that are common in file1 and file2.")
    print("also print lines in file1, expluding lines in file2 not present in file1.")
    print("cat file1 | {0} file2".format(sys.argv[0]))
    sys.exit(1)

def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        usage()

    if os.path.isfile(sys.argv[1]):
        file2_lines = open(sys.argv[1],'r').readlines()
    else:
        usage()


    file1_lines = sys.stdin.readlines()

    file1_lines_set = set(file1_lines)
    file2_lines_set = set(file2_lines)

    upper_diff = file1_lines_set.difference(file2_lines_set)
    common_lines = file1_lines_set.intersection(file2_lines_set)

    for up_line in upper_diff:
        print(up_line.strip())

    for common_line in common_lines:
        print(common_line.strip())


    sys.exit(0)


if __name__ == '__main__':
    main()
