#!/usr/bin/python3

import xclipy as clip
import encoders

def main():
    line = clip.paste()
    encoded_html_dec_line = encoders.encode_html_dec(line)
    clip.copy(encoded_html_dec_line)

main()
