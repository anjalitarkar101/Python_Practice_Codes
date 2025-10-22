# Assign a letter grade based on a student's score : 
# A(90-100) , B(80-89) , C(70-79) , D(60-69) and F(below 60)

score = input("Enter the student's score : ")
score_in_int = int(score)

if score_in_int >= 101 :
    print("Please verify your score again !!")
    exit()

if score_in_int >= 90 :
    grade = "A"

elif score_in_int >= 80 :
    grade = "B"

elif score_in_int >= 70 :
    grade = "C"

elif score_in_int >= 60 :
    grade = "D"

else :
    grade = "F"


print(" Student grade is : " , grade)



