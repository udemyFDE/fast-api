from Animal import *
from Bird import *
from Dog import *
from Lion import *


zoo: Animal = []

dog = Dog()
dog2 = Animal()
bird = Bird()
lion = Lion()
bird2 = Bird()
lion2 = Lion()


zoo.append(dog)
zoo.append(dog2)
zoo.append(bird)
zoo.append(lion)
zoo.append(bird2)
zoo.append(lion2)

for animal in zoo:
    animal.talk()

