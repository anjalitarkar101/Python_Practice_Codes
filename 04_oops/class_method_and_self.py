# Add a method to display full name of the car class 

class Car:                                     # defining a CLASS named Car
                                   
    def __init__(self , brand , model):        # defining a constructor method __init__ using  self, brand and model as parameters and self is a telephone line to access the attributes and methods of the class
        self.brand = brand                     # brand is an attribute(variable) of the class Car
        self.model = model                     # model is an attribute(variable) of the class Car

    def full_name(self):                       # defining a full name method 
        return f"{self.brand} {self.model}"   


my_car1 = Car("Toyota", "Corolla")             # creating an OBJECT named mycar1 of the class Car
print(my_car1.brand)                           # accessing the attribute brand 
print(my_car1.model)                           # accessing the attribute model
print(my_car1.full_name())                     # calling the method full_name   


my_car2 = Car("Tata", "Safari")                # creating another OBJECT named mycar2 of the class Car
print(my_car2.brand)                           # accessing the attribute brand
print(my_car2.model)                           # accessing the attribute model
print(my_car2.full_name())                     # calling the method full_name