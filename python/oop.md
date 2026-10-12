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

### Four Pillars of OOP(s)
1. [_Encapsulation_](#encapsulation)
2. [_Abstraction_](#abstraction)
3. [_Inheritance_](#inheritance)
4. [_Polymorphism_](#polymorphism)


#### Abstraction
* It's an interface that allows a user to turn on and off things, or do different types of functionality without understanding or needing to understand the actual functionality of what happens inside.

> eg: we can kind of think of abstraction like a flashlight. A flashlight has an on and off switch. When you turn the switch on, you expect a beam of light to shoot out of the flashlight. When the switch is off, you expect no light. Now, what's tricky about that is we don't know how the light inside the flashlight turns on and off. We just know that when the flashlight is on, we expect a beam of light.

* `definition of abstraction` -- This means to hide the implementation and only show necessary details to the user.

* `why do we want to use abstraction?`
    - This allows users to not have to understand what the functionality is behind the scenes.
    - We can create simple and reusable code.
    - Allows us for a better use Case of the DRY principle (don't repeat yourself).
    - And lastly, it enables Python objects to become more scalable in the long term.

#### Encapsulation


#### Inheritance


#### Polymorphism