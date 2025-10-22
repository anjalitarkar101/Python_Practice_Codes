# Modify the car class to encapuslate the brand attribute , making it private, and 
# provide a getter method for accessing the brand.

class Car:                                           # defining a CLASS named Car
                                 
    def __init__(self , brand , model):              # defining a constructor method __init__ using  self, brand and model as parameters and self is a telephone line to access the attributes and methods of the class
        self.__brand = brand                         # brand is an attribute(variable) of the class Car
        self.model = model                           # model is an attribute(variable) of the class Car

    def full_name(self):                             # defining a full name method to return full name of the car
        return f"{self.__brand} {self.model}"  
    
    def get_brand(self):                             # defining a getter method to access the private attribute __brand
        return self.__brand



my_car = Car("Toyota", "Corolla")                   # creating an OBJECT named my_car of the subclass ElectricCar
print(my_car.get_brand())                           # calling the method get_brand

