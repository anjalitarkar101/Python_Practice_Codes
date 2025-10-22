while True :
    num = int(input("enter a number between 1 to 10: "))
    if num >= 1 and num <= 10 :        # if 1<= num <= 10 :  (this is also correct)
        print("valid input")
        break
    else :
        print("invalid input, please try again")