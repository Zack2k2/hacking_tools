#!/usr/bin/python3

import sys
import os

def usage():
    print("intersection.py prints lines that are common in file1 and file2")
    print("cat file1 | {0} file2")
    sys.exit(1)

def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        usage()

    if os.path.isfile(sys.argv[1]):
        file2_lines = open(sys.argv[1],'r').readlines()
    else:
        usage()


    file1_lines = sys.stdin.readlines()


    for f1_line in file1_lines:
        if f1_line in file2_lines:
            print(f1_line.strip())


if __name__ == '__main__':
    main()
