num = int(input("enter the number whose factorial you want: "))
factorial = 1

for i in range(1 , num+1) :
    factorial = factorial * i
    
print("the factorial of %d is %d" %(num , factorial))
