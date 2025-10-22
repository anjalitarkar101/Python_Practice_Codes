# Recommend a type of pet food based on the pet's species and age 
# Dog : < 2 years - Puppy food   
# Cat : > 5 years - Senior cat food 

pet_species = input("Enter your pet's species : ").strip().capitalize()

pet_age = input("Enter your pet's age in years : ")
pet_age_in_int = int(pet_age)

if pet_species == "Dog" :
    if pet_age_in_int < 2 : 
        pet_food = "Puppy food"

    else :
        pet_food = "Senior food"

if pet_species == "Cat" :
    if pet_age_in_int > 5 : 
        pet_food = "Senior cat food"

    else :
        pet_food = "Kitten  food"

    print("Recommended pet food : " , pet_food)