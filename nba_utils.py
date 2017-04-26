#!/usr/local/bin/python2.7
# encoding: utf-8
'''
nba_utils
TODO Create Class for initiate  variables
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
'''
import sys
import csv


NBA_STATS = ["FT", "MIN", "BL", "3P", "TOT", "FG", "3PA",
             "DR", "OR", "TO", "PF", "PTS", "FGA", "A", "ST"]
CONSTDATA = {"DATA SET": "",
             "DATE": "",
             "POSITION": "",
             "OWN TEAM": "",
             "OPP TEAM": "",
             "Venue": "",
             "FTA": ""}


def _get_header(fpath):
    """ Get Header  from CSV file """
    with open(fpath, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        infile.close()
    return fieldnames


def _add_player(fpath):
    """ Add new Player in CSV file """
    nba_stat_local = ["FT", "MIN", "BL", "3P", "TOT", "FG", "3PA",
                      "DR", "OR", "TO", "PF", "PTS", "FGA", "A", "ST"]
    print "Enter player name and stats: %s" % (', '.join(nba_stat_local))
    new_player = _req_input("")
    if new_player:
        new_string = []
        nba_stat_local.insert(0, "PLAYER FULL NAME")
        player_name = " ".join(map(str, new_player.split()[:-15:]))
        player_stat = new_player.split()[-15:]
        player_stat.insert(0, player_name)
        new_dict = dict(zip(nba_stat_local, player_stat))
        new_dict.update(CONSTDATA)
        fieldnames = _get_header(fpath)
        for x in fieldnames:
            v = new_dict.get(x)
            new_string.append(v)
        with open(fpath, 'a+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', dialect='excel')
            writer.writerow(new_string)
        print "Player %s has been added." % player_name
    else:
        print "No player name or incorrect stats."


def _team(d):
    """ Get lest of Players in the Team """
    team_name = _req_input("name of Team")
    if team_name in _list_of_teams(d):
        team = "OWN TEAM"
        print "Players in team %s:" % team_name
        for f in d:
            if team_name in f.get(team):
                player = f.get("PLAYER FULL NAME")
                print player
    else:
        print "No team with name: %s" % team_name


def _player_stats(d):
    """ Get Player status """
    print "Player stats:"
    print "Available STAT values: %s" % " ".join(map(str, NBA_STATS))
    player_name = _req_input("player name and STAT (optional)")
    all_players = _full_player_name(d)
    stat = _check_name_with_stats(player_name)
    if stat:
        res = player_name.split(" ")[:-1]
        player_name = " ".join(map(str, res))
        if player_name in all_players:
            player_dic = find_dic_in_file(d, "PLAYER FULL NAME", player_name)
            res = sort_by_stats(player_dic, stats=stat)
            print player_name, stat + ":", res
        else:
            print "No players with name: %s" % player_name
            print "Check Player name and STAT (one from list below, optional)."
            print "Available STAT values: %s" % " ".join(map(str, NBA_STATS))
    else:
        if player_name in all_players:
            player_dic = find_dic_in_file(d, "PLAYER FULL NAME", player_name)
            res = sort_by_stats(player_dic)
            print player_name, " ".join(map(str, res))
            return res
        else:
            print "No players with name: %s" % player_name
            print "Check Player name and STAT (one from list below, optional)."
            print "Available STAT value: %s" % " ".join(map(str, NBA_STATS))


def sort_by_stats(player_dic, stats=None):
    """ Sort Player stats by order in request. """
    output = []
    if stats:
        output = player_dic.get(stats)
    else:
        for i in NBA_STATS:
            output.append(player_dic.get(i))
    return output


def find_dic_in_file(d, key, value):
    """ Get dictionary from CSV file. """
    for i, dic in enumerate(d):
        if dic[key] == value:
            return dic
    return -1


def _all_players(d):
    """ Get all Players Name. """
    print "All players names:"
    output = []
    for row in d:
        v_search = "PLAYER FULL NAME"
        player = row.get(v_search)
        output.append(player)
    return output


def _list_of_teams(d, for_print=None):
    """ Get list of teams. """
    output = []
    for row in d:
        team = "OWN TEAM"
        name_of_team = row.get(team)
        if name_of_team not in output:
            output.append(name_of_team)
    if for_print:
        print "List of Teams:"
        for n in output:
            print n
    else:
        return output


def _full_player_name(d, for_print=None):
    """ Get Full Player name. """
    print "All players names:"
    output = []
    for row in d:
        v_search = "PLAYER FULL NAME"
        player = row.get(v_search)
        output.append(player)
    if for_print:
        for pl_name in output:
            print pl_name
    else:
        return output


def _check_name_with_stats(full_name):
    """ Check Player name in Stats and return stat only. """
    full_name = full_name.upper()
    stat = full_name.split(" ")[-1]
    if stat in NBA_STATS:
        return stat
    else:
        return None


def _stats(d, stat):
    """ Put values in list of stat. """
    output = []
    for row in d:
        count = row.get(stat)
        if count is None:
            continue
        else:
            output.append(count)
    return output


def _stat_count(d, stat, val):
    """ Method to handle min, max, avg and median requests for stat"""
    req = _stats(d, stat)
    if len(req) > 0:
        if val is "max":
            output = max(req)
        elif val is "min":
            output = min(req)
            if output is None:
                output = 0
        elif val is "avg":
            req = map(float, req)
            output = round(sum(req) / float(len(req)), 1)
        elif val is "median":
            req = map(float, req)
            req = sorted(req)
            half, odd = divmod(len(req), 2)
            if odd:
                output = req[half]
            output = (req[half - 1] + req[half]) / 2.0
        print "Output for %s of %s: %s" % (val, stat, output)
    else:
        print "No values"


def _req_input(help_text):
    """ Input handler. """
    req = raw_input('Enter %s: ' % help_text)
    return req


def _exit():
    """ Exit helper. """
    print "Goodbye!"
    sys.exit(0)


def main_menu(fpath):
    """
    Main Menu
    Open CSV file for read here.
    input: path to CSV file
    """
    _print_main_menu()
    is_valid = 0
    with open(fpath, 'r') as infile:
        reader = csv.DictReader(infile, delimiter=',')
        d = [x for x in reader]
    while not is_valid:
        while not is_valid:
            try:
                choice = int(raw_input('Enter your choice [1-7] : '))
                is_valid = 1
            except ValueError, e:
                print "'%s' is not a valid integer." % e.args[0].split(": ")[1]
        if choice == 1:
            _full_player_name(d, for_print=True)
            is_valid = 0
            _print_main_menu()
        elif choice == 2:
            _list_of_teams(d, for_print=True)
            is_valid = 0
            _print_main_menu()
        elif choice == 3:
            _player_stats(d)
            is_valid = 0
            _print_main_menu()
        elif choice == 4:
            _add_player(fpath)
            is_valid = 0
            main_menu(fpath)
        elif choice == 5:
            _team(d)
            is_valid = 0
            _print_main_menu()
        elif choice == 6:
            is_valid = 0
            _stats_menu(d, fpath)
        elif choice == 7:
            _exit()
        else:
            is_valid = 0
            print "Invalid number. Try again..."


def _stats_menu(d, fpath):
    """ Sub menu for Main Menu with list of Stats. """
    _print_stats_menu()
    is_valid_stats = 0
    while not is_valid_stats:
        while not is_valid_stats:
            try:
                choice = int(raw_input('Enter your choice [0-16] : '))
                is_valid_stats = 1
            except ValueError, e:
                print "'%s' is not a valid integer." % e.args[0].split(": ")[1]
        if choice == 0:
            main_menu(fpath)
        elif choice == 1:
            _stat_menu(d, fpath, "FT")
        elif choice == 2:
            _stat_menu(d, fpath, "MIN")
        elif choice == 3:
            _stat_menu(d, fpath, "BL")
        elif choice == 4:
            _stat_menu(d, fpath, "3P")
        elif choice == 5:
            _stat_menu(d, fpath, "TOT")
        elif choice == 6:
            _stat_menu(d, fpath, "FG")
        elif choice == 7:
            _stat_menu(d, fpath, "3PA")
        elif choice == 8:
            _stat_menu(d, fpath, "DR")
        elif choice == 9:
            _stat_menu(d, fpath, "OR")
        elif choice == 10:
            _stat_menu(d, fpath, "TO")
        elif choice == 11:
            _stat_menu(d, fpath, "PF")
        elif choice == 12:
            _stat_menu(d, fpath, "PTS")
        elif choice == 13:
            _stat_menu(d, fpath, "FGA")
        elif choice == 14:
            _stat_menu(d, fpath, "A")
        elif choice == 15:
            _stat_menu(d, fpath, "ST")
        elif choice == 16:
            _exit()
        else:
            is_valid_stats = 0
            print "Invalid number. Try again..."


def _stat_menu(d, fpath, stat):
    """ Sub menu for Stats Menu with list of count method. """
    _print_stat_menu()
    is_valid_stat = 0
    while not is_valid_stat:
        while not is_valid_stat:
            try:
                choice = int(raw_input('Enter your choice [0-5] : '))
                is_valid_stat = 1
            except ValueError, e:
                print "'%s' is not a valid integer." % e.args[0].split(": ")[1]
        if choice == 0:
            _stats_menu(d, fpath)
        elif choice == 1:
            _stat_count(d, stat, "max")
            is_valid_stat = 0
            _print_stat_menu()
        elif choice == 2:
            _stat_count(d, stat, "min")
            is_valid_stat = 0
            _print_stat_menu()
        elif choice == 3:
            _stat_count(d, stat, "avg")
            is_valid_stat = 0
            _print_stat_menu()
        elif choice == 4:
            _stat_count(d, stat, "median")
            is_valid_stat = 0
            _print_stat_menu()
        elif choice == 5:
            _exit()
        else:
            is_valid_stat = 0
            print "Invalid number. Try again..."


def _print_main_menu():
    """ Print menu helper. """
    print 35 * '-'
    print "   N B A   S T A T   S E A R C H"
    print "   M A I N - M E N U"
    print 35 * '-'
    print "1. List of Players"
    print "2. List of Teams"
    print "3. Player stats"
    print "4. Add player"
    print "5. Team"
    print "6. STATS MENU >>"
    print "7. Quit"
    print 35 * '-'


def _print_stats_menu():
    """ Print menu helper. """
    print 35 * '-'
    print "   N B A   S T A T S   S E A R C H"
    print "   S T A T S - M E N U"
    print 35 * '-'
    print "0. << Go to MAIN MENU"
    print "1. FT"
    print "2. Min"
    print "3. BL"
    print "4. 3P"
    print "5. Tot"
    print "6. FG"
    print "7. 3PA"
    print "8. DR"
    print "9. OR"
    print "10. TO"
    print "11. PF"
    print "12. PTS"
    print "13. FGA"
    print "14. A"
    print "15. ST"
    print "16. Quit"
    print 35 * '-'


def _print_stat_menu():
    """ Print menu helper. """
    print 35 * '-'
    print "   N B A   S T A T   S E A R C H"
    print "   S T A T  - M E N U"
    print 35 * '-'
    print "0. << Go to STATS MENU"
    print "1. Max"
    print "2. Min"
    print "3. Avg"
    print "4. Median"
    print "5. Quit"
    print 35 * '-'
