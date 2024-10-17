import html_entity_names

special_chars = "\'\"><`\\"

#
# encode_url - encode `line` into URL encoding.
#
def encode_url(line):
    return ''.join(['%' + format(ord(char), '02X') for char in line])

#
# encodes the given line returning encoded_hex
#
def encode_hex(line):
    return ''.join(['\\x{0}'.format(hex(ord(c)).upper()[2:]) for c in line ])


#
# encode_octal:
# given a line retuns a string with that is octal encoded. 
#
def encode_octal(line):
    octal_result = ""
    for char in line:
        octal_result += "\\" + oct(ord(char))[2:].zfill(3)
    return octal_result

#
# encode_html_dec
# returns html encoded `line` in decimal encoding.
#
def encode_html_dec(line):
     return ''.join(['&#{0};'.format(ord(char)) for char in line])

#
# returns html encoded `line` that is hex-html encoded.
#
def encode_html_hex(line):
    return ''.join(['&#x{0};'.format(hex(ord(char))[2:]) for char in line])


def encode_html_named_simple(line):
    result = ""
    character_entities = html_entity_names.named_HTML_entities;
    for ch in line:
        if ch in character_entities.keys():
            result = result + character_entities[ch]
        else:
            result = result + ch

    return result

def encode_html_named_dec(line):
    result = ""
    character_entities = html_entity_names.named_HTML_entities;
    for ch in line:
        if ch in character_entities.keys():
            result = result + character_entities[ch]
        else:
            result = result + encode_html_dec(ch);

    return result

def encode_html_named_hex(line):
    result = ""
    character_entities = html_entity_names.named_HTML_entities;
    for ch in line:
        if ch in character_entities.keys():
            result = result + character_entities[ch]
        else:
            result = result + encode_html_hex(ch)
    
    return result


#
# escape_unicode
# convert characters into unicode escaped notations.
#
def escape_unicode(line,special=True,pad=4):
    result_line = ""
    if special == True:
        for ch in line:
            if ch in special_chars:
                hex_ch = hex(ord(ch))[2:].zfill(pad).upper()
                result_line = result_line + "\\u" + hex_ch;
            else:
                result_line = result_line + ch

        return result_line

    else:
        for ch in line:
            hex_ch = hex(ord(ch))[2:].zfill(pad).upper()
            result_line = result_line + "\\u" + hex_ch

        return result_line


def encodetocharcode(line):
    result = ""
    for ch in line:
        if result == "":
            result = str(hex(ord(ch)))[2:]
        else:
            result = result + "," + str(hex(ord(ch)))[2:]

    return result


def char_to_2_byte(char):
    if len(char) != 1:
        return 

    def m(b):
        return '%'+format(b,'X')

    code_point = ord(char)

    if code_point < 0x80:
        two_byte = [0xC0 | (code_point >> 6), 0x80 | (code_point & 0x3F) ]
        return ''.join(map(m,two_byte))
    else:
        return 

    
def char_to_3_byte(char):
    if len(char) != 1:
        return 

    def m(b):
        return '%'+format(b,'X')

    code_point = ord(char)

    if code_point < 0x80:
        three_byte = [0xE0, 0x80, 0x80 | (code_point & 0x3F)]
        return ''.join(map(m,three_byte))
    else:
        return 


def char_to_4_byte(char):
    if len(char) != 1:
        return 

    def m(b):
        return '%'+format(b,'X')

    code_point = ord(char)

    if code_point < 0x80:
        utf8_bytes = bytes([0xF0 | ((code_point >> 18) & 0x07),
                        0x80 | ((code_point >> 12) & 0x3F),
                        0x80 | ((code_point >> 6) & 0x3F),
                        0x80 | (code_point & 0x3F)])

        return ''.join(map(m,utf8_bytes))
    else:
        return 



def encode_overlong_2_bytes(line,only_special=True):
    if only_special:
        result = ""
        for ch in line:
            if ch in special_chars:
                result = result + char_to_2_byte(ch)
            else:
                result = result + ch
        return result
    else:
        return ''.join(['{}'.format(char_to_2_byte(ch)) for ch in line ] )


def encode_overlong_3_bytes(line,only_special=True):
    if only_special:
        result = ""
        for ch in line:
            if ch in special_chars:
                result = result + char_to_3_byte(ch)
            else:
                result = result + ch
        return result
    else:
        return ''.join(['{}'.format(char_to_3_byte(ch)) for ch in line] )

def encode_overlong_4_bytes(line,only_special=True):
    if only_special:
        result = ""
        for ch in line:
            if ch in special_chars:
                result = result + char_to_4_byte(ch)
            else:
                result = result + ch
        return result
    else:
        return ''.join(['{}'.format(char_to_4_byte(ch)) for ch in line] )
