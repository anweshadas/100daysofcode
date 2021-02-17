#!/usr/bin/env python3

import random
import json
import os
import datetime
from colorama import Fore
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.completion.base import Completer 

class Roll:
    def __init__(self,name,defeated_by, defeats):
        self.name = name
        self.defeated_by = defeated_by 
        self.defeats = defeats

class Player:
    def __init__(self,name):
        self.name = name 
        

rolls = {}

def main():
    print(Fore.WHITE)
    log("App starting up...")
    
    load_rolls()
    show_header()
    show_leaderboard()
    player1, player2 = get_players()
    log(f"{player1.name} has logged in.")

    play_game(player1, player2)
    log("Game Over")

def show_header():
    print(Fore.LIGHTMAGENTA_EX)
    print("------------------------")
    print("Rock Paper Scissior v1")
    print("Data Structure version")
    print("------------------------")
    print(Fore.WHITE)



def show_leaderboard():
    leaders = load_leaders()
    
    # dictionaries does not have .sort. So we are converting the sorted_named into a list. sorted_named returns a list of tupples.

    sorted_leaders = list(leaders.items())
    sorted_leaders .sort(key=lambda l: l[1], reverse=True)

    # The line above can be replaced by a function and a sort function

    #def to_sort(l):
    #print(f"{l=}")
    #return l[1]

    # sorted_named.sort(key=to_sort)


    print()
    print("LEADERS: ")
    # [0:5] shows only first 5 winners
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins: ,} -- {name}")

    print()
    print("-------------------------")
    print()

    

def get_players():

    p1 = input("Player 1, what is your name?")
    player1 =  Player(p1)
    p2 = "Computer"
    player2 = Player(p2)

    return player1,player2


def play_game(player_1, player_2):
    log(f"New game starting between {player_1.name} and {player_2.name}.")

    # wins keeps the count of how many times player_1 and player_2 has won)
    wins = {player_1.name :0, player_2.name: 0}
    #taking all the keys in rolls dictionary in a list
    roll_names = list(rolls.keys())
    

    while not find_winner(wins, wins.keys()):
        roll_1 = get_roll(player_1.name,roll_names)
        roll_2 = random.choice(roll_names)
    
        if not roll_1:
            print(Fore.LIGHTRED_EX + "Try again")
            print(Fore.WHITE)
            continue
        
        
        log(f"Round: {player_1.name} roll {roll_1} and {player_2.name} rolls {roll_2}.")
        print(Fore.GREEN + f"{player_1.name} rolls {roll_1}")
        print(Fore.BLUE + f"{player_2.name} rolls {roll_2}")
        print(Fore.WHITE)
        

        winner = check_for_winning_throw(player_1, player_2, roll_1, roll_2)
        if winner is None:
            msg = "This round was a tie!"
            print(msg)
            log(msg)
                
        else:
            msg = f"{winner.name} takes the round!"
            fore = Fore.GREEN if winner == player_1 else Fore.LIGHTRED_EX
            print(fore + msg)
            log(msg)
            wins[winner.name] += 1
            
        msg = f"Score is {player_1.name} : {wins[player_1.name]} {player_2.name} : {wins[player_2.name]}."
        log(msg)
        print(Fore.RED + msg)
        print()
        print(Fore.WHITE)


    overall_winner = find_winner(wins, wins.keys())
    msg = f"{overall_winner} wins the game!"
    print(msg)
    log(msg)
    record_win(overall_winner) 
        

def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name
    
    return None


def check_for_winning_throw(player_1, player_2, roll_1, roll_2):
    
    if roll_1 == roll_2:
        return None

    roll1 = rolls.get(roll_1)
    roll2 = rolls.get(roll_2)

    if roll2.name in roll1.defeated_by:
        return player_2
    if roll2.name in roll1.defeats:
        return player_1
    
    


def get_roll(player_name, rolls):
    print(f"Available roles : {',  '.join(rolls)}")

    #for index, r in enumerate(rolls, start=1):
        #print(f"{index}.{r}")
        
    #text = input(f"{player_name} what is your roll? ")
    #selected_index = int(text) -1

    word_comp = PlayComplete()
    roll = prompt(f"{player_name}, what is your roll: ", completer=word_comp)

    if not roll or roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not valid.")
        return None
    return roll

    #if selected_index < 0 or selected_index >= len(rolls):
        #print("Sorry {player_name} {text} is out of bounds!") 
        #return None
    
    return rolls[selected_index]

def load_rolls():

    global rolls
    
    rock = Roll("rock",("paper", "air", "water"),("fire", "scissors", "sponge"))
    rolls["rock"] = rock
    paper = Roll("paper",("scissors", "fire", "sponge"),("rock", "water", "air"))
    rolls["paper"] = paper
    scissors = Roll("scissors",("fire", "rock","water"),("paper", "sponge", "air"))
    rolls["scissors"] = scissors
    fire = Roll("fire", ("rock", "water", "air"),("scissors", "sponge", "paper"))
    rolls["fire"] = fire
    sponge = Roll("sponge",("rock", "fire", "scissors"),("paper", "air", "water") )
    rolls["sponge"] = sponge
    air = Roll("air", ("paper", "sponge", "scissors"),("water", "rock", "fire"))
    rolls["air"] = air
    water = Roll("water",("air", "paper", "sponge"),("rock", "fire", "scissors"))
    rolls["water"] = water



def load_leaders():

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "leaderboard.json")

    if not os.path.exists(filename):
        return {}

    with open(filename) as fobj:
        return json.load(fobj)


def record_win(winner_name):
    print(f"called with {winner_name=}")
    leaders = load_leaders()
    
    if winner_name in leaders:
        leaders[winner_name] += 1 


    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "leaderboard.json")

    with open(filename, 'w') as fobj:
        json.dump(leaders, fobj)


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "rps.log")
    
    with open(filename, "a")as fobj:
        fobj.write(f"[{datetime.datetime.now().date().isoformat()}] ")
        fobj.write(msg)
        fobj.write("\n")

class PlayComplete(Completer):
    
    def get_completions(self, document,complete_event):
        
        global rolls
        rolls2 = list(rolls.keys())
        word = document.get_word_before_cursor()
        complete_all = not word if not word.strip() else word == '.'
        completions = []
        
        for roll in rolls2:
            if complete_all or word in roll:
                completions.append(
                    Completion(roll,
                    start_position=-len(word),
                    style="fg:white bg:darkgreen",
                    selected_style="fg:yellow bg:green"
                ))
        return completions




if __name__  == "__main__":    
    main()
