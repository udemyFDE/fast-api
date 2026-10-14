# Child Class Zombie()
# It expects the same attributes declared in the parent constructor

from Enemy import *

class Zombie(Enemy):

    # constructor for Zombie class (child)
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie", health_points=health_points, attack_damage=attack_damage)
        # super() refers the constructor from parent class Enemy()
        # and passes the values to parent class
        # also tells the child constructor to use the parent constructor to initialize

    # passing the value for type of enemy is not required as this child class is to create zombie object
    # so the above method makes the type of enemy as zombie a default
    # def __init__(self, type_of_enemy, health_points, attack_damage):
    #     super().__init__(type_of_enemy=type_of_enemy, health_points=health_points, attack_damage=attack_damage)

    # Method overriding
    # Inherit the parent functionality but also has it's own functionality
    # own functionality takes the precedence
    def talk(self):
        print("Zombie is *Grumbling...*")

    # new method only for zombie and not for parent functionality
    def spread_disease(self):
        print("The zombie is trying to spread infection")
    