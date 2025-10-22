# Movie tickets are priced based on age : $12 for adults(18 and above) , $8 for children. 

age = input("Enter your age : ")
age_in_int = int(age)

if age_in_int >= 18 : 
     price = 12 

else : 
      price = 8 

print(" Movie ticket price (in $) for you will be :" , price)
    