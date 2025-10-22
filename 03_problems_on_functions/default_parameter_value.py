# Create a function that takes a name as a parameter and returns a greeting message. 
# If no name is provided, it should return "Hello, user!".

def greet(name="user"):
    return "  Hello , "+ name +"!  "



result = greet("Alice")
print(result)

result = greet()
print(result)