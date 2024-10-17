# The following program would would get
# all input tags along side with there id and class
# input tags, number of input tags, ids, tags.

# input File Format:
# links1
# links2
# links3

# output Format:
# links1,number_of_inputs,id...,class...


import sys
import csv
import bs4
import requests as req
import argparse
from urllib.parse import urlparse
