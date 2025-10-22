# Determine if an year is leap year 

year = input("Enter an year :  ")
year_in_int = int(year)

if year_in_int % 100 == 0 :                            # if given year is a century year
    if year_in_int % 400 == 0  :
        print("Given year is leap year")

    else :
        print("Given year is NOT a leap year")

else :                                                 # if given year is not a century year  
    if year_in_int % 4 == 0 :
        print("Given year is leap year")

    else :
        print("Given year is NOT a leap year")


