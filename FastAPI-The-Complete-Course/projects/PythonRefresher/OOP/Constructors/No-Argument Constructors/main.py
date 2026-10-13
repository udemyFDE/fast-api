
# using the class object
from Enemy import *

zombie = Enemy()
# here we don't see any warning for Enemy() like a missing attribute/parameter
# in Parameter constructor it will be highlighted


# define typ_of_enemy
# zombie.type_of_enemy = 'Zombie'

zombie.talk()


# with or without value for typ_of_enemy -- same output due to no-argument constructor in the Class object
# output --
# New enemy created with no starting values (from no-argument constructor)
# I am an enemy!
