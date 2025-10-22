list_of_numbers = input("enter the list of numbers: ").split()
count_of_positive_numbers = 0

for i in list_of_numbers :
    if int(i) > 0 :
        count_of_positive_numbers = count_of_positive_numbers + 1  
        # count_of_positive_numbers += 1   

print("count_of_positive_numbers is:", count_of_positive_numbers)