#!/usr/local/bin/python2.7
# encoding: utf-8
"""
Utils

@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
"""

import os
import sys
import csv
import logging
from datetime import datetime


LOG_F = '%(asctime)s - %(name)s - %(lineno)d - %(levelname)s: ' + '%(message)s'


def initialize_logger(log_dir_name="logs", log_name="log", log_level="INFO"):
    """
    Initialize logger.

    Parameters :
    log_dir_name : str
        Name of directory for *.log files. Default is "logs"
    log_name : str
        Name of directory for *.log files. Default is "logname"
    log_level : str
        Log level. Default is "INFO"

    Returns :
    object
        Log file as object for add the events.
    """
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
        full_log_name = log_name + "_" + get_cur_time("%Y%m%d_%H-%M") + ".log"
        handler = logging.FileHandler(os.path.join(log_dir, full_log_name))
        handler.setFormatter(formatter)
        log.addHandler(handler)
        logging.captureWarnings(True)
        log.setLevel(log_level)
        return log
    except (OSError, IOError) as err:
        print "ERROR: Failed to create log: %s" % err
        return False


def create_dir(dpath=None):
    """
    Create a directory if it is not exist.

    Parameters :
    dpath : str
        Full directory path in unix format

    Returns :
    False if Directory exist or cannot be created
    """
    if dpath:
        try:
            if not os.path.isdir(dpath):
                os.makedirs(dpath)
            else:
                print "ERROR: Directory exist and cannot be created"
        except (OSError, IOError) as err:
            print "ERROR: Failed to create directory: %s" % err
            return False


def req_input(help_text=None):
    """
    Input handler.

    Parameters :
    help_text : str
        The text wil be printed as help to input.

    Returns :
    objreq : value
        variable from input.
    """
    req = raw_input("Enter %s: " % help_text)
    # while req is True:
    #     if not req:
    #         print 'Please enter "n" for exit or %s: ' % help_text
    #     elif req is "n":
    #         return False
    #     else:
    return req


def get_csv_reader(fpath):
    """
    Reader for CVS file.

    Parameters :
    fpath : str
        Path to csv file.

    Returns :
    object : str
        body of csv file by strings spited by ','
    """
    try:
        with open(fpath, 'r') as infile:
            reader = csv.DictReader(infile, delimiter=',')
            file_obj = [x for x in reader]
        return file_obj
    except (OSError, IOError) as err:
        print "ERROR: Failed to read CSV file: %s" % err
        return False


def add_csv_string(fpath, val="a", new_string=""):
    """
    Write to the CVS file a new string.

    Parameters :
    fpath : str
        Path to csv file.
    val : str
        'a' for append, 'b', or 'ab'
    new_string : str
        New string
    """
    try:
        with open(fpath, val) as infile:
            writer = csv.writer(infile, delimiter=',')
            writer.writerow(new_string)
    except (OSError, IOError) as err:
        print "ERROR: Failed to add string in CSV file: %s" % err
        return False


def get_csv_writer(fpath):
    """
    Write to the CVS file.

    Parameters :
    fpath : str
        Path to csv file.
    Return :
    writer : object
    """
    try:
        with open(fpath, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
        return writer
    except (OSError, IOError) as err:
        print "ERROR: Failed to get writer for CSV file: %s" % err
        return False


def get_csv_header(fpath):
    """
    Get Header from CSV file.

    Parameters :
    fpath : str
        Path to csv file.
    Return :
    fieldnames : object
        Header of csv file as array.
    """
    try:
        with open(fpath, 'r') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
        return fieldnames
    except (OSError, IOError) as err:
        print "ERROR: Failed to get header from CSV file: %s" % err
        return False


def good_exit():
    """ Exit w/o exception and print: Goodbye!"""
    print "Goodbye!"
    sys.exit(0)


def bad_exit():
    """ Exit with exception and print: Something wrong! Goodbye!"""
    print "Something wrong! Goodbye!"
    sys.exit(1)


def get_cur_time(date_time_format):
    """
    Get current date-time accordance to date_time_format.

    Parameters :
    date_time_format : str
        It cab be like '%Y%m%d_%H-%M'

    Returns :
    Returns current date_time as a string formatted
    according to date_time_format
    """
    if date_time_format:
        date_time = datetime.now().strftime(date_time_format)
        return date_time
    else:
        print "No Date/Time format"
