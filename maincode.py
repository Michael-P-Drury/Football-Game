import random
import time
import numpy as np
import pandas as pd

players = pd.read_csv('footballers.csv')

players = np.array(players)


def team1_print(text):
    print(text)


def team2_print(text):
    print('                              '+text)

def chance_team(team, defense, creation, op_team, team1, jump_to_result):
    goals = 0
    chances = 0
    sot = 0
    for player in team:
        r = random.randint(1, 2000000)
        r1 = random.randint(1, 1500)
        r2 = random.random()
        r3 = random.random()
        player_name = (player[2].capitalize())

        got_through = False

        for op_player in op_team:
            if (player[5] * creation) >= op_player[6] * r:
                got_through = True

        if got_through:
            if team[0][2] == team1[0][2]:
                team1_print(f'{player_name} has an attacking chance')
            else:
                team2_print(f'{player_name} has an attacking chance')
            chances += 1
            if not jump_to_result:
                time.sleep(1)
            if r1 <= player[4]:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name}'s shot was on target")
                else:
                    team2_print(f"{player_name}'s shot was on target")
                sot += 1
                if not jump_to_result:
                    time.sleep(1)
                for op_player in op_team:
                    if op_player[7] != 0:
                        if (r2 * op_player[7]) > (r3 * player[4]):
                            if team[0][2] == team1[0][2]:
                                team1_print(f"{player_name}'s shot was saved by {op_player[2].capitalize()}")
                            else:
                                team2_print(f"{player_name}'s shot was saved by {op_player[2].capitalize()}")
                        else:
                            if team[0][2] == team1[0][2]:
                                team1_print(f"{player_name} SCORED!!")
                            else:
                                team2_print(f"{player_name} SCORED!!")
                            goals += 1
            else:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name} missed")
                else:
                    team2_print(f"{player_name} missed")
                if not jump_to_result:
                    time.sleep(1)
    return goals, chances, sot


def penalty(team, op_team, team1, jump_to_result):

    goals = 0
    sot = 0

    r = random.random()
    r2 = random.random() * 4
    r1 = random.randint(1, 1000)

    if team[0][2] == team1[0][2]:
        team1_print(f"It's a penalty")
    else:
        team2_print(f"It's a penalty")

    if not jump_to_result:
        time.sleep(1)

    choose_from_pen = []
    for player in team:
        choose_from_pen.append(player[2].capitalize())

    for op_player in op_team:
        if op_player[7] != 0:
            loop = True
            choice = 0
            while loop:
                if team[0][2] == team1[0][2]:
                    team1_print(f"Choose a player(by the corresponding number):")
                else:
                    team2_print(f"Choose a player(by the corresponding number):")

                for i, player in zip(range(1, 12), choose_from_pen):
                    if team[0][2] == team1[0][2]:
                        team1_print(f'{i} : {player}')
                    else:
                        team2_print(f'{i} : {player}')
                try:
                    choice = int(input())
                    if 1 <= choice <= 11:
                        loop = False
                    else:
                        if team[0][2] == team1[0][2]:
                            team1_print(f"not a valid input")
                        else:
                            team2_print(f"not a valid input")
                except:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"not a valid input")
                    else:
                        team2_print(f"not a valid input")

            player = team[choice - 1]
            player_name = player[2].capitalize()

            if player[10] >= r1:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name}'s penalty was on target")
                else:
                    team2_print(f"{player_name}'s penalty was on target")
                sot += 1
                if not jump_to_result:
                    time.sleep(1)

                if player[10] * r2 >= r * op_player[7]:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"{player_name} has scored!!")
                    else:
                        team2_print(f"{player_name} has scored!!")
                    goals += 1
                else:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"{player_name}'s penalty was saved by {op_player[2].capitalize()}")
                    else:
                        team2_print(f"{player_name}'s penalty was saved by {op_player[2].capitalize()}")
                if not jump_to_result:
                    time.sleep(1)
            else:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name} missed")
                else:
                    team2_print(f"{player_name} missed")
                    if not jump_to_result:
                        time.sleep(1)

    return goals, sot, choice


