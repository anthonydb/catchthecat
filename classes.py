import random
from randevents import locations_list, run_choices

# The kitty
class cat(object):

    def __init__(self):
        self.name = 'Kitty'

        # Randomly place the kitty in one of the rooms
        l = len(locations_list) - 1
        self.location = locations_list[random.randint(0,l)]

    def reveal(self):
        print '%s is hiding in the %s' % (self.name, self.location)

    def run(self):
        choices = run_choices[self.location]
        l = len(choices) - 1
        self.location = choices[random.randint(0,l)]

        print '%s is in the %s' % (self.name, self.location)
