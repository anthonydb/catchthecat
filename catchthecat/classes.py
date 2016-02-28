import random
from .randevents import locations_list, run_choices

# The kitty
class Cat(object):

    def __init__(self):
        self.name = 'Kitty'

        # Randomly place the kitty in one of the rooms
        l = len(locations_list) - 1
        self.location = locations_list[random.randint(1,l)]

    def reveal(self):
        print '%s ran to the %s' % (self.name, self.location)

    def run(self):
        choices = run_choices[self.location]
        l = len(choices) - 1
        self.location = choices[random.randint(0,l)]

class Player(object):
    def __init__(self):
        self.name = 'Player'
        self.location = 'foyer'

    def reveal(self):
        print '%s is in the %s' % (self.name, self.location)
