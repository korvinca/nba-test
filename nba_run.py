#!/usr/local/bin/python2.7
# encoding: utf-8
'''
nba_runner
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
'''

import argparse
import sys
import csv
import os.path
from nba_utils import main_menu


desc = """Script performs NBA stats searching."""
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-f", "--file", default=False,
                    required=True, help="Input file with NBA data")
args = parser.parse_args()
fpath = args.file

# Is file with data exist?
if not os.path.exists(fpath):
    print "No file with data."
    sys.exit(1)

# TODO fix the break line verification in the end of csv file on start.
# Add break line in end of CSV file manually :( on start
with open(fpath, 'a+') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', dialect='excel')
    writer.writerow("")

main_menu(fpath)
