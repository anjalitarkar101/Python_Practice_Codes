# Create a function that takes a variable number of arguments and returns their sum.

def sum_all(*args):        # * allows the function to accept a variable number of arguments as a tuple
    total = 0
    for num in args:
        total += num
    return total

## return sum(args)       # The built-in sum() function calculates the sum of all arguments

# Example usage:
result = sum_all(1, 2, 3, 4, 5)    # Passing multiple arguments
print(result)  
