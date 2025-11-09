# Create a function that demonstrates polymorphism by performing multiplication on  
# different data types like integers, floats, strings, lists, and tuples.

##### Parameter: A variable defined in the function definition.
##### Argument: The actual value passed to the function when it is called.

def multiply(a , b):                  # a and b are parameters
    return a * b


result = multiply(3, 4)               # Using integers as arguments
print(result)

result = multiply(5.5 , 2)            # Using floats as arguments
print(result)

result = multiply("shubham" , 2)      # Using strings as arguments
print(result)

result = multiply([1, 2] , 3)         # Using list as arguments
print(result)

result = multiply((5, 6) , 2)         # Using tuple as arguments
print(result)





