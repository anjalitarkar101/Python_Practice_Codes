# Add a static method to the Car class to return general description about car
# Static method belongs to the class rather than any specific instance and can be called on the class itself.

##### property/attribute means variable
##### method means function inside a class
##### object means instance

class Car:                                                                  
                                  
    def __init__(self , brand , model):       
        self._brand = brand                      
        self.model = model                          

    @staticmethod                       # using the @staticmethod decorator
    def general_description():          # defining a STATIC METHOD general_description for the class Car
        return "Cars are vehicles that run on roads "


my_car = Car("Tata", "Safari")          # creating an OBJECT named mycar of the class Car

print(my_car.general_description())     # calling the static method general_description using the object my_car
print(Car.general_description())        # calling the static method general_description using the class Car