number = int(input("Enter any number: "))
is_prime = True

if number > 1:
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break
else:
    is_prime = False

print(is_prime)