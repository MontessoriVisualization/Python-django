# if -else
#odd and even
num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

# condition using boolian
is_raining = True
if is_raining:
    print("It's raining. Don't forget to take an umbrella!")
else:
    print("It's not raining. Enjoy your day!")

#pass
is_raining = False
if is_raining:
    print("It's raining. Don't forget to take an umbrella!")
elif is_raining:
    pass # i will write the logic for this later
else:
    print("It's not raining. Enjoy your day!")

#nested if-else
#example: check if a number is positive, negative or zero if posative then check if it is even or odd
num2 = int(input("Enter a number: "))
if num2 > 0:
    print(f"{num2} is a positive number.")
    if num2 % 2 == 0:
        print(f"{num2} is an even number.")
    else:
        print(f"{num2} is an odd number.")
elif num2 < 0:
    print(f"{num2} is a negative number.")
else:
    print(f"{num2} is zero.")



day_num = int(input("Enter a day number (1-7): "))
match day_num:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("Invalid day number. Please enter a number between 1 and 7.")


#weekend and weekday
match day_num:
    case 1 | 2 | 3 | 4 | 5|6:
        print("weekday")
    case 7:
        print("weekend")


# # 2.Gym memberships are priced based on age: $25 for adults (18 and over), $15 for children. Everyone gets a $5 discount on januarry
age = int(input("Enter your age: "))
month = input("Enter the month 1-12: ")
price_adult = 25
price_child = 15
discount = 5

match month:
    case "1":
        month="january"
    case "2":
        month="february"
    case "3":   
        month="march"
    case "4":
        month="april"
    case "5":
        month="may"
    case "6":
        
        month="june"
    case "7":
        month="july"
    case "8":
        month="august"
    case "9":
        month="september"
    case "10":
        month="october"
    case "11":
        month="november"
    case "12":
        month="december"
    case _:
        print("Invalid month number. Please enter a number between 1 and 12.")
if month == "january":
    if age >= 18:
        price = price_adult - discount
        print(f"Your gym membership price is: ${price}")
    else:
        price = price_child - discount
        print(f"Your gym membership price is: ${price}")
else:
    if age >= 18:
        price = price_adult
        print(f"Your gym membership price is: ${price}")
    else:
        price = price_child
        print(f"Your gym membership price is: ${price}")
