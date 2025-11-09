# Program to find the first non-repeated character in a string provided by the user

input_string = input("enter the string to find it's first non repeated character: ")

for char in input_string :
    if input_string.count(char) == 1 :
        print("first non repeated character is:", char)
        break