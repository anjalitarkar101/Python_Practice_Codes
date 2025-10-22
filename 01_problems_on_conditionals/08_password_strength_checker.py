# Check if a password is "Weak" , "Medium" , or "Strong" 
# Criteria : < 6 characters - "Weak" , 6-10 chaaracters - "Medium" , > 10 characters - "Strong"

password = input("Enter your password : ")
no_of_char = len(password)

if no_of_char < 6 : 
    password_strength = "Weak"

elif no_of_char <= 10 : 
    password_strength = "Medium"  

else :
    password_strength = "Strong"

print("Your password strength is : " , password_strength)