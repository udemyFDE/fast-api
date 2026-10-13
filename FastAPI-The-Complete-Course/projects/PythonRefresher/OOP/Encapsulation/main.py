
# using the class object
from Enemy import *

zombie = Enemy('zombie')
zombie.__type_of_enemy = 'vampire'
# even if we try to overwrite the type_of_enemy value to vampire, the output is still zombie



# Getters and Setters in Class object
enemy_type = zombie.get_type_of_enemy()
print(enemy_type)
zombie.set_type_of_enemy('vampire')
# set will work only if the Setter is used with dynamic attribute
# If you don't want the attribute value to be changed then comment the Setter functionality

zombie.talk()
zombie.walk_forward()
zombie.attack()

# output --
# zombie
# I am a zombie having 10 health points. Be prepared to fight!
# zombie moves closer to you
# zombie attacks for 1 damage
