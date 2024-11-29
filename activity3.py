#animal class

from abc import ABC

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("i can walk and run")
    
class snake(animal):
    def move(self):
        print("i can crawl")

class dog(animal):
    def move(self):
        print("i can bark")

class lion(animal):
    def move(self):
        print("i can roar")

h=human()
h.move()

s=snake()
s.move()

d=dog()
d.move()

l=lion()
l.move()