import random
from randevents import locations_list, run_choices

# The kitty
class Cat(object):

    def __init__(self):
        self.name = 'Kitty'

        # Randomly place the kitty in one of the rooms
        l = len(locations_list) - 1
        self.location = locations_list[random.randint(1,l)]

    def reveal(self):
        cat_reveal_string = '%s ran to the %s'  % (self.name, self.location)
        print(cat_reveal_string)

    def run(self):
        choices = run_choices[self.location]
        l = len(choices) - 1
        self.location = choices[random.randint(0,l)]

# The player
class Player(object):
    def __init__(self):
        self.name = 'Player'
        self.location = 'foyer'

    def reveal(self):
        player_reveal_string = '%s is in the %s' % (self.name, self.location)
        print(player_reveal_string)
