# Choose a mode of transportation based on the distance 
# <3 Km - Walk , 3-15 Km - Bike , >15 Km - Car

distance = input("Enter the distance to be covered : ")
distance_in_int = int(distance)

if distance_in_int < 3 :
    mode_of_transportation = "Walk"

elif distance_in_int <= 15 :
    mode_of_transportation = "Bike"

else:
    mode_of_transportation = "Car"

print(" Your recommended mode of transportation as per the distance to be covered : " , mode_of_transportation)