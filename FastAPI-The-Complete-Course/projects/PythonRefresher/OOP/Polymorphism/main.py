from Zombie import *
from Ogre import *
from Enemy import *

# Enemy is the parent class
# Zombies and Ogre are child classes

# this function will take the type of enemy and do talk and attack
def battle(e: Enemy):
    e.talk()    # from child class
    e.attack()  # from parent class
    zombie.spread_disease()   # called for both enemy types we get same output as it is from zombie class

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie)
battle(ogre)


# OR

# def battle(e1: Enemy, e2: Enemy):
#     e1.talk()    # from child class
#     e1.attack()  # from parent class
#     e2.talk()    # from child class
#     e2.attack()  # from parent class
#     # zombie.spread_disease()   # e1 and e2 are different enemies, called only once
#
# zombie = Zombie(10, 1)
# ogre = Ogre(20, 3)
#
# battle(zombie, ogre)


