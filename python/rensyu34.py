class Vehicle():
    #tire_count = 0
    def __init__(self) -> None:
        self.gasoline = 100

    def drive(self,x:int):
        self.gasoline -= x

class Bike(Vehicle):
    tire_count = 2

class Car(Vehicle):
    tire_count = 4

bike = Bike()
print(bike.tire_count)
    
car = Car()
print(car.tire_count)