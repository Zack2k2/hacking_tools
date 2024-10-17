#!/usr/bin/python3

import xclipy as clip
import encoders

def main():
    line = clip.paste()
    encoded_line = encoders.encode_html_named_dec(line)
    clip.copy(encoded_line)

main()
