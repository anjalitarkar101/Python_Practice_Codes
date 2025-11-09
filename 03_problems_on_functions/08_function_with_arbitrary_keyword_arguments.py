# Create a function that takes any number of keyword arguments and prints them in the format "key: value".

def print_kwargs(**kwargs):                       # ** allows the function to accept a variable number of keyword arguments as a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
print_kwargs(name="Shubham", age=24, city="Agra")    # Passing multiple keyword arguments
