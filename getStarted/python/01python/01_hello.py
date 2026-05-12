import math
print(math.sqrt(16))
print(math.pi)
print(dir(math)) # to see all the functions and variables in math module

print("hello world")
# This is a comment
        # function add(a, b){
        #     console.log(a + b);
        # }
def add(a, b):
    return a + b

#is eligable to vote
def is_able_to_vote(age):
    if age >= 18:
        return True
    else:
        return False

# Text Type:	str(sting in js)
# Numeric Types:	int, float, complex(number in js)
# Sequence Types:	list, tuple, range(array in js)
# Mapping Type:	dict(object in js)
# Set Types:	set, frozenset(set in js)
# Boolean Type:	bool(boolean in js)
# None Type:	NoneType(null in js)


import os
print(os.getcwd()) # to get the current working directory
import sys
print(sys.platform) # to get the platform information
print(sys.version) # to get the python version
# mutable and immutable data types


number = 10
print(number)
number = 20
print(number)

# modules are pre written code that we can use in our program
# foreg example: math module, random module, datetime module etc. we can import these modules and use their functions in our program.

