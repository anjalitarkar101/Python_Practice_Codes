# Use a property decorator in the Car class to make the model property read-only.
# property decorators allow you to define methods that can be accessed like properties

##### property/attribute means variable
##### method means function inside a class
##### object means instance

class Car:                                            

    def __init__(self , brand , model):              
        self.brand = brand                         
        self.__model = model      # making model a PRIVATE ATTRIBUTE by adding double underscores(__) before model                           

    @property                     # using the @property decorator to make the model property read-only
    def model(self):              # defining a getter method to access the private property __model
        return self.__model                           


my_car = Car("Tata", "Safari")       # creating an OBJECT named mycar of the class Car 
print(my_car.model)                  # accessing the method model as a property due to the @property decorator

