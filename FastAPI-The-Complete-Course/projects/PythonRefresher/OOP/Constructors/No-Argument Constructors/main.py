
# using the class object
from Enemy import *

zombie = Enemy()
# here we don't see any warning for Enemy() like a missing attribute/parameter
# in Parameter constructor it will be highlighted


# define typ_of_enemy
# zombie.type_of_enemy = 'Zombie'

zombie.talk()


# with or without value for type_of_enemy -- same output due to no-argument constructor in the Class object
# output -- using initializer with print statement
# New enemy created with no starting values
# I am an enemy with 10 health points and can do the damage of 1!

# output -- using initializer with values
# I am zombie with 100 health points and can do the damage of 1!
