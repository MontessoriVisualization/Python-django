# #input => operation => output

# num1 = float(input("Enter a number: "))
# operation = input("Enter an operation (+, -, *, /): ")

# num2 = float(input("Enter another number: "))
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero is not allowed."
# else:
#     result = "Error: Invalid operation."
# print("Result:", result)
# 2/0=Error: Division by zero is not allowed.



#task :write a program to check if a number is even or odd
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print("result:", result)
