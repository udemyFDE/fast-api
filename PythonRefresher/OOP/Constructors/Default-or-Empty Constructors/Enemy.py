class Enemy:

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    # Python allows you to create an object without defining your own __init__() method.
    # The inherited initializer does not require additional arguments.

    # Python provides an initializer if we don't define
    pass

    # OR

    # if we define
    def __init__(self):
        pass

    # The above is default/empty constructor
    # the initializer only has pass which does nothing but initialize the object
    # we see nothing on the terminal when an object is instantiated using this Class object

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