class BMW():
    def max_speed(self):
        print("BMW's max speed is 307km/h")

    def typeoffuel(self):
        print("BMW alloweds petrol or diesel")

class Ferrali():
    def max_speed(self):
        print("ferrali's max speed is 355km/h")

    def typeoffuel(self):
        print("Ferrali alloweds petrol ")

obj_BMW= BMW()
pbj_Ferrali=Ferrali()

for car in (obj_BMW, pbj_Ferrali):
    car.max_speed()
    car.typeoffuel()