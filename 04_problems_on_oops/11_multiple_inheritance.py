# Create three classes Car , Battery and Engine , and let the ElectricCar class inherit from all the three classes, 
# demonstarting multiple inheritance.

##### property/attribute means variable
##### method means function inside a class
##### object means instance

class Car:                                                                             
    def __init__(self , brand , model):               
        self.__brand = brand                          
        self.__model = model                            
       
class Battery:
    def battery_info(self):
        return "This car has a battery."

class Engine:
    def engine_info(self):
        return "This car has an engine."


class ElectricCar(Car , Battery , Engine):
    pass


my_electric_car = ElectricCar("Tesla", "Model S")      # creating an OBJECT named my_electric_car of the child class named ElectricCar

print(my_electric_car.battery_info())                  # calling the inherited method battery_info from parent class named Battery
print(my_electric_car.engine_info())                   # calling the inherited method engine_info from parent class named Engine

