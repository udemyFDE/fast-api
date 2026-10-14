from Zombie import *
from Ogre import *

zombie = Zombie(10, 1)

print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')

# these are inherited from parent class
zombie.walk_forward()
zombie.attack()
print(zombie.get_type_of_enemy())

# this one overrides the method in parent class with child class
zombie.talk()

# this is from child class, not exist in parent class
zombie.spread_disease()

ogre = Ogre(20, 3)
print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage}')


# these are inherited from parent class
ogre.walk_forward()
ogre.attack()
print(ogre.get_type_of_enemy())

# this is from child class, not exist in parent class
ogre.talk()
