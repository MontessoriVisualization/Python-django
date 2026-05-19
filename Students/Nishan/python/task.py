#1.can vote or cannot vote
print("Enter your age:")
age = int(input())
if age >= 18:
    print("You can vote.")
else:    
    print("You cannot vote.")
    #Gym memberships are priced based on age: $25 for adults (18 and over), $15 for children. Everyone gets a $5 discount on januarry

print("Enter your age:")
age = int(input())
if age >= 18:
    price = 25 - 5
    print(f"Your gym membership price is: ${price}")
else:
    price = 15 - 5
    print(f"Your gym membership price is: ${price}")

#3.grade calculator loop + conditional statements
print("Enter your score:")
score = int(input())
if score >= 90:
    print("Your grade is: A")
elif score >= 80:
    print("Your grade is: B")   
elif score >= 70:
    print("Your grade is: C")
elif score >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

    #4.password strength checker (8 characters, 1 uppercase, 1 lowercase, 1 number, 1 special character)
import re
print("Enter your password:")
password = input()  
if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'[0-9]', password) and
    re.search(r'[@$!%*?&]', password)):
    print("Your password is strong.")
else:
    print("Your password is not strong.")   