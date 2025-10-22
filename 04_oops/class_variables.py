# Add a class variable to the car class to keep track of the number of car instances created

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




my_car1 = Car("Toyota", "Corolla")         # creating an OBJECT named mycar1 of the class Car

my_car2 = Car("Tata", "Safari")            # creating another OBJECT named mycar2 of the class Car

my_car3 = Car("Tata", "Safari")            # creating an OBJECT named mycar3 of the class Car 


print(Car.total_cars)                      # accessing the class variable total_cars using the class name Car


