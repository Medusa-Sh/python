import random

def getRandomp():
    print("Printing random date between", 100, "and", 1000)
    randomGenerator=random.random()
    pasword=random.randint(100, 1000)
    return pasword
print("Random Password is:", getRandomp())