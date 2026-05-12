#conversion of data types in  python

# number to string
num = 10.3
complex_num = 2 + 3j
str_num = str(num)#"10.3"
str_complex_num = str(complex_num)#"(2+3j)"

# string to number
str_num = "10.3"
num = float(str_num)#10.3
str_complex_num = "2 + 3j"
complex_num = complex(str_complex_num)#(2+3j)

# name="saugat" X
# name=int(name) # this will give an error because we cannot convert a string to an integer

# number and string to boolean
num = 0
str_num = ""
bool_num = bool(num) # this will give False because 0 is considered as False in python
bool_str_num = bool(str_num) # this will give False because an empty string is considered
none_value = None
bool_none_value = bool(none_value) # this will give False because None is considered as False in python
print("bool of num:", bool_num)
print("bool of str_num:", bool_str_num)
print("bool of none_value:", bool_none_value)