def free_kick(team, op_team, team1, jump_to_result):

    sot = 0
    goals = 0

    r = random.random()
    r2 = random.random()
    r1 = random.randint(1, 2000)

    if team[0][2] == team1[0][2]:
        team1_print(f"It's a free kick")
    else:
        team2_print(f" It's a free kick")

    if not jump_to_result:
        time.sleep(1)

    choose_from_free = []
    for player in team:
        choose_from_free.append(player[2].capitalize())

    for op_player in op_team:
        if op_player[7] != 0:
            loop = True
            choice = 0
            while loop:
                if team[0][2] == team1[0][2]:
                    team1_print(f"Choose a player(by the corresponding number):")
                else:
                    team2_print(f"Choose a player(by the corresponding number):")
                for i, player in zip(range(1, 12), choose_from_free):
                    if team[0][2] == team1[0][2]:
                        team1_print(f'{i} : {player}')
                    else:
                        team2_print(f'{i} : {player}')
                try:
                    choice = int(input())
                    if 1 <= choice <= 11:
                        loop = False
                    else:
                        if team[0][2] == team1[0][2]:
                            team1_print(f"not a valid input")
                        else:
                            team2_print(f"not a valid input")
                except:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"not a valid input")
                    else:
                        team2_print(f"not a valid input")

            player = team[choice-1]
            player_name = player[2].capitalize()

            if player[10] >= r1:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name}'s free kick was on target")
                else:
                    team2_print(f"{player_name}'s free kick was on target")
                sot += 1
                if not jump_to_result:
                    time.sleep(1)
                if player[10] * r2 >= r * op_player[7]:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"{player_name} has scored!!")
                    else:
                        team2_print(f"{player_name} has scored!!")
                    goals += 1
                    if not jump_to_result:
                        time.sleep(1)
                else:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"{player_name}'s free kick was saved by {op_player[2].capitalize()}")
                    else:
                        team2_print(f"{player_name}'s free kick was saved by {op_player[2].capitalize()}")
                    if not jump_to_result:
                        time.sleep(1)
            else:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name} missed")
                else:
                    team2_print(f"{player_name} missed")
                if not jump_to_result:
                    time.sleep(1)

    return goals, sot


def set_piece(team, op_team, team1, jump_to_result):
    goals = 0
    pens = 0
    free_kicks = 0
    chances = 0
    sot = 0

    for op_player in op_team:
        r = random.randint(1, 350000)
        if op_player[3] == 'attacker':
            pen_free = random.randint(1, 200)
        elif op_player[3] == 'midfielder':
            pen_free = random.randint(1, 40)
        elif op_player[3] == 'defender':
            pen_free = random.randint(1, 10)
        else:
            pen_free = random.randint(1, 3)

        if op_player[9] >= r:
            if team[0][2] == team1[0][2]:
                team1_print(f'{op_player[2].capitalize()} has committed a foul in a dangerous area')
            else:
                team2_print(f'{op_player[2].capitalize()} has committed a foul in a dangerous area')
            time.sleep(1)
            if pen_free <= 2:
                pen_out = penalty(team, op_team, team1, jump_to_result)
                goals += pen_out[0]
                sot += pen_out[1]
                pens += 1
            else:
                free_out = free_kick(team, op_team, team1, jump_to_result)
                goals += free_out[0]
                sot += free_out[1]
                free_kicks += 1
            chances += 1

    return goals, pens, free_kicks, sot, chances


