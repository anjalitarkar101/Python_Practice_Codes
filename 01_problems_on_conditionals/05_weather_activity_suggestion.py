# Suggest an activity based on the weather 
# Sunny-Go for a walk , Rainy-Read a book , Snowy - Build a snowman 

weather = input("Enter the weather condition :").strip().capitalize()

if weather == "Sunny" :
    activity = "Go for a walk"

elif weather == "Rainy" :
    activity = "Read a book"

elif weather == "Snowy" :
    activity = "Build a snowman"

print(" The activity you should go for : " , activity)