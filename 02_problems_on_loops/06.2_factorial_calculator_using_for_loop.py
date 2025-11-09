# Program to calculate the factorial of a number provided by the user using for loop

num = int(input("enter the number whose factorial you want: "))
factorial = 1

for i in range(1 , num+1) :
    factorial = factorial * i     # factorial *= i 
    
print("the factorial of %d is %d" %(num , factorial))