def goals(team1, team2, team1_def, team2_def, team1_creation, team2_creation, jump_to_result):
    team1_chance = chance_team(team1, team2_def, team1_creation, team2, team1, jump_to_result)
    team2_chance = chance_team(team2, team1_def, team2_creation, team1, team1, jump_to_result)
    team1_goals = team1_chance[0]
    team2_goals = team2_chance[0]
    team1_chances = team1_chance[1]
    team2_chances = team2_chance[1]
    team1_sot = team1_chance[2]
    team2_sot = team2_chance[2]
    team1_set_piece = set_piece(team1, team2, team1, jump_to_result)
    team2_set_piece = set_piece(team2, team1, team1, jump_to_result)
    team1_goals += team1_set_piece[0]
    team2_goals += team2_set_piece[0]
    team1_pens = team1_set_piece[1]
    team2_pens = team2_set_piece[1]
    team1_free = team1_set_piece[2]
    team2_free = team2_set_piece[2]
    team1_sot += team1_set_piece[3]
    team2_sot += team2_set_piece[3]
    team1_chances += team1_set_piece[4]
    team2_chances += team2_set_piece[4]

    return team1_goals, team2_goals, team1_chances, team2_chances, team1_sot, team2_sot, team1_pens, team2_pens, team1_free, team2_free


def check_over(mins, team1_goals, team2_goals, team1_sot, team2_sot, team1_chances, team2_chances, team1_pens, team2_pens, team1_free, team2_free, game_type, stoppage_time, first_half, jump_to_result):
    if mins == 90:
        if not jump_to_result:
            time.sleep(1)
        print(f'There will be {stoppage_time} mins of stoppage time')
        print('')
        if not jump_to_result:
            time.sleep(1)
    if mins == (90 + stoppage_time) or mins == (120 + stoppage_time) and not first_half:
        if mins == (90 + stoppage_time):
            mins = 90
            first_half = True
        if mins == (120 + stoppage_time):
            mins = 120
        stopping_time = 0
        print_stats(team1_goals, team2_goals, team1_sot, team2_sot, team1_chances, team2_chances, team1_pens, team2_pens, team1_free, team2_free)
        if game_type == 2 and team1_goals == team2_goals:
            print('press enter to continue into extra time')
            input()
        return True, mins, first_half
    else:
        return False, mins, first_half


def print_banner(mins, team1_goals, team2_goals, team1_sot, team2_sot, team1_chances, team2_chances, team1_pens, team2_pens, team1_free, team2_free, stoppage_time, first_half, jump_to_result):
    if mins in [1, 21, 31, 41, 51, 61, 71, 81]:
        suffix = 'st'
    elif mins in [2, 22, 32, 42, 52, 62, 72, 82]:
        suffix = 'nd'
    else:
        suffix = 'th'

    if mins == 45 or mins == 105:
        if not jump_to_result:
            time.sleep(1)
        print(f'There will be {stoppage_time} mins of stoppage time')
        print('')
        if not jump_to_result:
            time.sleep(1)

    print(f"{team1_goals}::{team2_goals}     --------------------{mins}{suffix} minute------------------------")

    if (mins == (45 + stoppage_time) or mins == 105) and first_half == True:
        first_half = False

        if mins == (45 + stoppage_time):
            mins = 45
        if mins == (105 + stoppage_time):
            mins = 105

        stoppage_time = 0

        print('---------------------------------------HALF TIME-------------------------------------------')
        print_stats(team1_goals, team2_goals, team1_sot, team2_sot, team1_chances, team2_chances, team1_pens, team2_pens, team1_free, team2_free)
        print('press enter to continue')
        input()

    return mins, first_half, stoppage_time


def calculate_defense(team):
    defense = 0
    for player in team:
        defense += player[6]
    defense = defense / len(team)
    return defense


def calculate_creation(team):
    creation = 0
    for player in team:
        if player[8] >= 200:
            creation += player[8]
    creation = creation / (len(team) - 1)
    return creation


