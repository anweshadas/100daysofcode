#!/usr/bin/env python3

from datetime import datetime
import time


# ToDo
# take the name
# set the time for 25 minutes
# set the time for long break of 15 minutes
# set the time for short break of 5 minutes
# start the pomodoro 
# make it  

def main():
    show_header()
    user, user_input = get_user()
    sleep_time(user_input)
    pass


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


if __name__ == "__main__":
    main()



        

        


