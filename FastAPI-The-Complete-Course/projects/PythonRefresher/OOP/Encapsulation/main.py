
# using the class object
from Enemy import *

zombie = Enemy('zombie')
zombie.__type_of_enemy = 'vampire'
# even if we try to overwrite the type_of_enemy value to vampire, the output is still zombie
# output --
# I am a zombie having 10 health points. Be prepared to fight!
# zombie moves closer to you
# zombie attacks for 1 damage


zombie.talk()
zombie.walk_forward()
zombie.attack()