def print_start(team1, team2):
    start_screen = input('do you want the dramatic enterance? ')
    if start_screen in ['yes', 'y', 'Yes', 'Y']:
        print('team1:')
        print()
        time.sleep(1)
        for player in team1:
            player_name = player[2].capitalize()
            if player[3] == 'attacker':
                print(f'{player_name} as an {player[3]}')
            else:
                print(f'{player_name} as a {player[3]}')
            time.sleep(1)
        print()
        print()
        print('team2:')
        time.sleep(1)
        print()
        for player in team2:
            player_name = player[2].capitalize()
            if player[3] == 'attacker':
                print(f'{player_name} as an {player[3]}')
            else:
                print(f'{player_name} as a {player[3]}')
            time.sleep(1)
        input('Press Enter to start match')

    else:
        print('team1:')
        print()
        for player in team1:
            player_name = player[2].capitalize()
            if player[3] == 'attacker':
                print(f'{player_name} as an {player[3]}')
            else:
                print(f'{player_name} as a {player[3]}')
        print()
        print()
        print('team2:')
        print()
        for player in team2:
            player_name = player[2].capitalize()
            if player[3] == 'attacker':
                print(f'{player_name} as an {player[3]}')
            else:
                print(f'{player_name} as a {player[3]}')
        print()
        print('Press Enter to start match')
        input()


def print_stats(team1_goals, team2_goals, team1_sot, team2_sot, team1_chances, team2_chances, team1_pens, team2_pens, team1_free, team2_free):
    print()
    print(f"{'Match Stats' : ^51}")
    print(f"{'team1' : <25}:{'team2' : >25}")
    print(f"{team1_goals : <25}:{team2_goals : >25}   :   Goals")
    print(f"{team1_sot : <25}:{team2_sot : >25}   :   Shots on Target")
    print(f"{team1_chances : <25}:{team2_chances : >25}   :   Chances")
    print(f"{team1_pens : <25}:{team2_pens : >25}   :   Pens")
    print(f"{team1_free : <25}:{team2_free : >25}   :   Free Kicks")
    print()


def set_up_teams(team1_names, team2_names):
    players = np.array(pd.read_csv('footballers.csv'))

    team1 = []
    team2 = []

    error_names = []

    for name in team1_names:
        found = False
        for row in players:
            if name == row[2]:
                team1.append(row)
                found = True
        if not found:
            error_names.append(name)

    for name in team2_names:
        found = False
        for row in players:
            if name == row[2]:
                team2.append(row)
                found = True
        if not found:
            error_names.append(name)

    if len(team1) != len(team1_names) or len(team2) != len(team2_names):
        print(f'The following players could not be found: {error_names}')

    return team1, team2


def get_game_type():
    game_input = False
    while not game_input:
        try:
            game_type = int(input('What game type is this group stage/ ligue match (1) or a knock out match (2)? '))
            if game_type in [1, 2]:
                game_input = True
            else:
                print('Not a valid input please Try again')
        except:
            print('Not a valid input please Try again')

    return game_type


def get_quick_game():
    response = False
    while not response:
        try:
            quickgame = str(input('Would you like a quick game? '))
            quickgame = quickgame.upper()
            if quickgame in ['Y', 'YES']:
                quickgame = True
                response = True
            elif quickgame in ['N', 'NO']:
                quickgame = False
                response = True
            else:
                print('Not a valid input please Try again (hint enter y, yes or n, no)')
        except:
            print('Not a valid input please Try again')
    return quickgame


def get_jump_to_result():
    response = False
    while not response:
        try:
            jump_to_result = str(input('Would you like to jump to result? '))
            jump_to_result = jump_to_result.upper()
            if jump_to_result in ['Y', 'YES']:
                jump_to_result = True
                response = True
            elif jump_to_result in ['N', 'NO']:
                jump_to_result = False
                response = True
            else:
                print('Not a valid input please Try again (hint enter y, yes or n, no)')
        except:
            print('Not a valid input please Try again')
    return jump_to_result


