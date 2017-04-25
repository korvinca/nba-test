
import csv
import argparse
from nba_utils import main_menu
from pprint import pprint


NBA_OPTIONS = ["List of Players", "List of Teams", "Player stats",
               "Add player", "Team", "STATS", "Quit"]

desc = """Script performs NBA stats searching."""
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-f", "--file", default=False,
                    required=True,help="Input file with NBA data")
args = parser.parse_args()

a = csv.DictReader(open(args.file), delimiter=',')
d = [x for x in a]

main_menu(d)
