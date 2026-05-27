# Create a function that greets users, but if no name is provided, it greets "Guest".
# 


def greet(name="Guest"):
    print("Hello, " + name + "! Welcome to the Python programming course.")
user_name = input("Enter your name: ")

greet(user_name)
greet()

# 2.Write a function student_marks(math, science) that returns:

# total marks
# average marks

def student_marks(math, science):
    total_marks = math + science
    average_marks = total_marks / 2
    return total_marks, average_marks
print(student_marks(85, 90))

total, average = student_marks(40, 90)

print(f"Total marks: {total}, Average marks: {average}")

# 3.polimerfism
print(user_name*3)


# 4. Function with *args
# Write a function student_marks multiple subjects that returns:

# # total marks
# # average marks
def student_marks(*args):
    total_marks = sum(args)
    average_marks = total_marks / len(args)
    return total_marks, average_marks

print(student_marks(85, 90, 80, 95))

# Function with **kwargs
# Write a function student(**details) that prints all key-value pairs.

def student(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
student(name="Alice", age=22, grade="A", major="Computer Science")

#10. Recursive Function
#factorial of a number 5*4*3*2*1
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))




# hw:Create a function square(num) that returns the square of a number.
#Write a function circle(radius) that returns:
# area
# circumference
# Create a function that finds the largest number using *args
#Create a function that accepts product details using **kwargs name ,price and quantity and prints them in a formatted way.

