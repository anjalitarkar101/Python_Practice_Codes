# Determine if a fruit is ripe , overripe , or unripe based on its color 
# For Example >> Banana : Green-Unripe , Yellow-Ripe , Brown-Overripe

fruit_name = input("Enter the fruit name : ").strip().capitalize()
fruit_color = input("Enter the fruit color : ").strip().capitalize()

if fruit_name == "Banana" : 
    if fruit_color == "Green" :
        ripeness = "Unripe"

    elif fruit_color == "Yellow" :
        ripeness = "Ripe"

    elif fruit_color == "Brown" :
        ripeness = "Overripe"

print("Given fruit is : " , ripeness)

