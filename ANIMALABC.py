from abc import ABC,abstractmethod
class Animal(ABC):


    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk and run")

class snail(Animal):
    def move(self):
        print("I can crawl")

class dog(Animal):
    def move(self):
        print("I can bark")

class lion(Animal):
    def move(self):
        print("I can roar")



R = human()
R.move()

K = snail() 
K.move()

R = dog()
R.move()

K = lion()
K.move()