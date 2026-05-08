#  "The Smart Checkout System"
# Objective: Create a JavaScript program that simulates a simple shopping cart checkout process.

# Instructions for Students:
# Write a code script that performs the following steps in order:

# Setup the Store:

# Create a const variable for walletBalance and set it to 5000.
# Create an array called cartItems containing three prices: [500, 1200, 350].
# Manage the Cart (Array Operations):

# A new item is added! Use .push() to add a price of 2000 to the cart.
# Oops, that item is too expensive. Use .pop() to remove the last item.
# Create a new array called recommendedItems with prices [100, 200].
# combine recommendedItems and cartItems into a new array called finalCart using the Spread Operator (...).
# Calculate Totals (Math & Operators):

# Calculate the sum of the prices in finalCart (Hint: since we don't have loops yet, access them manually like finalCart[0] + finalCart[1]...).
# Store this sum in a variable totalPrice.
# Add a 10% tax to the logic. Update totalPrice to include the tax.
# Round the totalPrice to 2 decimal places using .toFixed().
# Coupon Code Handling (String Manipulation):

# Create a variable couponCode with the messy value "   DisCOunT10   ".
# Clean up the code: Remove the whitespace using .trim() and convert it to uppercase.
# If the cleaned code is "DISCOUNT10", subtract 500 from the totalPrice.
# Final Decision (Conditionals):

# Write an if/else statement:
# If totalPrice is less than or equal to walletBalance: Console log "Purchase Successful! New Balance: [Remaining Amount]".
# Else: Console log "Insufficient Funds! You need [Missing Amount] more."
# Receipt Generation (Randomness):

# Generate a random Order ID between 1 and 100 using Math.random() and Math.floor().
# Console log a receipt message using Template Literals (backticks): Order [ID] confirmed. Thank you for shopping!


import random
WalletBalance=5000
CartItems=[500,1200,350]
CartItems.append(2000)
print(CartItems)
CartItems.pop()
print(CartItems)

RecommendedItems=[100,200]# we can use *or + or extent to destructure lists and make one list out of them
FinalCart=CartItems+RecommendedItems
print(FinalCart)
TotalPrice=FinalCart[0]+FinalCart[1]+FinalCart[2]+FinalCart[3]+FinalCart[4]
print(TotalPrice)

TotalPricewithTax= TotalPrice+(10/100)*TotalPrice
print(TotalPricewithTax)

CuponCode ="       DisCOunT10          "
print(CuponCode.strip().upper())
if CuponCode=="DISCOUNT10":
    TotalPrice-=500

if TotalPrice<= WalletBalance:
    NewBalance=WalletBalance-TotalPrice
    print(f"Purchase Sucessfull New Balance={NewBalance}")
    OrderID=random.randint(1,101)
    print(f" {OrderID} Confimed!!!! Thankyou for shopping")
    
else:
    MissingBalance=TotalPrice-WalletBalance
    print(f"Insufficient Balance!!! You need {MissingBalance} more")

