from time import sleep
from sys import exit

pattern = []
pause = 1
rounds = 3

def breathe(pattern):
    stage = 0
    for i in range(len(pattern)):
        if stage == 0:
            stage += 1
            if pattern[i] != 0:
                print("Breathe in")
                sleep(pause)
                for i in range(1, pattern[i]):
                    print(i+1)
                    sleep(pause)
        elif stage == 1:
            stage += 1
            if pattern[i] != 0:
                print("Hold")
                sleep(pause)
                for i in range(1, pattern[i]):
                    print(i+1)
                    sleep(pause)
        elif stage == 2:
            stage += 1
            if pattern[i] != 0:
                print("Breathe Out")
                sleep(pause)
                for i in range(1, pattern[i]):
                    print(i+1)
                    sleep(pause)
        elif stage == 3:
            stage += 1
            if pattern[i] != 0:
                print("Hold")
                sleep(pause)
                for i in range(1, pattern[i]):
                    print(i+1)
                    sleep(pause)
        else:
            print("error")

def round(rounds, pattern):
    for i in range(rounds):
        breathe(pattern)

def custom_pattern():
    pattern = []
    breath_in = int(input("How many counts for the breath in? Enter 1-10  "))
    pattern.append(breath_in)
    in_hold = int(input("How many counts for the first hold? Enter 0-10 (0 = no hold)  "))
    pattern.append(in_hold)
    breath_out = int(input("How many counts for the breath out? Enter 1-10  "))
    pattern.append(breath_out)
    out_hold = int(input("How many counts for the second hold? Enter 0-10 (0 for no hold)  "))
    pattern.append(out_hold)
    return pattern


def choose():
    print("""
    Which breathing pattern would you like to use?

    1. Relax - 4 counts in, 7 counts hold, 8 counts out
    2. Box - 4 counts in, 4 counts hold, 4 counts out, 4 counts hold
    3. Energize - 6 counts in, 2 counts out
    4. DIY - Enter your own pattern (coming soon)
    """)
    pattern_choice = int(input("What'll it be? Pick 1-4  "))
    if pattern_choice == 1:
        pattern = [4, 7, 8, 0]
    elif pattern_choice == 2:
        pattern = [4, 4, 4, 4,]
    elif pattern_choice == 3:
        pattern = [6, 0, 2, 0]
    elif pattern_choice == 4:
        pattern = custom_pattern()
    else:
        print("We can't do that pattern yet. Soon!")
        choose()
    sleep(pause)
    rounds = int(input("How many rounds would you like to breathe? Enter 1-10  "))
    sleep(pause)
    input("Ready? Press enter to start ")
    round(rounds, pattern)

def start():
    """Welcomes the user and explains how to use the app."""
    print("""
    Welcome to this Python breathing exercise.

    Pick a breathing style, how long
    you want to go, then simply breathe along
    with the counter on the screen.
    """)
    name = input("What's your name?  ")
    print("\nLet's breathe together, {}.".format(name))
    choose()

start()
# TODO: WHen the breathing pattern is done, ask if they'd like to do another
