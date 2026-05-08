# from hello import add
# print(add(2, 3))

# innerworking of python
# 1. python code ==> bytecode ===> vm(pthon interpreter) 
#         (compile(convert))      

def add(a, b):
    return a + b
pi = 3.14

# mutable and inmutable data types in python
a=10
# a =====> 10
# ||
# ||
# ||
# \/
# 20 <======b
# 
a=20
b=20
print(a == b) # True because both a and b are pointing to the same memory location where the value 20 is stored
print(a is b) # True because both a and b are pointing to the same memory location where the value 20 is stored

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)# True because both x and z are pointing to the same memory location where the list is stored
print(x is y)# False because x and y are pointing to different memory locations where the lists are stored
print(x == y)# True because the values of x and y are the same even though they are stored in different memory locations
print(x == z)# True because the values of x and z are the same and they are stored in the same memory location
print(x is not y) # True because x and y are pointing to different memory locations where the lists are stored
print(x is not z) # False because x and z are pointing to the same memory location where the list is stored
print(id(x)) # to see the memory location of x
print(id(y)) # to see the memory location of y
print(id(z)) # to see the memory location of z
