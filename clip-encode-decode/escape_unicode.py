#!/usr/bin/python3

import xclipy as clip
import encoders
import sys

def main():
    if len(sys.argv) == 2:
        pad = int(sys.argv[1])
    else:
        pad = 4

    line = clip.paste()
    encoded_line = encoders.escape_unicode(line)
    clip.copy(encoded_line)

main()
