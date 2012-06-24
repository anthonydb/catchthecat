# The kitty

class cat(object):

    def __init__(self):
        self.name = 'Kitty'
        self.location = 'foyer'
        print '%s is in the %s' % (self.name, self.location)

    def run(self):
        self.location = 'kitchen'
        print '%s is in the %s' % (self.name, self.location)

