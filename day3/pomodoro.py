#!/usr/bin/env python3

from datetime import datetime
import time 
import os
import json


# ToDo
# use it as a command line tool
# have a log file to calculate how many sessions one has done


def main():
    show_header()
    data = read_data() # it is called first because the user might want to see only the progress
    user, user_input = get_user()
    sleep_time(user_input)
    save_data(data, user_input)


def show_header():
    print("=======================")
    print("Welcome to PomFocal")
    print("=======================")

def get_user():
    user = input("What is your name?")
    print(f"Hello {user}")
    choice = ['Pomodoro', 'Long Break', 'Short Break']
    print("What do you wish? - 1. Pomodoro focused work, 2. Long Break and 3. Short Break")
    print(f"""{user} for 
    Pomodoro focused work enter : 1
    Long Break enter : 2 
    Short Break : 3 """)
    print(" ")
    user_input = input("What do you wish? ")
    return user,user_input

def sleep_time(user_input):
    now = datetime.now()
    if user_input == "1":
        time.sleep(25)
        print("Your Pomodoro session is over, it is time for a break.")
    if user_input == "2":
        time.sleep(15)
        print("Your Long Break is over, it is time for another Pomodoro session.")
    if user_input == "3":
        time.sleep(5)
        print("Your Short Break is over, it is time for another Pomodoro session.")

def read_data(): 
    # create a json file to keep the data 
    # check if the file exists if no - return None
    # if yes - read the file, write new data in it and return the changed file

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'log.json')
    
    if not os.path.exists(filename):
        return {}
    else:
        with open (filename) as fobj:
           data = json.load(fobj)
           return data

def save_data(data, user_input):
    # check if today's date exists in data, if not create dictionary with default value,0
    # increase based on user input and save the data
    
    today = datetime.now().strftime("%Y-%B-%d")
    if not data.get(today):
        current_data = {'pomodoro':0,'long_break':0,'short_break':0}
    else:
        current_data = data.get(today)
    
    # Now we have the todays information we have to increase the changes in there
    # breakpoint()

    if user_input == '1':
        current_data['pomodoro'] +=1
    if user_input == '2':
        current_data['long_break'] +=1
    if user_input == '3':
        current_data['short_break'] +=1
    data[today] = current_data

    
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'log.json')

    with open(filename,"w") as fobj:
        json.dump(data,fobj)


if __name__ == "__main__":
    main()




        

        


