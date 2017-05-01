#!/usr/local/bin/python2.7
# encoding: utf-8
'''
nba_runner
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
'''

import argparse
import sys
import os.path
from nba_helper import NBAStats
from utils import initialize_logger


def main(fpath):
    """test"""
    log.info("Starting script")
    log.debug(fpath)
    # To fix the break line verification in the end of csv file on start.
    # Uncomment line below
    # add_new_line_csv(fpath)
    statwork = NBAStats(fpath, log)
    statwork.main()


def parse_arg():
    """ Parsing -file *.CSV file. File should be located in the same dir."""
    desc = """Script performs NBA stats searching."""
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-f", "--file", default=False,
                        required=True, help="Input file with NBA data")
    args = parser.parse_args()
    fpath = args.file
    # Is file with data exist?
    if not os.path.exists(fpath):
        log.error("No file with data.")
        sys.exit(1)
    return fpath


if __name__ == '__main__':
    log = initialize_logger("logs", "nba", "INFO")
    fpath = parse_arg()
    sys.exit(main(fpath))
