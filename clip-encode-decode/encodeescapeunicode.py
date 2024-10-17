#!/usr/bin/python3

import xclipy as clip
import encoders
import sys

def main():
    if len(sys.argv) == 2:
        is_all = sys.argv[1]
        if is_all.lower() == 'yes' or is_all.lower() == 'y' or is_all.lower() == 'all' or is_all.lower() == 'a':
            is_all = True
    else:
        is_all = False

    line = clip.paste()
    encoded_line = encoders.escape_unicode(line,(not is_all))
    clip.copy(encoded_line)

main()
