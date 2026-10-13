
# using the class object
from Enemy import *


# here we see warning for Enemy() like a missing attribute/parameter
# zombie = Enemy()
# In empty or no-argument constructors we don't know what the class object require as dynamic inputs, if any.

# below 2 are accepted as the missing value is only for type_of_enemy
# so the constructor will take the given value for type_of_enemy
# zombie = Enemy(type_of_enemy='zombie')
zombie = Enemy('zombie')

# if more than one parameters do not have values declared in the Class object
# then need to explicitly pass them the respective values as below
# the values can also be passed to overwrite the ones defined in Class object
# zombie = Enemy(type_of_enemy='zombie', health_points=1000)


print(f'{zombie.type_of_enemy} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')
# output --
# zombie has 10 health points and can do attack of 1
# health points and attack values are taken from Class object if not defined in this file to overwrite

zombie.talk()
zombie.walk_forward()
zombie.attack()

# Output --
# I am a zombie. Be prepared to fight!
# zombie moves closer to you
# zombie attacks for 1 damage

