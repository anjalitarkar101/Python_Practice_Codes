# Create a generator function that yields even numbers up to a specified limit

def even_generator(limit):
    for num in range(0, limit + 1, 2):
        yield num

# Example usage:
for even_num in even_generator(10):
    print(even_num)
    