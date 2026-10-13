
# using the class object
from Enemy import *


# here we see warning for Enemy() like a missing attribute/parameter
# zombie = Enemy()
# In empty or no-argument constructors we don't know what the class object require as dynamic inputs, if any.

zombie = Enemy(type_of_enemy='zombie')


# define typ_of_enemy
# zombie.type_of_enemy = 'Zombie'

zombie.talk()
zombie.walk_forward()
zombie.attack()

# Output --
# I am a zombie. Be prepared to fight!
# zombie moves closer to you
# zombie attacks for 1 damage

