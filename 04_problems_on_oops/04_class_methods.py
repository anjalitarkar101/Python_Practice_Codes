# Add a method to display full name of the Car class

##### property/attribute means variable
##### method means function inside a class
##### object means instance
 

class Car:                                     
                                   
    def __init__(self , brand , model):        # defining a constructor METHOD __init__
        self.brand = brand                    
        self.model = model                     

    def full_name(self):                       # defining a METHOD named full_name 
        return f"{self.brand} {self.model}"   


my_car1 = Car("Toyota", "Corolla")            
print(my_car1.brand)                           
print(my_car1.model)                           
print(my_car1.full_name())                     # calling the method full_name   


my_car2 = Car("Tata", "Safari")                
print(my_car2.brand)                           
print(my_car2.model)                          
print(my_car2.full_name())                     # calling the method full_name