# Catch the Cat is a basic text adventure game by
# Anthony DeBarros and Nino DeBarros, built for the purpose
# of learning more about Python.

import os
import random
import time
from randevents import general_events
from classes import cat

calories = 0
food = 'x'
c = cat()

def start():
    cls()
    foyer()

def cls():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

# Create a 20% chance that someone will shout in the house
def random_event():
    draw_event = random.randint(1,5)
    if draw_event == 4:
        x = len(general_events) - 1
        num = random.randint(0,x)
        print '\nSomeone shouts: \"' + general_events[num] + '\"'

def foyer():
    print '\n\nYou are in the foyer.'
    kitty_run()
    print 'You see stairs going up and various rooms. Now what?'
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
    print '\n\nYou are in the Kitchen'
    kitty_run()
    print '\nMom is here. She just took two pizzas out of the oven. Now what?'
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
        print '\nIncorrect entry'
        kitchen()

def study():
    print '\n\nYou are in the Study'
    kitty_run()
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
        print '\nIncorrect entry'
        study()    

def greenlr():
    print '\n\nYou are in the green living room'
    kitty_run()
    print '\nYou see a coffee table scattered with books...'
    print '\nMove to (F)oyer or (D)ining Room'
    prompt_gl = raw_input('Command: ')
    if prompt_gl.upper() == 'F':
        cls()
        foyer()
    if prompt_gl.upper() == 'D':
        cls()
        diningroom()
    else:
        print '\nIncorrect entry'
        greenlr()    

def diningroom():
    print '\n\nYou are in the dining room'
    kitty_run()
    print '\nYou see a table with plates placed on it...'
    print '\nMove to (K)itchen or (G)reen Living Room'
    prompt_dr = raw_input('Command: ')
    if prompt_dr.upper() == 'K':
        cls()
        kitchen()
    if prompt_dr.upper() == 'G':
        cls()
        greenlr()
    else:
        print '\nIncorrect entry'
        diningroom()    

def livingroom():
    print '\n\nYou entered the living room'
    kitty_run()
    print '\nThere is a couch, two chairs, and a TV...'
    print '\nMove to (K)itchen'
    prompt_lr = raw_input('Command: ')
    if prompt_lr.upper() == 'K':
        cls()
        kitchen()
    else:
        print '\nIncorrect entry'
        livingroom()  

def stairsup():
    print '\n\nYou are at the top of the stairs'
    kitty_run()
    print '\nYou see a hallway'
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
        print '\nIncorrect entry'
        office()  
    

def office():
    print '\n\nYou are in the office'
    kitty_run()
    print '\nThere is a computer on a desk ...'
    print '\nMove to (S)tairs'
    prompt_up = raw_input('Command: ')
    if prompt_up.upper() == 'S':
        cls()
        stairsup()
    else:
        print '\nIncorrect entry'
        office()  

def bedroom():
    print '\n\nYou come into the bedroom'
    kitty_run()
    print '\nThere is a bed; beside it is a large dresser.'
    print '\nMove to (S)tairs'
    prompt_br = raw_input('Command: ')
    if prompt_br.upper() == 'S':
        cls()
        stairsup()
    else:
        print '\nIncorrect entry'
        bedroom()  

# Move that kitty! Also have something random happen!
def kitty_run():
    c.run()
    time.sleep(1)
    random_event()    

# Consume calories!
def eat(food):
    os.system('cls')
    global calories
    if food == 'pizza':
        calories = calories + 500
        print 'You have eaten %s calories!' % str(calories)
    if calories > 1999:
        print '\nBetter slow down on the food there, big boy!'
    
start()
