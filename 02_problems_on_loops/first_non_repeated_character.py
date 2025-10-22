string = input("enter the string to find it's first non repeated character: ")

for char in string :
    if string.count(char) == 1 :
        print("first non repeated character is:", char)
        break