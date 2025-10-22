# Create an ElectricCar class that inherits from the Car class and 
# has an additional attribute battery_size.

class Car:                                           # defining a CLASS named Car
                                  
    def __init__(self , brand , model):              # defining a constructor method __init__ using  self, brand and model as parameters and self is a telephone line to access the attributes and methods of the class
        self.brand = brand                           # brand is an attribute(variable) of the class Car
        self.model = model                           # model is an attribute(variable) of the class Car

    def full_name(self):                             # defining a full name method to return full name of the car
        return f"{self.brand} {self.model}"   

class ElectricCar(Car):                              # defining a subclass named ElectricCar that inherits from the superclass Car
    def __init__(self, brand, model, battery_size):  # defining a constructor method __init__ using self, brand, model and battery_size as parameters
        super().__init__(brand, model)               # using super() to call the constructor of the superclass Car to initialize brand and model attributes
        self.battery_size = battery_size             # battery_size is an additional attribute(variable) of the subclass ElectricCar

    

my_electric_car = ElectricCar("Tesla", "Model S", "100kWH")  # creating an OBJECT named my_electric_car of the subclass ElectricCar
print(my_electric_car.brand)                                 # accessing the inherited attribute brand
print(my_electric_car.model)                                 # accessing the inherited attribute model
print(my_electric_car.full_name())                           # calling the inherited method full_name
print(my_electric_car.battery_size)                          # accessing the additional attribute battery_size