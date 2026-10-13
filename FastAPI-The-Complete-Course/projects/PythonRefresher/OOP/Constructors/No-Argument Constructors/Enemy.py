class Enemy:

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    # You explicitly define __init__() without extra parameters.
    # It takes self but no extra arguments.
    # It can initialize attributes.

    def __init__(self):
        print("New enemy created with no starting values")

    # The above is no-argument constructor, can have statements or initialize attributes.
    # the initializer has a statement to print while initializing the object
    # we see this statement on the terminal when an object is instantiated using this Class object

    def talk(self):
        print(f"I am an enemy with {self.health_points} health points and can do the damage of {self.attack_damage}!")

    # OR

    # def __init__(self):
    #     self.type_of_enemy = 'zombie'
    #     self.health_points = 100
    #     # this can initialize the value and/or overwrite the value defined above
    #
    # # The above is no-argument constructor, can have statements or initialize attributes.
    # # the initializer has the values to be used while initializing the object
    # # These values will be used in the below function
    #
    # def talk(self):
    #     print(f"I am {self.type_of_enemy} with {self.health_points} health points and can do the damage of {self.attack_damage}!")



    # self here points to the class Enemy
    # def talk(self):
    #     print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    # def walk_forward(self):
    #     print(f"{self.type_of_enemy} moves closer to you")
    #
    # def attack(self):
    #     print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")