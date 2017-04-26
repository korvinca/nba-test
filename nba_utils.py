#!/usr/local/bin/python2.7
# encoding: utf-8
'''
nba_utils
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
'''

NBA_OPTIONS = ["List of Players", "List of Teams", "Player stats",
               "Add player", "Team", "STATS", "Quit"]

NBA_STATS = ["FT", "MIN", "BL", "3P", "TOT", "FG", "3PA",
             "DR", "OR", "TO", "PF", "PTS", "FGA", "A", "ST"]


def _player_stats(d):
    print "Player stats:"
    print ("Available STAT values: %s" % " ".join(map(str, NBA_STATS)))
    player_name = _req_input("player name and STAT (optional)")
    all_players = _full_player_name(d)
    stat = _check_name_with_stats(player_name)
    if stat:
        res = player_name.split(" ")[:-1]
        player_name = " ".join(map(str, res))
#        print player_name
        if player_name in all_players:
            player_dic = find_dic_in_file(d, "PLAYER FULL NAME", player_name)
#            print player_dic
            res = sort_by_stats(player_dic, stats=stat)
            print player_name, stat + ":", res
        else:
            print ("No players with name: %s" % player_name)
            print "Check Player name and STAT (one from list below, optional)."
            print ("Available STAT values: %s" % " ".join(map(str, NBA_STATS)))
    else:
        if player_name in all_players:
            player_dic = find_dic_in_file(d, "PLAYER FULL NAME", player_name)
#            print player_dic
            res = sort_by_stats(player_dic)
            print player_name, " ".join(map(str, res))
            return res
        else:
            print ("No players with name: %s" % player_name)
            print "Check Player name and STAT (one from list below, optional)."
            print ("Available STAT value: %s" % " ".join(map(str, NBA_STATS)))


def sort_by_stats(player_dic, stats=None):
    output = []
    if stats:
        output = player_dic.get(stats)
    else:
        for i in NBA_STATS:
            output.append(player_dic.get(i))
    return output


def find_dic_in_file(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return dic
    return -1


def _all_players(d):
    print "All players names:"
    output = []
    for row in d:
        v_search = "PLAYER FULL NAME"
        player = row.get(v_search)
        output.append(player)
    return output


def _list_of_teams(d):
    print "List of Teams:"
    output = []
    for row in d:
        own_team = "OWN TEAM"
        opp_team = "OPP TEAM"
        name_of_team = row.get(own_team or opp_team)
        if name_of_team not in output:
            output.append(name_of_team)
    for n in output:
        print n


def _full_player_name(d, for_print=None):
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
    full_name = full_name.upper()
    stat = full_name.split(" ")[-1]
    if stat in NBA_STATS:
        return stat
    else:
        return None


def _add_player():
    print "Add player:"


def _team():
    print "Team:"


def _stats():
    print "STATS"


def _req_input(help_text):
    req = raw_input('Enter %s: ' % help_text)
    return req


def main_menu(d):
    _print_main_menu()
    is_valid = 0
    while not is_valid:
        while not is_valid:
            try:
                choice = int(raw_input('Enter your choice [1-7] : '))
                is_valid = 1
            except ValueError, e:
                print ("'%s' is not a valid integer." %
                       e.args[0].split(": ")[1])
        if choice == 1:
            _full_player_name(d, for_print=True)
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
            _stats_menu(d)
        elif choice == 7:
            print ("Goodbye!")
            exit
        else:
            is_valid = 0
            print ("Invalid number. Try again...")


def _stats_menu(d):
    _print_stats_menu()
    is_valid_stat = 0
    while not is_valid_stat:
        while not is_valid_stat:
            try:
                choice = int(raw_input('Enter your choice [0-15] : '))
                is_valid_stat = 1
            except ValueError, e:
                print ("'%s' is not a valid integer." %
                       e.args[0].split(": ")[1])
        if choice == 0:
            _print_main_menu()
            exit
        elif choice == 1:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 2:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 3:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 4:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 5:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 6:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 7:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 8:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 9:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 10:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 11:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 12:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 13:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 14:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        elif choice == 15:
            _stats()
            is_valid_stat = 0
            _print_stats_menu()
        else:
            is_valid_stat = 0
            print ("Invalid number. Try again...")


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
    print ("6. STATS MENU >>")
    print ("7. Quit")
    print (35 * '-')


def _print_stats_menu():
    print (35 * '-')
    print ("   N B A   S T A T   S E A R C H")
    print ("   S T A T S - M E N U")
    print (35 * '-')
    print ("0. << Go to MAIN MENU")
    print ("1. FT")
    print ("2. Min")
    print ("3. BL")
    print ("4. 3P")
    print ("5. Tot")
    print ("6. FG")
    print ("7. 3PA")
    print ("8. DR")
    print ("9. OR")
    print ("10. TO")
    print ("11. PF")
    print ("12. PTS")
    print ("13. FGA")
    print ("14. A")
    print ("15. ST")
    print (35 * '-')
