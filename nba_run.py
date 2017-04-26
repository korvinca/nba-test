
import csv
import argparse
from nba_utils import (main_menu, _full_player_name, _list_of_teams,
                       _player_stats, _team, _add_player, _get_header)


desc = """Script performs NBA stats searching."""
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-f", "--file", default=False,
                    required=True, help="Input file with NBA data")
args = parser.parse_args()

f = open(args.file)
headers = _get_header(f)

reader = csv.DictReader(f)
# headers = reader.fieldnames
# Get list of dict with records
record = csv.DictReader(f, delimiter=',')
d = [x for x in record]
# print d
# _list_of_teams(d, for_print=True)
# _team(d)
# _full_player_name(d)
# _player_stats(d)
# _list_of_teams(d)
# main_menu(d)
f.close()


_add_player(f=args.file, h=headers)
