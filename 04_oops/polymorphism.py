# demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, 
# but with different behaviours 


class Car:                                            # defining a CLASS named Car

    def __init__(self , brand , model):               # defining a constructor method __init__ using  self, brand and model as parameters and self is a telephone line to access the attributes and methods of the class
        self.__brand = brand                          # brand is an attribute(variable) of the class Car
        self.model = model                            # model is an attribute(variable) of the class Car

    def full_name(self):                              # defining a full name method to return full name of the car
        return f"{self.__brand} {self.model}"  
    
    def get_brand(self):                              # defining a getter method to access the private attribute __brand
        return self.__brand
    
    def fuel_type(self):                              # defining a method fuel_type for the class Car
        return "Petrol or Diesel"            

class ElectricCar(Car):                               # defining a subclass named ElectricCar that inherits from the superclass Car
    def __init__(self, brand, model, battery_size):   # defining a constructor method __init__ using self, brand, model and battery_size as parameters
        super().__init__(brand, model)                # using super() to call the constructor of the superclass Car to initialize brand and model attributes
        self.battery_size = battery_size              # battery_size is an additional attribute(variable) of the subclass ElectricCar

    def fuel_type(self):                              # defining a method fuel_type for the subclass ElectricCar
        return "Electricity"                          # overriding the fuel_type method of the superclass Car


my_car = Car("Tata", "Safari")                               # creating an OBJECT named mycar of the class Car 
print(my_car.get_brand())                                    # calling the method get_brand
print(my_car.model)                                          # accessing the attribute model
print(my_car.full_name())                                    # calling the method full_name
print(my_car.fuel_type())                                    # calling the method fuel_type 


my_electric_car = ElectricCar("Tesla", "Model S", "100kWH")  # creating an OBJECT named my_electric_car of the subclass ElectricCar
print(my_electric_car.get_brand())                           # calling the inherited method get_brand
print(my_electric_car.model)                                 # accessing the inherited attribute model
print(my_electric_car.full_name())                           # calling the inherited method full_name
print(my_electric_car.battery_size)                          # accessing the additional attribute battery_size
print(my_electric_car.fuel_type())                           # calling the method fuel_type of the subclass ElectricCar