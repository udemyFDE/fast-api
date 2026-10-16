class Enemy:

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        # double underscore (__) before type_of_enemy -- can't overwrite the value

    def get_type_of_enemy(self):
        return self.__type_of_enemy
        # print(self.__type_of_enemy)

    def set_type_of_enemy(self, type_of_enemy):
        self__type_of_enemy = type_of_enemy
        # self.__type_of_enemy = type_of_enemy
# self__type_of_enemy -- not allow to change (Static)
# self.__type_of_enemy -- can be changed

        # self here points to the class Enemy
    def talk(self):
        print(f"I am a {self.__type_of_enemy} having {self.health_points} health points. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")