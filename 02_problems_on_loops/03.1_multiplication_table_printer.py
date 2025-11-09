# Program to print multiplication table of a given number upto 10 

n = int(input("enter the number whose multiplication table you want: "))

for i in range(1 , 11) :
    value = n * i
    print(n , "x" , i , "=" , value)
