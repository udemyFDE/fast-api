# Child Class Ogre()
# It expects the same attributes declared in the parent constructor

from Enemy import *

class Ogre(Enemy):

    # constructor for Ogre class (child)
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_points, attack_damage=attack_damage)
        # super() refers the constructor from parent class Enemy()
        # and passes the values to parent class
        # also tells the child constructor to use the parent constructor to initialize

    # passing the value for type of enemy is not required as this child class is to create ogre object
    # so the above method makes the type of enemy as ogre a default
    # def __init__(self, type_of_enemy, health_points, attack_damage):
    #     super().__init__(type_of_enemy=type_of_enemy, health_points=health_points, attack_damage=attack_damage)


    # Method overriding
    def talk(self):
        print("Ogre is slamming hands all around!")
    