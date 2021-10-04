#Oops Concept

class Cars:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def start(self):
        print(self.name + " Engine started")    

car1 = Cars("Maruti", "Red", 10000)       
car2 = Cars("BMW", "Black", 200000)

print(car1.name, car1.color, car1.price)
print(car2.name, car2.color, car2.price)

car1.start()
car2.start()