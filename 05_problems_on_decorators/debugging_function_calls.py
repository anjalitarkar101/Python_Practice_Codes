# Create a decorator to print the function name and the values of its arguments each time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper     # return the definition of wrapper function

@debug
def hello():
    print("Hello !")

@debug
def greet(name , greeting  =  " Hello "):
    print(f"{greeting}, {name}!")

# Testing the decorator
hello()
greet("Alice" , greeting = "Hi")