def penalty_extra(team, op_team, team1, chosen):
    goals = 0

    sot = 0

    r = random.random()
    r2 = random.random() * 4
    r1 = random.randint(1, 1000)

    choose_from_pen = []
    for player in team:
        choose_from_pen.append(player[2].capitalize())

    for op_player in op_team:
        if op_player[7] != 0:
            loop = True
            choice = 0
            while loop:
                if team[0][2] == team1[0][2]:
                    team1_print(f"Choose a player(by the corresponding number): you have already chosen{chosen}")
                else:
                    team2_print(f"Choose a player(by the corresponding number): you have already chosen{chosen}")

                for i, player in zip(range(1, 12), choose_from_pen):
                    if team[0][2] == team1[0][2]:
                        team1_print(f'{i} : {player}')
                    else:
                        team2_print(f'{i} : {player}')
                try:
                    choice = int(input())
                    if 1 <= choice <= 11 and choice not in chosen:
                        loop = False
                    else:
                        if team[0][2] == team1[0][2]:
                            team1_print(f"not a valid input")
                        else:
                            team2_print(f"not a valid input")
                except:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"not a valid input")
                    else:
                        team2_print(f"not a valid input")

            player = team[choice - 1]
            player_name = player[2].capitalize()

            if player[10] >= r1:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name}'s penalty was on target")
                else:
                    team2_print(f"{player_name}'s penalty was on target")
                sot += 1
                time.sleep(1)

                if player[10] * r2 >= r * op_player[7]:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"{player_name} has scored!!")
                    else:
                        team2_print(f"{player_name} has scored!!")
                    goals += 1
                else:
                    if team[0][2] == team1[0][2]:
                        team1_print(f"{player_name}'s penalty was saved by {op_player[2].capitalize()}")
                    else:
                        team2_print(f"{player_name}'s penalty was saved by {op_player[2].capitalize()}")
                time.sleep(1)
            else:
                if team[0][2] == team1[0][2]:
                    team1_print(f"{player_name} missed")
                else:
                    team2_print(f"{player_name} missed")
                    time.sleep(1)

    return goals, choice


def team_stat_set(team):

    for player in team:
        if player[3] == 'attacker':
            player[5] = player[5] * 1.4
            player[8] = player[8] * 1.1
            player[6] += player[9] * 0.2
        elif player[3] == 'defender':
            player[6] = player[6] * 2.1
            player[8] = player[8] * 0.55
            player[8] = player[8] * 0.6
        elif player[3] == 'midfielder':
            player[8] = player[8] * 1.6
            player[6] = player[6] * 0.85
            player[6] += player[9] * 0.4

    return team


