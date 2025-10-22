# Create a function that takes a variable number of arguments and returns their sum.

def sum_args(*args):      # * allows the function to accept a variable number of arguments and it is compulsory to use it
    return sum(args)        # The built-in sum() function calculates the sum of all arguments

# Example usage:
result = sum_args(1, 2, 3, 4, 5)
print(result)  