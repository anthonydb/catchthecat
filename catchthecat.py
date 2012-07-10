# Catch the Cat is a basic text game written by
# Anthony DeBarros and Nino DeBarros, built for the purpose
# of learning more about Python.

import os
import random
import time
from randevents import general_events
from classes import cat, player
from art import splash_text, win_text

calories = 0
move_count = -1
food = 'x'
c = cat()
p = player()

# Set up the player and kitty. Player in foyer and kitty somewhere random.
def start():
    cls()
    print splash_text
    print 'Welcome to Catch the Cat! In this game, the objective is to'
    print 'catch the cat running through the rooms. When you land in'
    print 'the same room as the cat, you win! Enjoy!'
    raw_input('\nPress Enter to begin!')
    cls()
    foyer()

# These are the locations in the house.
def foyer():
    print '\n\n'
    p.location = 'foyer'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print 'You see stairs going up to some rooms ... '
        print '\nMove to (K)itchen, (S)tudy, (G)reen Living Room or go (U)p'
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
            cls()
            print '\nIncorrect entry'
            foyer()

def kitchen():
    print '\n\n'
    p.location = 'kitchen'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nMom just took two pizzas out of the oven ... '
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
            cls()
            print '\nIncorrect entry'
            kitchen()

def study():
    print '\n\n'
    p.location = 'study'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nYou see the shelves lined with books ...'
        print '\nMove to (F)oyer or (K)itchen'
        prompt_st = raw_input('Command: ')
        if prompt_st.upper() == 'F':
            cls()
            foyer()
        if prompt_st.upper() == 'K':
            cls()
            kitchen()
        else:
            cls()
            print '\nIncorrect entry'
            study()    

def greenlr():
    print '\n\n'
    p.location = 'green living room'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nYou see a coffee table scattered with books ...'
        print '\nMove to (F)oyer or (D)ining Room'
        prompt_gl = raw_input('Command: ')
        if prompt_gl.upper() == 'F':
            cls()
            foyer()
        if prompt_gl.upper() == 'D':
            cls()
            diningroom()
        else:
            cls()
            print '\nIncorrect entry'
            greenlr()    

def diningroom():
    print '\n\n'
    p.location = 'dining room'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nYou see a table with plates placed on it ...'
        print '\nMove to (K)itchen or (G)reen Living Room'
        prompt_dr = raw_input('Command: ')
        if prompt_dr.upper() == 'K':
            cls()
            kitchen()
        if prompt_dr.upper() == 'G':
            cls()
            greenlr()
        else:
            cls()
            print '\nIncorrect entry'
            diningroom()    

def livingroom():
    print '\n\n'
    p.location = 'living room'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nThere is a couch, two chairs, and a TV ...'
        print '\nMove to (K)itchen'
        prompt_lr = raw_input('Command: ')
        if prompt_lr.upper() == 'K':
            cls()
            kitchen()
        else:
            cls()
            print '\nIncorrect entry'
            livingroom()  

def stairsup():
    print '\n\n'
    p.location = 'stairs'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nYou see a hallway ...'
        print '\nMove to the (O)ffice, the (B)edroom, or back down to the (F)oyer'
        prompt_up = raw_input('Command: ')
        if prompt_up.upper() == 'O':
            cls()
            office()
        if prompt_up.upper() == 'F':
            cls()
            foyer()
        if prompt_up.upper() == 'B':
            cls()
            bedroom()
        else:
            cls()
            print '\nIncorrect entry'
            office()  
    
def office():
    print '\n\n'
    p.location = 'office'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nThere is a computer on a desk ...'
        print '\nMove to (S)tairs'
        prompt_up = raw_input('Command: ')
        if prompt_up.upper() == 'S':
            cls()
            stairsup()
        else:
            cls()
            print '\nIncorrect entry'
            office()  

def bedroom():
    print '\n\n'
    p.location = 'bedroom'
    move_actions()
    if catch_test() == True:
        win()    
    else:
        print '\nThere is a bed; beside it is a large dresser ...'
        print '\nMove to (S)tairs'
        prompt_br = raw_input('Command: ')
        if prompt_br.upper() == 'S':
            cls()
            stairsup()
        else:
            print '\nIncorrect entry'
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
    move_count += 1
    print '                                   Move: ' + str(move_count)
    p.reveal()
    c.run()
    c.reveal()
    time.sleep(1)
    random_event()    

# Consume calories!
def eat(food):
    cls()
    global calories
    if food == 'pizza':
        calories = calories + 500
        print 'You have eaten %s calories!' % str(calories)
    if calories > 1999:
        print '\nBetter slow down on the food there, big boy!'

# Create a 20% chance that someone will shout in the house
def random_event():
    draw_event = random.randint(1,5)
    if draw_event == 4:
        x = len(general_events) - 1
        num = random.randint(0,x)
        print '\nSomeone shouts: \"' + general_events[num] + '\"'

# Test whether player and kitty have arrived in the same place
def catch_test():
    if c.location == p.location:
        return True
    else:
        return False

# FTW!    
def win():
        print '\n\nYou caught the cat in ' + str(move_count) + ' moves!' 
        print win_text

start()
