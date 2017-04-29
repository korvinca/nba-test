#!/usr/local/bin/python2.7
# encoding: utf-8
'''
nba_runner
TODO fix the break line verification in the end of csv file on start.
TODO Add verification for user and stats with adding user in CSV file.
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
'''

import argparse
import sys
import os.path
from nba_helper import NBAStats
from utils import initialize_logger


def main(fpath):
    """launch test"""
    log.info("Starting script")
    log.debug(fpath)
#    add_new_line_csv(fpath)
    statwork = NBAStats(fpath, log)
    statwork.main()


def parse_arg():
    desc = """Script performs NBA stats searching."""
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-f", "--file", default=False,
                        required=True, help="Input file with NBA data")
    args = parser.parse_args()
    fpath = args.file
    # Is file with data exist?
    if not os.path.exists(fpath):
        log("No file with data.")
        sys.exit(1)
    return fpath


if __name__ == '__main__':
    log = initialize_logger(".", "nba_test.log", "INFO")
    fpath = parse_arg()
    sys.exit(main(fpath))