#!/usr/bin/python3

import xclipy as clip
import sys
import encoders

def main():

    line = clip.paste()
    url_encoded_line = encoders.encode_url(line)
    clip.copy(url_encoded_line)


main()
