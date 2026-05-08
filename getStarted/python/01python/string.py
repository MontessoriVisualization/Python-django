# string in python
name = "saugat"
print("name:", name)
print("type of name:", type(name))
print("character at index 0:", name[0])
print("length of name:", len(name))

decription = """
this is a multi line string
we can use triple quotes to create a multi line string
this is the end of the multi line string
"""

print("description:", decription)
concatination = name + " is a teacher"
print("concatination:", concatination)
print("index 1 of description:", decription[1])


#is smth in description
print("saugat " in decription)# false
print("saugat " not in decription)# true

# string methods
print("name in uppercase:", name.upper())
print("name in lowercase:", name.lower())
print(dir(name)) # to see all the methods of string
#capitalize the first letter of the string
print("name with capitalized first letter:", name.capitalize())# first letter of the string will be capitalized and the rest will be in lowercase
print("name with capitalized first letter:", name.title()) # to capitalize the first letter of each word in the string

sentence = "   this is a sentence with leading and trailing spaces   "
print("sentence with leading and trailing spaces:", sentence.strip()) # to remove leading and trailing spaces from the string

list_of_words = "apple, banana, orange"
print("list of words:", list_of_words.split(", ")) # to split the string into a list of words based on the delimiter ", "
#replace
print("name with replaced characters:", name.replace("s", "R")) # to replace all occurrences of "a" with "o" in the string

#index
print("index of a in name:", name.index("a")) # to find the index of the first occurrence of "a" in the string

#string slicing
b = "Hello World!"
print(b[2:5])# prints from [2] to [5-1]
print(b[:5])# prints from [0] to [5-1]
print(b[6:11])# prints from [6] to [11-1]
print(b[-6:-1])# prints from [-6] to [-1-1]

# f stringa (formatted string)
name = "saugat"
age = 25
print("Hi my name is " + name + " and I am " + str(age) + " years old") # using concatenation
print(f"Hi my name is {name} and I am {age} years old") # using f string