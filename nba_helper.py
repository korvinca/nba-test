#!/usr/local/bin/python2.7
# encoding: utf-8
"""
utils
@author:     Ivan K.
@contact:    ivan.korolevskiy@gmail.com
"""

from utils import (good_exit, req_input, get_csv_reader, get_csv_writer,
                   get_csv_header)

NBA_STATS = ["FT", "MIN", "BL", "3P", "TOT", "FG", "3PA",
             "DR", "OR", "TO", "PF", "PTS", "FGA", "A", "ST"]
CONSTDATA = {"DATA SET": "",
             "DATE": "",
             "POSITION": "",
             "OWN TEAM": "",
             "OPP TEAM": "",
             "Venue": "",
             "FTA": ""}


class NBAStats(object):
    """Base class for NBA app"""
    def __init__(self, fpath, log):
        self.log = log
        self.fpath = fpath
        self.stats = " ".join(map(str, NBA_STATS))
        self.csv = get_csv_reader(fpath)
        self.main()

    def _add_player(self):
        """ Add new Player in CSV file """
        nba_stat_local = ["FT", "MIN", "BL", "3P", "TOT", "FG", "3PA",
                          "DR", "OR", "TO", "PF", "PTS", "FGA", "A", "ST"]
        print "Enter player name and stats: %s" % self.stats
        new_player = req_input("")
        if new_player:
            new_string = []
            nba_stat_local.insert(0, "PLAYER FULL NAME")
            player_name = " ".join(map(str, new_player.split()[:-15:]))
            player_stat = new_player.split()[-15:]
            player_stat.insert(0, player_name)
            new_dict = dict(zip(nba_stat_local, player_stat))
            new_dict.update(CONSTDATA)
            # Get header from CSV file
            fieldnames = get_csv_header(self.fpath)
            for header_items in fieldnames:
                one_header = new_dict.get(header_items)
                new_string.append(one_header)
            # Append a new player in csv file
            get_csv_writer(self.fpath, 'a', new_string)
            print "Player %s has been added." % player_name
        else:
            print "No player name or incorrect stats."

    def _team(self):
        """ Get lest of Players in the Team """
        team_name = req_input("name of Team")
        if team_name in self._list_of_teams():
            team = "OWN TEAM"
            print "Players in team %s:" % team_name
            for playerline in self.csv:
                if team_name in playerline.get(team):
                    player = playerline.get("PLAYER FULL NAME")
                    print player
        else:
            print "No team with name: %s" % team_name

    def _player_stats(self):
        """ Get Player status """
        print "Player stats:"
        print "Available STAT values: %s" % self.stats
        player_name = req_input("player name and STAT (optional)")
        all_players = self._full_player_name()
        stat = self._check_name_with_stats(player_name)
        if stat:
            res = player_name.split(" ")[:-1]
            player_name = " ".join(map(str, res))
            if player_name in all_players:
                player_dic = self._find_dic_in_file("PLAYER FULL NAME",
                                                    player_name)
                res = self._sort_by_stats(player_dic, stats=stat.upper())
                print player_name, stat + ":", res
            else:
                print "No players with name: %s" % player_name
                print "Check Player name and STAT, one from the list below,"
                print "Available STAT values: %s" % self.stats
        else:
            if player_name in all_players:
                player_dic = self._find_dic_in_file("PLAYER FULL NAME",
                                                    player_name)
                res = self._sort_by_stats(player_dic)
                print player_name, " ".join(map(str, res))
                return res
            else:
                print "No players with name: %s" % player_name
                print "Check Player name and STAT (one from list, optional)."
                print "Available STAT value: %s" % self.stats

    def _sort_by_stats(self, player_dic, stats=None):
        """ Sort Player stats by order in request. """
        output = []
        if stats:
            output = player_dic.get(stats)
        else:
            for stat in NBA_STATS:
                output.append(player_dic.get(stat))
        return output

    def _find_dic_in_file(self, key, value):
        """ Get dictionary from CSV file. """
        for i, dic in enumerate(self.csv):
            if dic[key] == value:
                return dic
        return -1

    def _all_players(self):
        """ Get all Players Name. """
        print "All players names:"
        output = []
        for row in self.csv:
            v_search = "PLAYER FULL NAME"
            player = row.get(v_search)
            output.append(player)
        return output

    def _list_of_teams(self, for_print=None):
        """ Get list of teams. """
        output = []
        for row in self.csv:
            team = "OWN TEAM"
            name_of_team = row.get(team)
            if name_of_team not in output:
                output.append(name_of_team)
        if for_print:
            print "List of Teams:"
            for teamname in output:
                print teamname
        else:
            return output

    def _full_player_name(self, for_print=None):
        """ Get Full Player name. """
        print "All players names:"
        output = []
        for row in self.csv:
            v_search = "PLAYER FULL NAME"
            player = row.get(v_search)
            output.append(player)
        if for_print:
            for pl_name in output:
                print pl_name
        else:
            return output

    def _check_name_with_stats(self, full_player_name):
        """ Check is Stat in the same request with Player name and
            return stat only or None.
        """
        stat_and_name_in_upper = full_player_name.upper()
        stat = stat_and_name_in_upper.split(" ")[-1]
        if stat in NBA_STATS:
            return stat
        else:
            return None

    def _stats(self, stat):
        """ Put values in list of stat. """
        output = []
        for row in self.csv:
            count = row.get(stat)
            if not count:
                self.log.info("Null")
                continue
            else:
                output.append(count)
        return output

    def _stat_count(self, stat, val):
        """ Method to handle min, max, avg and median requests for stat"""
        req = self._stats(stat)
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

    def main(self):
        """ Main Menu """
        self.main_menu()
        is_valid = 0
        while not is_valid:
            while not is_valid:
                try:
                    choice = int(raw_input('Enter your choice [1-7] : '))
                    is_valid = 1
                except ValueError, err:
                    print ("'%s' is not a valid integer." %
                           err.args[0].split(": ")[1])
            if choice == 1:
                self._full_player_name(for_print=True)
                is_valid = 0
                self.main_menu()
            elif choice == 2:
                self._list_of_teams(for_print=True)
                is_valid = 0
                self.main_menu()
            elif choice == 3:
                self._player_stats()
                is_valid = 0
                self.main_menu()
            elif choice == 4:
                self._add_player()
                is_valid = 0
                self.main_menu()
            elif choice == 5:
                self._team()
                is_valid = 0
                self.main_menu()
            elif choice == 6:
                is_valid = 0
                self._stats_menu()
            elif choice == 7:
                good_exit()
            else:
                is_valid = 0
                print "Invalid number. Try again..."

    def _stats_menu(self):
        """ Sub menu for Main Menu with list of Stats. """
        self.stats_menu()
        is_valid_stats = 0
        while not is_valid_stats:
            while not is_valid_stats:
                try:
                    choice = int(raw_input('Enter your choice [0-16] : '))
                    is_valid_stats = 1
                except ValueError, err:
                    print ("'%s' is not a valid integer." %
                           err.args[0].split(": ")[1])
            if choice == 0:
                self.main_menu()
            elif choice == 1:
                self._stat_menu("FT")
            elif choice == 2:
                self._stat_menu("MIN")
            elif choice == 3:
                self._stat_menu("BL")
            elif choice == 4:
                self._stat_menu("3P")
            elif choice == 5:
                self._stat_menu("TOT")
            elif choice == 6:
                self._stat_menu("FG")
            elif choice == 7:
                self._stat_menu("3PA")
            elif choice == 8:
                self._stat_menu("DR")
            elif choice == 9:
                self._stat_menu("OR")
            elif choice == 10:
                self._stat_menu("TO")
            elif choice == 11:
                self._stat_menu("PF")
            elif choice == 12:
                self._stat_menu("PTS")
            elif choice == 13:
                self._stat_menu("FGA")
            elif choice == 14:
                self._stat_menu("A")
            elif choice == 15:
                self._stat_menu("ST")
            elif choice == 16:
                good_exit()
            else:
                is_valid_stats = 0
                print "Invalid number. Try again..."

    def _stat_menu(self, stat):
        """ Sub menu for Stats Menu with list of count method. """
        self.stat_menu()
        is_valid_stat = 0
        while not is_valid_stat:
            while not is_valid_stat:
                try:
                    choice = int(raw_input('Enter your choice [0-5] : '))
                    is_valid_stat = 1
                except ValueError, err:
                    print ("'%s' is not a valid integer." %
                           err.args[0].split(": ")[1])
            if choice == 0:
                self._stats_menu()
            elif choice == 1:
                self._stat_count(stat, "max")
                is_valid_stat = 0
                self.stat_menu()
            elif choice == 2:
                self._stat_count(stat, "min")
                is_valid_stat = 0
                self.stat_menu()
            elif choice == 3:
                self._stat_count(stat, "avg")
                is_valid_stat = 0
                self.stat_menu()
            elif choice == 4:
                self._stat_count(stat, "median")
                is_valid_stat = 0
                self.stat_menu()
            elif choice == 5:
                good_exit()
            else:
                is_valid_stat = 0
                print "Invalid number. Try again..."

    @classmethod
    def main_menu(cls):
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

    @classmethod
    def stats_menu(cls):
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

    @classmethod
    def stat_menu(cls):
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
