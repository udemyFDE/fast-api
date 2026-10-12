
# these ar just normal variables
# type_of_enemy: str
# health_points: int = 10
# attack_damage: int = 1
#
# print(health_points)

# using the class object
from Enemy import *

# example
# enemy1 = Enemy()
# enemy2 = Enemy()
# enemy2.health_points = 100
#
# print(enemy1.health_points)
# print(enemy2.health_points)



zombie = Enemy()


# define typ_of_enemy
zombie.type_of_enemy = 'Zombie'
# type_of_enemy has no value in the class, so the below print statement gives error
print(f'{zombie.type_of_enemy} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')


# example of abstraction, only know/call the functions/methods
# don't know how it is done/what's inside the code
zombie.talk()
zombie.walk_forward()
zombie.attack()