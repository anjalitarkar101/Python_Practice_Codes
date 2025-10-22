num = int(input("enter the number whose factorial you want: "))
original_num = num  # Save the original number

factorial = 1

while num > 0 :
    factorial = factorial * num
    num = num - 1
    
print("factorial of %d is %d" % (original_num , factorial) )

