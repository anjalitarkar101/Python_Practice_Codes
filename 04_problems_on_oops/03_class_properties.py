# Add a class property to the Car class to keep track of the number of car instances created

##### property/attribute means variable
##### method means function inside a class
##### object means instance

class Car:                                          
    
    total_cars = 0                         # class property to keep track of the number of car instances created                   
                                  
    def __init__(self , brand , model):               
        self._brand = brand                          
        self.model = model                           
        Car.total_cars += 1                # incrementing the class property total_cars by 1 each time a new car instance is created


my_car1 = Car("Toyota", "Corolla")         # creating an OBJECT named mycar1 of the class Car
my_car2 = Car("Tata", "Safari")            # creating another OBJECT named mycar2 of the class Car
my_car3 = Car("Tata", "Safari")            # creating an OBJECT named mycar3 of the class Car 

print(Car.total_cars)                      # accessing the class property total_cars using the Car class


