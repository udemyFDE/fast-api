
# these ar just normal variables
# type_of_enemy: str
# health_points: int = 10
# attack_damage: int = 1
#
# print(health_points)

# using the class object
from Enemy import *

zombie = Enemy()



# zombie.type_of_enemy = 'Zombie'
print(f'{zombie.type_of_enemy} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')


zombie.talk()
zombie.walk_forward()
zombie.attack()