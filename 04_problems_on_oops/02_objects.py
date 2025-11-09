# Create two instances of the class named Car with properties like brand and model

##### property/attribute means variable
##### method means function inside a class
##### object means instance

class Car:                                
                                   
    def __init__(self , brand , model):    
        self.brand = brand                
        self.model = model                


my_car1 = Car("Toyota", "Corolla")         # creating an OBJECT named mycar1 of the class Car
print(my_car1.brand)                       # accessing the instance property self.brand
print(my_car1.model)                       # accessing the instance property self.model

my_car2 = Car("Tata", "Safari")            # creating another OBJECT named mycar2 of the class Car
print(my_car2.brand)                       # accessing the instance property self.brand
print(my_car2.model)                       # accessing the instance property self.model