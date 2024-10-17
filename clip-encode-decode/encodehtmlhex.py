#!/usr/bin/python3

import xclipy as clip
import encoders

def main():
    line = clip.paste()
    encoded_html_hex_line = encoders.encode_html_hex(line)
    clip.copy(encoded_html_hex_line)

main()
