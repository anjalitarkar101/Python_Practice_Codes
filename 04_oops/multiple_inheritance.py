# Create three classes Car , Battery and Engine , and let the ElectricCar class inherit from all the three classes, 
# demonstarting multiple inheritance.

class Car:                                            # defining a CLASS named Car
    
    total_cars = 0                                    # class variable to keep track of the number of car instances created
                                  
    def __init__(self , brand , model):               # defining a constructor method __init__ using  self, brand and model as parameters and self is a telephone line to access the attributes and methods of the class
        self.__brand = brand                          # brand is an attribute(variable) of the class Car
        self.__model = model                            # model is an attribute(variable) of the class Car
        Car.total_cars += 1                           # incrementing the class variable total_cars by 1 each time a new car instance is created

    def full_name(self):                              # defining a full name method to return full name of the car
        return f"{self.__brand} {self.__model}"  
    
    def get_brand(self):                              # defining a getter method to access the private attribute __brand
        return self.__brand
    
    def fuel_type(self):                              # defining a method fuel_type for the class Car
        return "Petrol or Diesel"            

    @staticmethod                                      # defining a static method using the @staticmethod decorator
    def general_description():                       
        return "Cars are vehicles that run on roads and are used for transportation."
    
    @property                                        # using the @property decorator to make the model attribute read-only
    def model(self):                              # defining a getter method to access the private attribute __model
        return self.__model                           


class Battery:
    def battery_info(self):
        return "This car has a battery."

class Engine:
    def engine_info(self):
        return "This car has an engine."


class ElectricCar(Car , Battery , Engine):
    pass


my_electric_car = ElectricCar("Tesla", "Model S")      # creating an OBJECT named my_electric_car of the subclass ElectricCar

print(my_electric_car.battery_info())                   # calling the inherited method battery_info from Battery class
print(my_electric_car.engine_info())                    # calling the inherited method engine_info from Engine class

