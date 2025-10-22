string = input("enter the string you want to reverse: ")
reverse_string = ""

for char  in range(0 ,len(string)) :
    reverse_string = string[char] + reverse_string

print("reverse_string is:", reverse_string)