# Modify the Car class to encapsulate the brand property, making it private
# Provide a getter method for accessing the private property
# Provide a setter method to modify the private property

##### property/attribute means variable
##### method means function inside a class
##### object means instance


class Car:                                           
                                 
    def __init__(self , brand , model):              
        self.__brand = brand            # making brand a PRIVATE PROPERTY by adding double underscores(__) before brand      
        self.model = model                           
  

    def get_brand(self):                # defining a GETTER METHOD to access the private property __brand
        return self.__brand

    def set_brand(self, brand):         # defining a SETTER METHOD to modify the private property __brand
        self.__brand = brand


my_car = Car("Toyota", "Corolla")                   
print(my_car.get_brand())               # calling the getter method get_brand

my_car.set_brand("Honda")               # calling the setter method set_brand to modify the private property __brand
print(my_car.get_brand())               # calling the getter method get_brand after using setter

