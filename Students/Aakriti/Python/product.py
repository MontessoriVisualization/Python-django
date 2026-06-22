#Create a function that accepts product details using **kwargs name ,price and quantity and prints them in a formatted way.

def product(**details):
    for key,value in details.items():

        # print(f"The Detils of your product are {key}: {value}")
        print(f"{key}: {value}")
print("The details of your products are below :")
product(
    Name="Cookies",
    Price=250,
    Quantity=3
)