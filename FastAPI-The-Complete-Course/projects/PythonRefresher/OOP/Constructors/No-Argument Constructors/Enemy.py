class Enemy:

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    # You explicitly define __init__() without extra parameters.
    # It takes self but no extra arguments.
    # It can initialize attributes.

    def __init__(self):
        print("New enemy created with no starting values")

    def talk(self):
        print(f"I am an enemy!")

    # self here points to the class Enemy
    # def talk(self):
    #     print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    # def walk_forward(self):
    #     print(f"{self.type_of_enemy} moves closer to you")
    #
    # def attack(self):
    #     print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")