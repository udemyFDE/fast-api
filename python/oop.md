## OOP(s) -- Object oriented programming (system)

- It is a programming paradigm based on the concepts of objects which can contain the data and code `(or)` is a way of writing code by organizing it around objects that contain data and functions.

- In simple terms, OOP lets you represent real-world things, such as a car, a student, or a zombie in a game, in your code.

    - example: Imagine a car.
        - Data (attributes): Color, brand, speed.
        - Actions (methods): Start, stop, accelerate.

        ```
        class Car:
            def __init__(self, brand, color):
                self.brand = brand
                self.color = color

            def start(self):
                print(f"{self.brand} is starting!")


        # Create an object
        my_car = Car("Toyota", "Red")

        my_car.start()
        ```
        - Output: Toyota is starting!

        - Here is what each term means:
            - Class: A blueprint for creating objects. Example: Car.
            - Object: An instance created from a class. Example: my_car.
            - Attributes: Data belonging to an object. Example: brand and color.
            - Methods: Functions defined inside a class. Example: start().

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

-  [_quick way to remeber_](#quick-way-to-remember) and [_table comparison_](#comparison)


#### Abstraction
* Abstraction is the process of hiding implementation details and showing only the essential features to the user. In simple words, you know what something does, without needing to know how it works internally.
* Think about an ATM machine:
    - You enter your PIN and the amount.
    - The ATM gives you cash.
    - You don't need to know how the ATM verifies your PIN or communicates with the bank internally.
>This is abstraction: you use the necessary features without dealing with the internal complexity.
* It's an interface that allows a user to turn on and off things, or do different types of functionality without understanding or needing to understand the actual functionality of what happens inside.

> eg: we can kind of think of abstraction like a flashlight. A flashlight has an on and off switch. When you turn the switch on, you expect a beam of light to shoot out of the flashlight. When the switch is off, you expect no light. Now, what's tricky about that is we don't know how the light inside the flashlight turns on and off. We just know that when the flashlight is on, we expect a beam of light.


* `why do we want to use abstraction?`
    - This allows users to not have to understand what the functionality is behind the scenes.
    - We can create simple and reusable code.
    - Allows us for a better use Case of the DRY principle (don't repeat yourself).
    - And lastly, it enables Python objects to become more scalable in the long term.
    - Hides implementation details from the user.
    - Reduces complexity by exposing only essential functionality.
    - Enforces a common structure for related classes.
    - Improves maintainability when internal implementations change.


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
* It is the process of acquiring properties and methods from one Class to other Classes.
* It creates a hierarchy between classes.
* Let's understand with the below example

    Animal.py
    ```
    Class Animal

           weight: int
           color: str
           age: int
           animal_type: str

           def eat(self):
               print('Animal eating)

           def sleep(self):
               print('Animal sleeping)
    ```
    Dog.py
    ```
    from Animal import *

    Class Dog(Animal)

        # All attributes/properties of Animal

        can_shed: bool
        domestic_name: str

        def talk(self):
            print('Bark')

        def eat(self):
            print('Chews on bone')

         # All methods of Animal

    ```
    Bird.py
    ```
    from Animal import *

    Class Bird(Animal)

        # All attributes/properties of Animal

        bird_type: str

        def talk(self):
            print('Chirp')

        def fly(self):
            print('Bird begins to soar!')

         # All methods of Animal

    ```

    main.py
    ```
    from Dog import *

    dog = Dog()

    # this is from parent class
    dog.sleep()

    # this is from child class overriding the parent class
    dog.eat()

    # this is from child class
    dog.talk()

    # this will not work
    # animal = Animal()
    # animal.talk()
    # here the object is instantiated using parent class which do not have talk() functionality defined

    bird = Bird()

    # these will be from the methods in child class Bird()
    bird.talk()
    bird.fly()

    # this will not work
    # animal = Animal()
    # animal.talk()
    # animal.fly()
    # here the object is instantiated using parent class which do not have talk() and fly() functionality defined

    ```
    - Here, the `Animal` is the `Parent Class`; the `Dog` which inherits the properties of parent class is a `child class` and can also have respective attributes/properties and methods which will work only if the objects are instantiatesd using child class. If any object is instantiated using parent Class, the methods and properties of child class will not work for it.
    - The methods/properties of a parent class can be overridden by defining the same methods/properties for child class and these will work only when the object is instantiated using the child class.
    - From the example, both dog and animal have the eat functionality. Method overriding is when a child class has its own method already present in the parent class. When the child class does not have the same method, it will default to the parent class.

* `Self` vs `Super`


    | self | super |
    | --- | --- |
    | used to refer to a current object that is created or being instantiated | refered to the parent class |
    | used when there is a need to differentiate between the instance variables and parameters with the same name | used to call the parent class methods and/or constructors |
    
    - Let's see the example

    ```
    Class Person

        def __init__(self, name, age):
            self.name = name
            self.age = age

    
    Class Student(Person)

        def __init__(self, name, age, degree):
            super().__init__(name=name, age=age)
            self.degree = degree
    ```
    - student has an extra property `degree`.
    - Student uses `super` to call the person constructor which assigns the property `name` and `age`.
    - student uses `self` to reference the `degree` property, which is different from the degree parameter / argument coming in.
    - Here, the parent class `Person()` has the `name` and `age`. The child class `Student()` has additional property `degree` using `self` and used `super()` for name and age to ensure they are used from parent class.
    - `parent class` is also called as `super class` which is why it has the `super()` functionality.


#### Polymorphism
* It means to have many forms.
* In simple terms, different classes can have a method with the same name, but each class can implement that method differently.
* Changing the object at specific runtime.

* Let's see the example below by taking the Animal() Class example from Inheritance

    - suppose we have a variable zoo which is of type Animal and it is an empty list

    ```
    zoo: Animal = []
    ```
    - Now, we might have different animal types -- Dog(Animal), Bird(Animal), Lion(Animal) - which all takes in Animal

    class.py (dog.py, bird.py, lion.py)
    ```
    Class Dog(Animal)

        ** All Dog methods **
    
    Class Bird(Animal)

        ** All Bird methods **

    Class Lion(Animal)

        ** All Lion methods **
    ```
    - now, if we try to add some values by creating the object to the list

    main.py
    ```
    zoo: Animal = []

    dog = Dog()
    zoo.append(dog)
    # this will work as Dog() is of type Animal()
    # at runtime the dog will be transformed to animal to fit in the Animal list of zoo
    # same for the below

    bird = Bird()
    lion = Lion()
    
    zoo.append(bird)
    zoo.append(lion)


    dog2 = Animal()
    zoo.append(dog2)
    # this will also work as Dog() is of type Animal()
    # at runtime Animal object is created which will also fit into the list

    ```

* **What is Polymorphism?**

    class.py (Animal.py, dog.py, bird.py, lion.py)
    ```
    Class Animal()

        def talk(self):
            print('Does not make a sound') 

    Class Dog(Animal)

        def talk(self):
            print('Bark') 
    
    Class Bird(Animal)

        def talk(self):
            print('Chirp') 

    Class Lion(Animal)

        def talk(self):
            print('Roar.!!') 
    ```
    - Assuming we have some animals added to the list as per the below file
    main.py
    ```
    zoo: Animal = []

    dog = Dog()
    dog2 = Animal()
    bird = Bird()
    lion = Lion()
    
    zoo.append(dog)
    zoo.append(bird)
    zoo.append(lion)    
    zoo.append(dog2)


    for animal in zoo:
        animal.talk()


    # output:
    # Bark
    # Does not make a sound
    # Chirp
    # Roar..!
    ```
    - At polymorphism runtime, it'll change these objects into the correct objects. So it's a data type that has many forms, and it allows us to be able to change objects to fit within other things.



#### Quick way to remember:

* Abstraction: Hides complexity.
* Encapsulation: Protects data.
* Inheritance: Reuses code.
* Polymorphism: One interface, many forms.

#### Comparison

| Abstraction | Encapsulation | Inheritance | Polymorphism |
|---|---|---|---|
| Hides implementation details. | Bundles data and methods and manages access. | Allows a class to acquire properties and methods from another class. | Allows the same method or interface to behave differently in different situations. |
| Focuses on what an object does. | Focuses on controlling how internal data is accessed or changed. | Promotes code reusability. | Promotes flexibility and extensibility. |