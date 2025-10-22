# Demonstrate the use of isinstance() function to check if the object named my_tesla is an instance of the ElectricCar class and the Car class.

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
    

class ElectricCar(Car):                               # defining a subclass named ElectricCar that inherits from the superclass Car
    def __init__(self, brand, model, battery_size):   # defining a constructor method __init__ using self, brand, model and battery_size as parameters
        super().__init__(brand, model)                # using super() to call the constructor of the superclass Car to initialize brand and model attributes
        self.battery_size = battery_size              # battery_size is an additional attribute(variable) of the subclass ElectricCar

    def fuel_type(self):                              # defining a method fuel_type for the subclass ElectricCar
        return "Electricity"                          # overriding the fuel_type method of the superclass Car



my_tesla = ElectricCar("Tesla", "Model S", "100kWH")  # creating an OBJECT named my_tesla of the subclass ElectricCar

print(isinstance(my_tesla, ElectricCar))              # checking if my_tesla is an instance of the ElectricCar class
print(isinstance(my_tesla, Car))                      # checking if my_tesla is an instance of the Car class