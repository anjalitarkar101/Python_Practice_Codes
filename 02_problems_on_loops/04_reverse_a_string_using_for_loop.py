# Program to reverse a string provided by the user

input_string = input("enter the string you want to reverse: ")
reverse_string = ""

for char  in range(0 ,len(input_string)) :
    reverse_string = input_string[char] + reverse_string

print("reverse_string is:", reverse_string)