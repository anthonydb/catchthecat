# Catch the Cat is a basic text game written by
# Anthony DeBarros and Nino DeBarros, built for the purpose
# of learning more about Python.

import os
import random
import time
from datetime import datetime
from .randevents import general_events, book_quotes
from .beings import Cat, Player
from .db import make_db, insert_db, results_db
from .art import splash_text, win_text, house_diagram

calories = 0
move_count = -1
entry_flag = True
food = 'x'
c = Cat()
p = Player()

# Set up the player and kitty. Player in foyer and kitty somewhere random.
def start():
    make_db()
    cls()
    print splash_text
    print """
Welcome to Catch the Cat! In this game, the objective is to
catch the cat running through the rooms. Every time you move to
a new room, the cat moves too! If you land in the same room as
the cat, you win! Enjoy!
    """
    c.name = raw_input('\nType your cat\'s name and press Enter: ')
    p.name = raw_input('\nType your name and press Enter: ')
    cls()
    print '\nHere is a diagram of the house. Take a close look!'
    print house_diagram
    raw_input('\nPress Enter to begin!')
    cls()
    foyer()

# These are the locations in the house.
def foyer():
    print '\n'
    p.location = 'foyer'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'You see stairs that lead up to a hallway ... '
        print '\nMove to (K)itchen, (S)tudy, (G)reen Living Room or (U)p stairs'
        prompt_f = raw_input('Command: ')
        if prompt_f.upper() == 'K':
            cls()
            kitchen()
        elif prompt_f.upper() == 'S':
            cls()
            study()
        elif prompt_f.upper() == 'G':
            cls()
            greenlr()
        elif prompt_f.upper() == 'U':
            cls()
            stairsup()
        else:
            incorrect_entry()
            foyer()

def kitchen():
    print '\n'
    p.location = 'kitchen'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'Mom just took two pizzas out of the oven ... '
        print '\nMove to (F)oyer, (D)ining Room, (L)iving Room, (S)tudy or (E)at pizza'
        prompt_k = raw_input('Command: ')
        if prompt_k.upper() == 'F':
            cls()
            foyer()
        elif prompt_k.upper() == 'S':
            cls()
            study()
        elif prompt_k.upper() == 'D':
            cls()
            diningroom()
        elif prompt_k.upper() == 'L':
            cls()
            livingroom()
        elif prompt_k.upper() == 'E':
            food = 'pizza'
            eat(food)
            kitchen()
        else:
            incorrect_entry()
            kitchen()

def study():
    print '\n'
    p.location = 'study'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'You see shelves lined with books ...'
        print '\nMove to (F)oyer or (K)itchen or (R)ead a book'
        prompt_st = raw_input('Command: ')
        if prompt_st.upper() == 'F':
            cls()
            foyer()
        elif prompt_st.upper() == 'K':
            cls()
            kitchen()
        elif prompt_st.upper() == 'R':
            read()
            study()
        else:
            incorrect_entry()
            study()

def greenlr():
    print '\n'
    p.location = 'green living room'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'You see a coffee table scattered with books ...'
        print '\nMove to (F)oyer or (D)ining Room'
        prompt_gl = raw_input('Command: ')
        if prompt_gl.upper() == 'F':
            cls()
            foyer()
        elif prompt_gl.upper() == 'D':
            cls()
            diningroom()
        else:
            incorrect_entry()
            greenlr()

def diningroom():
    print '\n'
    p.location = 'dining room'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'You see a table with plates set on it ...'
        print '\nMove to (K)itchen or (G)reen Living Room'
        prompt_dr = raw_input('Command: ')
        if prompt_dr.upper() == 'K':
            cls()
            kitchen()
        elif prompt_dr.upper() == 'G':
            cls()
            greenlr()
        else:
            incorrect_entry()
            diningroom()

def livingroom():
    print '\n'
    p.location = 'living room'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'There is a couch, two chairs, and a TV ...'
        print '\nMove to (K)itchen'
        prompt_lr = raw_input('Command: ')
        if prompt_lr.upper() == 'K':
            cls()
            kitchen()
        else:
            incorrect_entry()
            livingroom()

def stairsup():
    print '\n'
    p.location = 'stairs'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'The upstairs hallway leads to two rooms ...'
        print '\nMove to the (O)ffice, the (B)edroom, or back down to the (F)oyer'
        prompt_up = raw_input('Command: ')
        if prompt_up.upper() == 'O':
            cls()
            office()
        elif prompt_up.upper() == 'F':
            cls()
            foyer()
        elif prompt_up.upper() == 'B':
            cls()
            bedroom()
        else:
            incorrect_entry()
            stairsup()

def office():
    print '\n'
    p.location = 'office'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'There is a computer on a desk ...'
        print '\nMove to (S)tairs'
        prompt_up = raw_input('Command: ')
        if prompt_up.upper() == 'S':
            cls()
            stairsup()
        else:
            incorrect_entry()
            office()

def bedroom():
    print '\name'
    p.location = 'bedroom'
    move_actions()
    if catch_test() == True:
        win()
    else:
        print 'There is a bed; beside it is a large dresser ...'
        print '\nMove to (S)tairs'
        prompt_br = raw_input('Command: ')
        if prompt_br.upper() == 'S':
            cls()
            stairsup()
        else:
            incorrect_entry()
            bedroom()

# Clear the screen using appropriate system command
def cls():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

# Move that kitty! Also have something random happen!
def move_actions():
    global move_count
    global entry_flag
    move_count += 1
    print 'Move: ' + str(move_count) + '\n'
    random_event()
    p.reveal()
    if entry_flag == True:
        c.run()
    if move_count == 0 and c.location == 'foyer':
        c.run()
    c.reveal()
    print ''
    time.sleep(1)
    entry_flag = True

def incorrect_entry():
    cls()
    print '\nIncorrect entry'
    global entry_flag
    entry_flag = False

# Consume calories!
def eat(food):
    cls()
    global calories
    if food == 'pizza':
        calories = calories + 500
        print 'You have eaten %s calories!' % str(calories)
        print 'This costs 1 move'
    if calories > 1999:
        print '\nBetter slow down on the food there, big boy!'
        print 'This cost you another move.'

# Get cultured!
def read():
    cls()
    r = len(book_quotes) - 1
    num = random.randint(0,r)
    print '\n\nYou take a book off the shelf and read:\n\n'
    print '\"%s\"\n  -- %s\n\n' % (book_quotes[num]['quote'], book_quotes[num]['title'])
    print 'This costs 1 move'
    raw_input('\nPress Enter to continue!')
    cls()

# Create a 20% chance that someone will shout in the house
def random_event():
    draw_event = random.randint(1,5)
    if draw_event == 4:
        x = len(general_events) - 1
        num = random.randint(0,x)
        print '\nSomeone shouts: \"' + general_events[num] + '\"\n'

# Test whether player and kitty have arrived in the same place
def catch_test():
    if c.location == p.location:
        return True
    else:
        return False

# FTW!
def win():
    global move_count
    print '\n\nYou caught the cat in ' + str(move_count) + ' moves!'
    print win_text
    insert_db(p.name, move_count, datetime.now())
    raw_input('\nPress Enter to see a list of leaders!')
    cls()
    results_db()

# Start the game
if __name__ == "__main__":
    start()
