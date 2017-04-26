
import csv
import argparse
import pprint
from nba_utils import main_menu, _full_player_name, _list_of_teams, _player_stats



desc = """Script performs NBA stats searching."""
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-f", "--file", default=False,
                    required=True,help="Input file with NBA data")
args = parser.parse_args()
f = open(args.file)

# Get headers
reader = csv.DictReader(f)
#headers = reader.fieldnames

# Get list of dict with records
record = csv.DictReader(f, delimiter=',')
d = [x for x in record]

#_full_player_name(d)
_player_stats(d)
#_list_of_teams(d)

#main_menu(d)

f.close()
