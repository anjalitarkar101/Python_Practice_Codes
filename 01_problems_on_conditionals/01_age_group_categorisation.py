# Classify a person's age group : Child(<13) , Teenager(13-19) , Adult(20-59) , Senior(60+)


age = input("Enter your age: ") 
age_in_int = int(age)

if age_in_int < 13 :
    age_group = "Child"

elif age_in_int < 20 :
    age_group = "Teenager"

elif age_in_int < 60 :
    age_group = "Adult"

else :
    age_group = "Senior"

print("You are categorized as:", age_group)