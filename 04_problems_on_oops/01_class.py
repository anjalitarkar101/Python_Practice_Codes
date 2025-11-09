# Create a class named Car with properties like brand and model

##### property/attribute means variable
##### method means function inside a class

class Car:                                # defining a CLASS named Car
                                   
    def __init__(self , brand , model):   # defining a constructor method __init__ using  self, brand and model as parameters and self is a telephone line to access the attributes and methods of the class
        self.brand = brand                # self.brand is an instance property and brand is a parameter(input)
        self.model = model                # self.model is an instance property and model is a parameter(input)

