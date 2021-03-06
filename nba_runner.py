#!/usr/local/bin/python2.7
# encoding: utf-8
"""
nba_runner
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
"""

import argparse
import sys
import os.path
from nba_helper import NBAStats
from utils import initialize_logger


def parse_arg():
    """ Parsing -file *.CSV file. File should be located in the same dir."""
    desc = """Script performs NBA stats searching."""
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-f", "--file", default=False,
                        required=True, help="Input file with NBA data.")
    args = parser.parse_args()
    path_to_file = args.file
    # Is file with data exist?
    if not os.path.exists(path_to_file):
        LOG.error("No file with data.")
        sys.exit(1)
    return path_to_file


def main(fpath):
    """test"""
    LOG.info("Starting script")
    LOG.debug(fpath)
    # To fix the break line verification in the end of csv file on start.
    # Uncomment line below
    # add_csv_string(fpath)
    statwork = NBAStats(fpath, LOG)
    statwork.main()


if __name__ == '__main__':
    LOG = initialize_logger("logs", "nba", "INFO")
    sys.exit(main(parse_arg()))
