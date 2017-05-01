#!/usr/local/bin/python2.7
# encoding: utf-8
'''
nba_utils
TODO Create Class for initiate  variables
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
'''
import os
import sys
import csv
import logging
from datetime import datetime


LOG_F = '%(asctime)s - %(name)s - %(lineno)d - %(levelname)s: ' + '%(message)s'


def initialize_logger(log_dir_name, logname, log_level):
    """Initialize logger."""
    log_dir = os.path.join(os.getcwd(), log_dir_name)
    try:
        # Create directory
        create_dir(log_dir)
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        log_format = LOG_F
        formatter = logging.Formatter(log_format)
        handler_stream = logging.StreamHandler()
        handler_stream.setFormatter(formatter)
        handler_stream.setLevel(logging.INFO)
        log.addHandler(handler_stream)
        handler = logging.FileHandler(os.path.join(log_dir, logname + "_" +
                                                   getCurTime("%Y%m%d_%H-%M") +
                                                   ".log"))
        handler.setFormatter(formatter)
        log.addHandler(handler)
        logging.captureWarnings(True)
        log.setLevel(log_level)
        return log
    except (OSError, IOError) as err:
        # return False in case of exception
        print "ERROR: Failed to create log: %s" % err
        return False


def create_dir(dpath):
    try:
        if not os.path.isdir(dpath):
            os.makedirs(dpath)
    except (OSError, IOError) as err:
        # return -1 in case of exception
        print "ERROR: Failed to create directory: %s" % err
        return False


def req_input(help_text):
    """ Input handler. """
    req = raw_input('Enter %s: ' % help_text)
    return req


def get_csv_reader(fpath):
    with open(fpath, 'r') as infile:
        reader = csv.DictReader(infile, delimiter=',')
        file_obj = [x for x in reader]
    return file_obj


def get_csv_writer(fpath, val, new_string):
    with open(fpath, val) as infile:
        writer = csv.writer(infile, delimiter=',')
        writer.writerow(new_string)


def add_new_line_csv(fpath):
    # Add break line in end of CSV file manually :( on start
    with open(fpath, 'a+') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', dialect='excel')
        writer.writerow("")


def get_csv_header(fpath):
    """ Get Header  from CSV file """
    with open(fpath, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
    return fieldnames


def good_exit():
    """ Exit helper. """
    print "Goodbye!"
    sys.exit(0)


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted
    according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time
