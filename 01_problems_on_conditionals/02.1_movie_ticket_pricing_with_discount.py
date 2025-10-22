# Movie tickets are priced based on age : $12 for adults(18 and above) , $8 for children. 
# Everyone gets a $2 discount on Wednesday 

day = input("Enter the day : ").strip().capitalize()

age = input("Enter your age : ")
age_in_int = int(age)

if day != "Wednesday" :
    if age_in_int >= 18 : 
     price = 12 

    else : 
      price = 8 

else :
    if age_in_int > 17 : 
     price = 10 

    else : 
      price = 6 


print(" Movie ticket price (in $) for you will be :" , price)
    