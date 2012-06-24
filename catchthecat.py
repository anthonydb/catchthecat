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

def start():
    os.system('cls')
    cls()
    c = cat()
    foyer()

def cls():
    os.system('cls')

def random_event():
    x = len(general_events) - 1
    num = random.randint(0,x)
    print '\nSomeone shouts: \"' + general_events[num] + '\"'

def foyer():
    print '\n\nYou are in the foyer.'
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
    time.sleep(1)
    random_event()
    time.sleep(.5)
    print '\nMom is here. She just took two pizzas out of the oven. Now what?'
    print '\nMove to (F)oyer, (D)ining Room, (L)iving Room or (E)at pizza'
    prompt_k = raw_input('Command: ')
    if prompt_k.upper() == 'F':
        cls()
        foyer()
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
    time.sleep(1)
    random_event()

def greenlr():
    print '\n\nYou are in the Green Living Room'
    time.sleep(1)
    random_event()

def stairsup():
    print '\n\nYou are at the top of the stairs'
    time.sleep(1)
    random_event()
    time.sleep(.5)

def diningroom():
    print '\n\nYou are in the dining room'
    time.sleep(1)
    random_event()

def livingroom():
    print '\n\nYou entered the living room'
    time.sleep(1)
    random_event()

def eat(food):
    os.system('cls')
    global calories
    if food == 'pizza':
        calories = calories + 500
        print 'You have eaten %s calories!' % str(calories)
    if calories > 1999:
        print '\nBetter slow down on the food there, big boy!'
    
start()
