# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, 
# but with different behaviours 

##### property/attribute means variable
##### method means function inside a class
##### object means instance

class Car:                                           
    def __init__(self , brand , model):               
        self._brand = brand                          
        self.model = model                           
    
    def fuel_type(self):                              # defining a METHOD named fuel_type for the class Car
        return "Petrol or Diesel"            

class ElectricCar(Car):                              
    def __init__(self, brand, model, battery_size):   
        super().__init__(brand, model)                
        self.battery_size = battery_size              

    def fuel_type(self):                              # defining a METHOD named fuel_type for the child class ElectricCar
        return "Electricity"                          # overriding the fuel_type method of the parent class Car


my_car = Car("Tata", "Safari")                               # creating an OBJECT named mycar of the parent class Car
print(my_car.fuel_type())                                    # calling the method fuel_type 

my_electric_car = ElectricCar("Tesla", "Model S", "100kWH")  # creating an OBJECT named my_electric_car of the child class ElectricCar
print(my_electric_car.fuel_type())                           # calling the method fuel_type 