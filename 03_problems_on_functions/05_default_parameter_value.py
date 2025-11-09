# Create a function that takes a name as a parameter and returns a greeting message. 
# If no name is provided, it should return "Hello, user!".

##### Parameter: A variable defined in the function definition.
##### Argument: The actual value passed to the function when it is called.

def greet(name="user"):                  # name is a parameter with a default value "user"
    return "  Hello , "+ name +"!  "



result = greet("Alice")                  # "Alice" is an argument
print(result)

result = greet()                         # No argument provided, uses default value
print(result)