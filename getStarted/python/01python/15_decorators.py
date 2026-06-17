# Write a decorator that prints Start before a function runs and End after it finishes. Apply it to a function that prints your name.


def my_decorator(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

@my_decorator
def my_function():
    print("My name is John Doe.")

my_function()


# Create a decorator that counts how many times a function is called. Use it on a function that adds two numbers and call it three times.

def count_calls(func):
    def wrapper(*args):
        wrapper.calls += 1
        func(*args)
        print(f"{func.__name__} has been called {wrapper.calls} times.")
    wrapper.calls = 0
    return wrapper

@count_calls
def add(a,b):
    print(a + b)

add(2, 3)
add(5, 7)
add(10, 15)

@count_calls
def sub(a,b):
    print(a - b)
sub(10, 5)  


# Build a decorator that logs the function name and arguments every time the function is called.

def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper





students = []

@log_args
def funct_main(name, age, city="delhi"):
    students.append({"name": name, "age": age, "city": city})



    
funct_main("Alice", 20, city="Mumbai")


# Write a decorator that retries a function up to 2 times if it raises an exception.




