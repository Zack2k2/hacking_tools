#!/usr/bin/python3

import encoders
import xclipy as clip

def main():
    line = clip.paste()
    hex_encoded_line = encoders.encode_hex(line)
    clip.copy(hex_encoded_line)

if __name__ == '__main__':
    main()
