num = int(input("enter the number upto which you want sum of even numbers: "))
sum_of_even_numbers = 0 

for i in range(1 , num+1) :
    if i % 2 == 0 :
        sum_of_even_numbers = sum_of_even_numbers + i    # sum_of_even_numbers += i

print("sum_of_even_numbers is:", sum_of_even_numbers)