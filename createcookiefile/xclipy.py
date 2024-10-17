import sys
import subprocess

#
# For some odd reason pyperclip was 
# not working for so i ended up writing
# my own clip board copy and paste management 
# wraper. build on top of calling linux xclip
# command, xclip is clipboard management command 
# in linux distros. It works like works like a charm.
#

def paste():
    return subprocess.check_output(['xclip', '-selection', 'c', '-o']).decode().strip()

def copy(dataline):
    subprocess.Popen(['xclip', '-selection', 'c'], stdin=subprocess.PIPE).communicate(input=dataline.encode())
