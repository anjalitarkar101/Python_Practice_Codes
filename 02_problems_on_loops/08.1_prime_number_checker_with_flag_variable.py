# Program to check if a number provided by the user is a prime number using a flag variable

number = int(input("Enter any number: "))
is_prime = True

if number > 1:
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
else:
    is_prime = False

print(is_prime)