num1 = float(input("Enter the first number: "))

choice = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if choice == '+':
    result = num1 + num2
elif choice == '-':
    result = num1 - num2

elif choice == '*':
    result = num1 * num2
elif choice == '/':
    result = num1 / num2

print("The result is:", result)
