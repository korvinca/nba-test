#!/usr/local/bin/python2.7
# encoding: utf-8
'''
nba_utils
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
'''

import csv


def open_file(csv_file):
    try:
        with open(csv_file) as f:
            records = csv.DictReader(f)
            for row in records:
                print row
        return records
    finally:
        f.close()

def _print_main_menu():
    print (35 * '-')
    print ("   N B A   S T A T   S E A R C H")
    print ("   M A I N - M E N U")
    print (35 * '-')
    print ("1. List of Players")
    print ("2. List of Teams")
    print ("3. Player stats")
    print ("4. Add player")
    print ("5. Team")
    print ("6. STATS")
    print ("7. Quit")
    print (35 * '-')


def _print_stats_menu():
    print (35 * '-')
    print ("   N B A   S T A T   S E A R C H")
    print ("   M A I N - M E N U")
    print (35 * '-')
    print ("1. List of Players")
    print ("2. List of Teams")
    print ("3. Player stats")
    print ("4. Add player")
    print ("5. Team")
    print ("6. STATS")
    print ("7. Quit")
    print (35 * '-')

def main_menu(d):
    _print_main_menu()
    is_valid = 0
    while not is_valid:
        while not is_valid:
            try:
                choice = int(raw_input('Enter your choice [1-7] : '))
                is_valid = 1
            except ValueError, e:
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
        ### Take action as per selected menu-option ###
        if choice == 1:
            _full_player_name(d)
            is_valid = 0
            _print_main_menu()
        elif choice == 2:
            _list_of_teams()
            is_valid = 0
            _print_main_menu()
        elif choice == 3:
            _player_stats()
            is_valid = 0
            _print_main_menu()
        elif choice == 4:
            _add_player()
            is_valid = 0
            _print_main_menu()
        elif choice == 5:
            _team()
            is_valid = 0
            _print_main_menu()
        elif choice == 6:
            _stats()
            is_valid = 0
            _print_stats_menu()
        elif choice == 7:
            print ("Goodbye!")
            exit
        else:
            is_valid=0
            print ("Invalid number. Try again...")

def _full_player_name(d):
    print "All players names:"
    for row in d:
        v_search = "PLAYER FULL NAME"
        print "%s" %  row.get(v_search)


def _list_of_teams():
    print "List of Teams:"


def _player_stats():
    print "Player stats:"


def _add_player():
    print "Add player:"


def _team():
    print "Team:"


def _stats():
    print "STATS"
