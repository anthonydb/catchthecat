import random

# The kitty

class cat(object):

    def __init__(self):
        self.name = 'Kitty'

        # Where oh where is kitty hiding?
        locations_list = ['foyer', 'study', 'kitchen', 
            'living room', 'dining room', 'stairs', 
            'green living room', 'stairs', 'office', 'bedroom']

        # Randomly place the kitty in one of the rooms
        l = len(locations_list) - 1
        self.location = locations_list[random.randint(0,l)]
        print '%s is hiding in the %s' % (self.name, self.location)

    def run(self):
        self.location = 'kitchen'
        print '%s is in the %s' % (self.name, self.location)

