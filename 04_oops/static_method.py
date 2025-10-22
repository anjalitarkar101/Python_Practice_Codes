# Add a static method to the car class to return general description about cars

class Car:                                            # defining a CLASS named Car
    
    total_cars = 0                                    # class variable to keep track of the number of car instances created
                                  
    def __init__(self , brand , model):               # defining a constructor method __init__ using  self, brand and model as parameters and self is a telephone line to access the attributes and methods of the class
        self.__brand = brand                          # brand is an attribute(variable) of the class Car
        self.model = model                            # model is an attribute(variable) of the class Car
        Car.total_cars += 1                           # incrementing the class variable total_cars by 1 each time a new car instance is created

    def full_name(self):                              # defining a full name method to return full name of the car
        return f"{self.__brand} {self.model}"  
    
    def get_brand(self):                              # defining a getter method to access the private attribute __brand
        return self.__brand
    
    def fuel_type(self):                              # defining a method fuel_type for the class Car
        return "Petrol or Diesel"            

    @staticmethod                                      # using the @staticmethod decorator
    def general_description():                         # defining a static method general_description for the class Car
        return "Cars are vehicles that run on roads and are used for transportation."


my_car = Car("Tata", "Safari")                         # creating an OBJECT named mycar of the class Car 
print(Car.general_description())                       # calling the static method general_description using the class Car