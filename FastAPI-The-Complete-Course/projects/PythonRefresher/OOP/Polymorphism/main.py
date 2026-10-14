from Zombie import *
from Ogre import *
from Enemy import *

# Enemy is the parent class
# Zombies and Ogre are child classes

# this function will take the type of enemy and do talk and attack
def battle(e: Enemy):
    e.talk()    # from child class
    e.attack()  # from parent class
    # zombie.spread_disease()   # for both enemy types we get same output as it is from zombie class

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie)
battle(ogre)


