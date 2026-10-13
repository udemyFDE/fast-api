## OOP(s) -- Object oriented programming (system)

- It is a programming paradigm based on the concepts of objects which can contain the data and code

- Benefits:
    * Scalability
    * Efficiency
    * Reusability


### What are objects?

- Objects are all around (eg: trees, houses, dogs etc.)
    - the example objects can be defined in 2 ways
        - Behaviour -- what the object does
            - of dog -- bark, eat, drink, sleep, walk, run..
        - State -- what the object is
            - of dog -- 4 legs, 2 ears, Goldendoodle, 5 year old, brown
    - So, if we have the variables/inputs declared for state of the dog as below example, cannot be said dog as object
    - example:
    ```    
    legs: int = 4
    ears: int = 2
    type: str = Goldendoodle
    age: int = 5
    color: str = Brown
    ```

    - To have the dog as an object
    - example file: dog.py
    ```
    class Dog:
           legs: int = 4
           ears: int = 2
           type: str = Goldendoodle
           age: int = 5
           color: str = Brown
    ```
    - now, we can create another file `main.py` and import everything from dog.py. We can instantiate (creating an object from a class) a new object
    ```
    from Dog import * 

    # Dog() is the class defined in dog.py
    dog = Dog()

    dog.legs
    dog.ears
    dog.type
    dog.age
    do.color

    # each of these have values that we called inside dog.py
    ```
    - the dog.py has static info which cannot be changed... futher in the course we deal with creating multiple opbects


### Constructors
- A special method that runs automatically when you create an object from a class. It is used to initialize the object's data.
- Used to create and initialize an object of a class with or without starting values
- In the below example-files, Enemy() is a class that has some variables with values but type_of_enemy has no value and has to be passed from main.py
- Enemy() is an example of calling a `Constructor`. We are not passing anything into the parameters in this example

Main.py
```
from Enemy import *

zombie = Enemy()

zombie.type_of_enemy = 'Zombie'

zombie.talk()
zombie.walk_forward()
zombie.attack()
```

Enemy.py
```
class Enemy:

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")
```
- 3 different type of Constructors that we can use in python

    - _default / empty constructors_
        - Python provides an initializer if you don't define __init__() yourself.
    - _no argument constructors_
        - You define __init__() without extra parameters. We don't pass anything into the constructors, but when the object is instantiated, we want some kind of functionality to happen.
    - _parameter constructors_
        - You define __init__() with extra parameters to initialize an object. passing stuff into that object when it gets instantiated.

- Using constructors can help to have less code and create/instantiate multiple objects using the same Class object

