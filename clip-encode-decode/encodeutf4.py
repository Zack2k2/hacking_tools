import xclipy as clip
import encoders
import sys

def main():
    line = clip.paste()
    toggle = True
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == 'yes' or sys.argv[1].lower() == 'true' or sys.argv[1].lower() == 'all':
            toggle = False
        else:
            toggle = True


    encoded_line = encoders.encode_overlong_4_bytes(line,only_special=toggle)
    clip.copy(encoded_line)


if __name__ == "__main__":
    main()
