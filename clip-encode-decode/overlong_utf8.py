import sys


def char_to_4_byte_utf8(char):
    # Ensure the character is a single character (not a string)
    if len(char) != 1:
        raise ValueError("Input must be a single character")

    def m(b):
        return '%'+format(b,'X')
    # Get the Unicode code point of the character
    code_point = ord(char)

    # Check if the code point requires a 4-byte representation

    # Convert the code point to a 4-byte UTF-8 encoding
    utf8_bytes = bytes([0xF0 | ((code_point >> 18) & 0x07),
                        0x80 | ((code_point >> 12) & 0x3F),
                        0x80 | ((code_point >> 6) & 0x3F),
                        0x80 | (code_point & 0x3F)])

    # Return the 4-byte UTF-8 encoding as bytes
    
    return ''.join(map(m,utf8_bytes))

def to_overlong_utf8(hex):
    code_point = int(hex, 16)

    def m(b):
        return '%' + format(b, 'X')

    if code_point < 0x80:
        two_byte = [0xC0 | (code_point >> 6), 0x80 | (code_point & 0x3F)]
        three_byte = [0xE0, 0x80, 0x80 | (code_point & 0x3F)]
        return ''.join(map(m, two_byte)) + ' / ' + ''.join(map(m, three_byte))
    else:
        raise ValueError("Only works for ASCII characters")

if len(sys.argv) < 2:
    sys.exit(1)


print(to_overlong_utf8(hex(ord(sys.argv[1]))[2:]))

print("\n : "+str(char_to_4_byte_utf8(sys.argv[1])))
