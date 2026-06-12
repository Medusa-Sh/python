class dogs:
    species = "Doggy"
    def __init__(self,name,age):
        self.name=name
        self.age=age

pochi=dogs("Pochi",3)
ben=dogs("Ben",1)
print("Pochi is a {}".format(pochi.__class__.species))
print("Ben is also a {}".format(ben.__class__.species))
print("{} is {} years old".format(pochi.name,pochi.age))
print("{} is {} years old".format(ben.name,ben.age))    