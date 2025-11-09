# Demonstrate the use of isinstance() function to check if the object named my_tesla is an instance of the ElectricCar class and the Car class.

##### property/attribute means variable
##### method means function inside a class
##### object means instance

class Car:                                                                 
                                  
    def __init__(self , brand , model):               
        self._brand = brand                          
        self._model = model                            


class ElectricCar(Car):                               
    def __init__(self, brand, model, battery_size):   
        super().__init__(brand, model)                
        self.battery_size = battery_size              


my_tesla = ElectricCar("Tesla", "Model S", "100kWH")  # creating an OBJECT named my_tesla of the child class ElectricCar

print(isinstance(my_tesla, ElectricCar))              # checking if my_tesla is an instance of the child class ElectricCar
print(isinstance(my_tesla, Car))                      # checking if my_tesla is an instance of the parent class Car