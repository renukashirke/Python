# Python comes with a huge library of modules for performing common tasks such as
# sending emails, working with date/time, generating random values, etc.

# Random Module

import random

random.random()  # returns a float between 0 and 1
random.randint(1, 6)  # returns an int between 1 and 6
members = ['John', 'Bob', 'Mary']
leader = random.choice(members)  # randomly picks an item
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
