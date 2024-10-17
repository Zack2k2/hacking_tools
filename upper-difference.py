import os
import sys


def usage():
    print("upper-difference.py prints lines that are only in file1 that does not occur in file2")
    print("just like set difference")
    print("$cat file1 | {0} file2")
    print("#...lines that only in file2")
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

    diff_lines = file1_lines_set - file2_lines_set

    for diff_line in diff_lines:
        print(diff_line.strip())

    sys.exit(0)


if __name__ == '__main__':
    main()
