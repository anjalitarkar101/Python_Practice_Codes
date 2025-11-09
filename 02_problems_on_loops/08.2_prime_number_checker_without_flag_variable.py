# Program to check if a number provided by the user is a prime number without using a flag variable

number = int(input("Enter any number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Given number is NOT a prime number")
            break
    else:
        print("Given number is a prime number")
else:
    print("Given number is NOT a prime number")