#!/usr/bin/python3

import encoders
import xclipy as clip

def main():
    line = clip.paste()
    octal_encoded_line = encoders.encode_octal(line)
    clip.copy(octal_encoded_line)

if __name__ == '__main__':
    main()
