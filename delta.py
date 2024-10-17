#!/usr/bin/python3


import sys
import os

def usage():
    print("delta.py prints lines that are not common in file1 and file2")
    print("#cat file1 | {0} file2")
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

    delta_lines = file1_lines_set.symmetric_difference(file2_lines_set)

    for delta_line in delta_lines:
        print(delta_line.strip())


if __name__ == '__main__':
    main()