def main():
    team1_goals = 0
    team2_goals = 0
    team1_chances = 0
    team2_chances = 0
    team1_sot = 0
    team2_sot = 0
    team1_pens = 0
    team2_pens = 0
    team1_free = 0
    team2_free = 0

    mins = 0
    over = False

    team1_names = ['drury', 'ohagan', 'van de sar', 'messi', 'kante', 'pele', 'kante', 'vidic', 'neymar', 'xavi', 'busquets']
    team2_names = ['alex', 'lewandowski', 'puyol', 'roberto carlos', 'iniesta', 'maldini', 'ronaldo', 'maradona', 'ibrahimovic', 'suarez', 'neuer']

    game_type = get_game_type()
    quick_game = get_quick_game()
    jump_to_result = get_jump_to_result()

    teams = set_up_teams(team1_names, team2_names)

    team1 = teams[0]
    team2 = teams[1]

    team1 = team_stat_set(team1)
    team2 = team_stat_set(team2)

    team1_def = calculate_defense(team1)
    team2_def = calculate_defense(team2)
    team1_creation = calculate_creation(team1)
    team2_creation = calculate_creation(team2)

    print_start(team1, team2)

    stoppage_time = 0

    first_half = True


    while not over:

        big_banner = print_banner(mins, team1_goals, team2_goals, team1_sot, team2_sot, team1_chances, team2_chances, team1_pens, team2_pens, team1_free, team2_free, stoppage_time,  first_half, jump_to_result)

        mins = big_banner[0]
        first_half = big_banner[1]
        stoppage_time = big_banner[2]

        print()
        min_goals = goals(team1, team2, team1_def, team2_def, team1_creation, team2_creation, jump_to_result)
        print()
        team1_goals += min_goals[0]
        team2_goals += min_goals[1]
        team1_chances += min_goals[2]
        team2_chances += min_goals[3]
        team1_sot += min_goals[4]
        team2_sot += min_goals[5]
        team1_pens += min_goals[6]
        team2_pens += min_goals[7]
        team1_free += min_goals[8]
        team2_free += min_goals[9]


        stoppage_time += min_goals[6]
        stoppage_time += min_goals[7]
        stoppage_time += min_goals[8]
        stoppage_time += min_goals[9]



        over_stuff = check_over(mins, team1_goals, team2_goals, team1_sot, team2_sot, team1_chances, team2_chances, team1_pens, team2_pens, team1_free, team2_free, game_type, stoppage_time, first_half, jump_to_result)
        over = over_stuff[0]
        mins = over_stuff[1]
        first_half = over_stuff[2]
        mins += 1

        if quick_game or jump_to_result:
            pass
        else:
            time.sleep(0.5)

    else:
        if team1_goals > team2_goals:
            print(f'team 1 wins')
        elif team2_goals > team1_goals:
            print(f'team 2 wins')
        else:
            if game_type == 2:
                over = False
                while not over:
                    big_banner = print_banner(mins, team1_goals, team2_goals, team1_sot, team2_sot, team1_chances,
                                              team2_chances, team1_pens, team2_pens, team1_free, team2_free,
                                              stoppage_time, first_half, jump_to_result)

                    mins = big_banner[0]
                    first_half = big_banner[1]
                    stoppage_time = big_banner[2]

                    print()
                    min_goals = goals(team1, team2, team1_def, team2_def, team1_creation, team2_creation, jump_to_result)
                    print()
                    team1_goals += min_goals[0]
                    team2_goals += min_goals[1]
                    team1_chances += min_goals[2]
                    team2_chances += min_goals[3]
                    team1_sot += min_goals[4]
                    team2_sot += min_goals[5]
                    team1_pens += min_goals[6]
                    team2_pens += min_goals[7]
                    team1_free += min_goals[8]
                    team2_free += min_goals[9]

                    over_stuff = check_over(mins, team1_goals, team2_goals, team1_sot, team2_sot, team1_chances,
                                            team2_chances, team1_pens, team2_pens, team1_free, team2_free, game_type,
                                            stoppage_time, first_half, jump_to_result)
                    over = over_stuff[0]
                    mins = over_stuff[1]
                    first_half = over_stuff[2]

                    mins += 1
                    if quick_game or jump_to_result:
                        pass
                    else:
                        time.sleep(0.5)

                if team1_goals > team2_goals:
                    print(f'team 1 wins')
                elif team2_goals > team1_goals:
                    print(f'team 2 wins')
                else:
                    penalties = 0
                    team1_pen_scored = 0
                    team2_pen_scored = 0
                    team1_chosen = []
                    team2_chosen = []
                    while penalties < 5 or (team1_pen_scored == team2_pen_scored):
                        print(f'Penalty : {penalties + 1}')
                        time.sleep(0.5)
                        print(f'Team1 pens scored : {team1_pen_scored}')
                        time.sleep(0.5)
                        print(f'Team2 pens scored : {team2_pen_scored}')
                        time.sleep(0.5)

                        team1_pen_extra = penalty_extra(team1, team2, team1, team1_chosen)
                        team2_pen_extra = penalty_extra(team2, team1, team1, team2_chosen)
                        team1_pen_scored += team1_pen_extra[0]
                        team2_pen_scored += team2_pen_extra[0]
                        team1_chosen.append(team1_pen_extra[1])
                        team2_chosen.append(team2_pen_extra[1])
                        if len(team1_chosen) >= 11:
                            team1_chosen = []
                        if len(team2_chosen) >= 11:
                            team2_chosen = []

                        penalties += 1
                        time.sleep(0.5)

                    print(f'Team1 pens scored : {team1_pen_scored}')
                    time.sleep(0.5)
                    print(f'Team2 pens scored : {team2_pen_scored}')
                    time.sleep(0.5)

                    if team1_pen_scored >= team2_pen_scored:
                        print('Team1 wins')
                    else:
                        print('Team2 wins')

            else:
                print('-----------------------------------draw-----------------------------------')


if __name__ == '__main__':
    main()
