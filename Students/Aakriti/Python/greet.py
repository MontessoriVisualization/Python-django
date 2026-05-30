# Create a function that greets users, but if no name is provided, it greets "Guest".

def greeting(name="Guest"):
    name=name.strip() or "Guest"
    print("Hello, " + name + "! Welcome to the Python programming course.")

user_name=input("Enter your name: ")
greeting(user_name)