# Dictionaries
letslearnuser={
    "name":"saugat",
    "age": 22,
    "course":["python","django","js"]


}
print(letslearnuser)
#couse python
print(letslearnuser["course"][0]) # this will give us the first element of the course list which is python
#length
print(len(letslearnuser)) # this will give us the number of key-value pairs in the dictionary which is 3


#modifying 
letslearnuser["age"] = 23 # this will modify the value of the age key to 23

#adding a new key-value pair
letslearnuser["email"] = "saugat@example.com"
print(letslearnuser)

#keys
keys=letslearnuser.keys() # this will give us a list of all the keys in the dictionary
#keys after mutating 
print(keys) # this will give us a list of all the keys in the dictionary after mutating it
letslearnuser["name"] = "saugat shrestha" # this will modify the value of the name key to saugat shrestha
letslearnuser["surname"] = "shrestha" # this will add a new key-value pair to the dictionary with the key surname and the value shrestha
print(keys) # this will give us a list of all the keys in

#values
values=letslearnuser.values() # this will give us a list of all the values in the dictionary
print(values) # this will give us a list of all the values in the dictionary
letslearnuser["age"] = 24 # this will modify the value of the age key
print(values) # this will give us a list of all the values in the dictionary after mutating it


# items
items=letslearnuser.items() # this will give us a list of all the key-value pairs in the dictionary as tuples
print(items) # this will give us a list of all the key-value pairs in the dictionary
letslearnuser["course"].append("react") # this will modify the value of the course key by appending react to the list
print(items) # this will give us a list of all the key-value pairs in the dictionary after mutating it



#if i want to acess the value name
Items_dict=letslearnuser.items() # this will give us a list of all the key-value pairs in the dictionary as tuples
print(Items_dict) # this will give us a list of all the key-value pairs in the dictionary

# removing items
letslearnuser.pop("surname") # this will remove the key-value pair with the key surname from the dictionary
print(letslearnuser)
#del
del letslearnuser["email"] # this will remove the key-value pair with the key email from the dictionary
print(letslearnuser)

#clear
letslearnuser.clear() # this will remove all the key-value pairs from the dictionary
#del list
del letslearnuser # this will delete the dictionary from memory

#nested dictionary
nested_dict={
    "name":"saugat",
    "age": 22,
    "course":{
        "python":"beginner",
        "django":"intermediate",
        "js":"advanced"
    }
}
print(nested_dict)
#acessing begainers
print(nested_dict["course"]["python"]) # this will give us the value of the python key in the course dictionary which is beginner

#copy 
copy_dict=letslearnuser.copy() # this will give us a new dictionary with the same key-value pairs as letslearnuser
print(copy_dict) # this will give us a new dictionary with the same key-value pairs as

#copy using dict constructor
copy_dict2=dict(letslearnuser) # this will give us a new dictionary with the same key-value pairs as letslearnuser
print(copy_dict2) # this will give us a new dictionary with the same key-value pairs