"""
You have volunteered to be the Coordinator for your town’s youth soccer league.As part of your job you need to divide
the 18 children who have signed up for the league into three even teams - Dragons, Sharks and Raptors.
In years past, the teams have been unevenly matched, so this year you are doing your best to fix that.
For each child, you will have the following information: Name, height (in inches),
whether or not they have played soccer before, and their guardians’ names. You'll take a list of these children, divide
them into teams and output a text file listing the three teams and the players on them. There are three main tasks
you'll need to complete to get this done:

1. In your Python program, read the data from the supplied CSV file. Store that data in an appropriate data type so that
it can be used in the next task.

2. Create logic that can iterate through all 18 players and assign them to teams such that each team has
the same number of players. The number of experienced players on each team should also be the same.

3. Finally, the program should output a text file named -- teams.txt -- that contains the league roster listing
the team name, and each player on the team including the player's information:
name, whether they've played soccer before and their guardians' names.
"""

import csv

sharks = []
raptors = []
dragons = []
TEAMS = [sharks, raptors, dragons]


def get_players():
    """
    This function takes list of players saved in csv file and creates list of them.
    :return players: List with information about players.
    """
    with open("soccer_players.csv", newline="") as csvfile:
        artreader = csv.reader(csvfile, delimiter=",")
        players = list(artreader)
    return players[1:]


def split_players(players):
    """
    This function splits players into two groups: advanced players and beginner players.
    :param players: List with information about players.
    :return advanced: List with information about advanced players.
            beginners: List with information about beginner players.
    """
    advanced = []
    beginners = []
    for player in players:
            if player[2] == "YES":
                advanced.append(player)
            else:
                beginners.append(player)
    return advanced, beginners


def create_teams(advanced, beginner, teams):
    team_index = 0

    for team in teams:
        team_size = 0
        while team_size <= len(list_of_players) // len(teams):
            teams[team_index].append([advanced[0]])
            del advanced[0]
            teams[team_index].append([beginner[0]])
            del beginner[0]
            team_size += len(teams[team_index])
        team_index += 1
    return sharks, raptors, dragons


def create_team_lists(sharks, raptors, dragons):
    teams = open("teams.txt", "w")
    teams.write("Sharks" + "\n")
    for shark in sharks:
        for row in shark:
            teams.write("{}, {}, {}\n".format(row[0], row[2], row[3]))
    teams.write("\n" + "Raptors" + "\n")
    for raptor in raptors:
        for row in raptor:
            teams.write("{}, {}, {}\n".format(row[0], row[2], row[3]))
    teams.write("\n" + "Dragons" + "\n")
    for dragon in dragons:
        for row in dragon:
            teams.write("{}, {}, {}\n".format(row[0], row[2], row[3]))

    teams.close()


def create_letters(sharks, raptors, dragons):
    for shark in sharks:
        for row in shark:
            name = str(row[0])
            list = open('%s.txt' % name, 'w')
            list.write(
'''Dear {},
I am pleased to inform you that you son {} is a members of Sharks Football Team. First training starts at 16 PM at school pitch.
Yours faithfully,
John Smiths
School Principal'''.format(row[3], row[0]))
            list.close()
    for raptor in raptors:
        for row in raptor:
            name = str(row[0])
            list = open('%s.txt' % name, 'w')
            list.write(
'''Dear {},
I am pleased to inform you that you son {} is a members of Raptors Football Team. First training starts at 17 PM at school pitch.
Yours faithfully,
John Smiths
School Principal'''.format(row[3], row[0]))
            list.close()
    for dragon in dragons:
        for row in dragon:
            name = str(row[0])
            list = open('%s.txt' % name, 'w')
            list.write(
'''Dear {},
I am pleased to inform you that you son {} is a members of Dragons Football Team. First training starts at 18 PM at school pitch.
Yours faithfully,
John Smiths
School Principal'''.format(row[3], row[0]))
            list.close()

if __name__ == "__main__":
    list_of_players = get_players()
    advanced_players, beginner_players = split_players(list_of_players)
    team_sharks, team_raptors, team_dragons = create_teams(advanced_players, beginner_players, TEAMS)
    create_team_lists(sharks, raptors, dragons)
    create_letters(sharks, raptors, dragons)