- The constructor (especially the parameter constructor) allows to pass the values but also to overwrite the values. If do not want to allow the overwrite, can be fixed using [_encapsulation_](#encapsulation)

### Four Pillars of OOP(s)
1. [_Encapsulation_](#encapsulation)
2. [_Abstraction_](#abstraction)
3. [_Inheritance_](#inheritance)
4. [_Polymorphism_](#polymorphism)


#### Abstraction
* Abstraction is the process of hiding implementation details and showing only the essential features to the user. In simple words, you know what something does, without needing to know how it works internally.
* Think about an ATM machine:
    - You enter your PIN and the amount.
    - The ATM gives you cash.
    - You don't need to know how the ATM verifies your PIN or communicates with the bank internally.
>This is abstraction: you use the necessary features without dealing with the internal complexity.
* It's an interface that allows a user to turn on and off things, or do different types of functionality without understanding or needing to understand the actual functionality of what happens inside.

> eg: we can kind of think of abstraction like a flashlight. A flashlight has an on and off switch. When you turn the switch on, you expect a beam of light to shoot out of the flashlight. When the switch is off, you expect no light. Now, what's tricky about that is we don't know how the light inside the flashlight turns on and off. We just know that when the flashlight is on, we expect a beam of light.

* `definition of abstraction` -- This means to hide the implementation and only show necessary details to the user.

* `why do we want to use abstraction?`
    - This allows users to not have to understand what the functionality is behind the scenes.
    - We can create simple and reusable code.
    - Allows us for a better use Case of the DRY principle (don't repeat yourself).
    - And lastly, it enables Python objects to become more scalable in the long term.


#### Encapsulation
* Encapsulation is the process of bundling data (variables) and methods (functions) into a single class and controlling access to that data.
* In simple words, encapsulation protects an object's data from being changed directly in unintended ways.
* Think of a bank account:
    - You have a bank balance.
    - You can deposit or withdraw money through authorized operations.
    - You shouldn't be able to change the balance arbitrarily without following the rules.

* Let's see through the below example
    Enemy.py
    ```
    class Enemy:

        def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
            self.type_of_enemy = type_of_enemy
            self.health_points = health_points
            self.attack_damage = attack_damage

        def talk(self):
            print(f"I am an enemy!")
    ```
    main.py
    ```
    # using the class object
    from Enemy import *

    zombie = Enemy('zombie')

    zombie.type_of_enemy = 'vampire'
    zombie.health_points = 100
    ```
    - Here, the values are initialized when an object is instantiated using the Enemy() Class object. But we can overwrite these values by simply declaring in main.py. So the attributes under the constructor in Enemy() are kind of public meaning they can be changed.
    - Enemy() is passed with 'zombie' but in the next line it is being chnaged to 'vampire'. And we know the vampire is not the kind of enemy object that we want to create. So, to prevent the type_of_enemy to be changed after the object is instantiated these public attributes should be made private. This can be done using `double underscore (__)` before the variable.

* Let's see the it in the below example
    Enemy.py
    ```
    class Enemy:

        def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
            self.__type_of_enemy = type_of_enemy
            self.health_points = health_points
            self.attack_damage = attack_damage

        def talk(self):
            print(f"I am an enemy!")
    ```
    - Here, we can see `double underscore (__)` before the `type_of_enemy` in `self.__type_of_enemy`.

* Now, after using the `double underscore (__)` and still we need to change something or to get the value, that's where the `encapsulation` comes into play.

* Let's see the `encapsulation` in below example
    Enemy.py
    ```
    class Enemy:

        def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
            self.__type_of_enemy = type_of_enemy
            self.health_points = health_points
            self.attack_damage = attack_damage

        def get_type_of_enemy(self):
            return self.__type_of_enemy

        def set_type_of_enemy(self, type_of_enemy):
            self__type_of_enemy = type_of_enemy        

        def talk(self):
            print(f"I am an enemy!")
    ```
    - we can see get and set for type_of_enemy which are called `getters` and `setters` in `encapsulation`. function for get is to return the value for type_of_enemy and set is to actually set the value.
    - We have no issues with get functionality but the set has the same issue of overwriting the value. So, to prohibit from overwriting do not use the `setters`

    main.py
    ```
    from Enemy import *

    zombie = Enemy('zombie')
    zombie.__type_of_enemy = 'vampire'

    zombie.get_type_of_enemy()

    zombie.talk()
    zombie.walk_forward()
    zombie.attack()
    ```
    - So, now the `zombie.__type_of_enemy = 'vampire'` will not work, instead we use the `getter` function itself. Everything will work inside our application and we're using encapsulation. We bundled the data away from the interface and it's behind scenes in the class, completely private.

* `why do we want to use encapsulation?`
    - helps keep related fields and methods together.
    - It makes our code cleaner and easier to read.
    - It provides more flexibility to our code.
    - It provides more reusability within our code.
    - And it hides values that a coder does not need to be able to either change or be able to see, and we have it completely encapsulated behind scenes.
    - Protects data from accidental modification.
    - Allows validation before changing values.
    - Keeps related data and methods organized.
    - Makes code easier to maintain.

#### Inheritance


#### Polymorphism