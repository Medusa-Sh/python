class bus:
    def __init__(self,capacity):
        self.capacity = capacity
        print("Bus created with capacity:50")
    def get_capacity(self):
        return self.capacity
bus1 = bus(50)
print("Bus capacity is:", bus1.get_capacity())