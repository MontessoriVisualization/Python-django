# Count how many numbers between 1 and N are divisible by 3
# 
# 
# Check if a string is a palindrome
# Find the first repeating character in a string
# Generate the Fibonacci series up to N terms
# Check if two strings are anagrams
# Find the largest and smallest number in a list without using max() or min()
# Build a simple calculator using loops and conditionals

# num= int(input("Enter a number: "))
# count=0
# for x in range(1,num + 1):#this means 
#     if x % 3 ==0:
#         count+=1
# print(f"There are {count} numbers between 1 and {num} that are divisible by 3.")

# # 2 Find the sum of all odd numbers from 1 to 100

# sum=0
# for x in range(1,101):
#     if x % 2 != 0:
#         sum+=x
# print(f"The sum of all odd numbers from 1 to 100 is: {sum}")

# #3 Print the multiplication table of a number in reverse order
# num1 = int(input("Enter a number: "))
# for x in range(10,-1,-1):
#     print(f"{num1} x {x} = {num1 * x}")

#5 Find the first repeating character in a string
# string = input("Enter a string: ")
# repeating_char = []#"s","a","u","g"
# for x in string:
#     if x in repeating_char:
#         print(f"the first repeating character in the string is: {x}")
#         break
#     else:
#         repeating_char.append(x)
# else:
#     print("No repeating character found.")

# print(repeating_char)

#4 palandrome
# string1 = input("Enter a string: ")
# reveed_string = string1[::-1]
# if string1 == reveed_string:
#     print(f"{string1} is a palindrome.")
# else:
#     print(f"{string1} is not a palindrome.")

#anogarm
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# print(sorted(string1))
# print(sorted(string2))
# if sorted(string1) == sorted(string2):
#     print(f"{string1} and {string2} are anagrams.")
# else:
#     print(f"{string1} and {string2} are not anagrams.")

# Count the frequency of each element in a list
# list1 = [1, 2, 3, 4, 5, 1]
# frequency = {}
# for x in list1:
#     if x in frequency:
#         frequency[x] += 1
#     else:
#         frequency[x] = 1
# print(frequency)

#calculator
while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            continue
    else:
        print("Invalid operator. Please try again.")
        continue
    
    print(f"The result of {num1} {operator} {num2} is: {result}")
    
    cont = input("Do you want to perform another calculation? (yes/no): ")
    if cont.lower() == "no":
        break
    else:
        continue