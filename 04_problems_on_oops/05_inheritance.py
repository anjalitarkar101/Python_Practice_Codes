# Create a child class named ElectricCar that inherits from the parent class named Car
# Child class has an additional property named battery_size.

##### property/attribute means variable
##### method means function inside a class
##### object means instance


class Car:                       # defining a PARENT CLASS named Car                    
                                  
    def __init__(self , brand , model):             
        self.brand = brand                           
        self.model = model                           

    def full_name(self):                             
        return f"{self.brand} {self.model}"   

class ElectricCar(Car):                              # defining a CHILD CLASS named ElectricCar that inherits from the parent class named Car
    def __init__(self, brand, model, battery_size):  # defining a constructor method __init__ using self, brand, model and battery_size as parameters
        super().__init__(brand, model)               # using super() to call the constructor of the parent class Car to initialize brand and model properties
        self.battery_size = battery_size             # self.battery_size is an additional property of the child class ElectricCar


my_electric_car = ElectricCar("Tesla", "Model S", "100kWH")  # creating an OBJECT named my_electric_car of the child class ElectricCar
print(my_electric_car.brand)                                 # accessing the inherited property self.brand
print(my_electric_car.model)                                 # accessing the inherited property self.model
print(my_electric_car.full_name())                           # calling the inherited method full_name
print(my_electric_car.battery_size)                          # accessing the additional property self.battery_size