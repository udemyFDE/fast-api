class Enemy:

    # You define __init__() with extra parameters to initialize an object.
    # It accepts additional arguments.s
    # Different objects can have different initial values.

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    # def talk(self):
    #     print(f"I am an enemy!")

    # self here points to the class Enemy
    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")