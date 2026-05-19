#int
tup1=(1, 2, 3, 4, 5)
tup2=(6, 7, 8, 9, 10)
print(tup1[0]) # this will give us the first element of the tuple which is 1
print(tup1[-1]) # this will give us the last element of the tuple which
print(tup1[0:3]) # this will give us a new tuple with the elements from index 0 to index 2 (3 is not included)
print(tup1[-3:-1]) # this will give us a new tuple with the

tup3= tup1 + tup2 # this will give us a new tuple with the elements of tup1 and tup2
tup2= tup2 * 100 # this will give us a new tuple with the elements of tup2 repeated twice
print(tup3)
print(tup2)

#unpacking a tuple
tup4=(1, 2, 3)
(a, b, c) = tup4 # this will unpack the elements of the tuple into the variables a, b, and c
print(a) # this will give us 1
print(b) # this will give us 2
print(c) # this will give us 3

tup5=(1, 2, 3, 4, 5)
(a, b, *rest) = tup5 # this will unpack the first two elements of
# the tuple into the variables a and b, and the rest of the elements into the variable rest
print(a) # this will give us 1
print(b) # this will give us 2
print(rest) # this will give us [3, 4, 5] because the rest of the elements are stored in a list


#mutating tuple
tup6=(1, 2, 3)
# tup6[0] = 10 # this will give us an error because tuples are
# list are mutable so we can convert the tuple to a list, mutate the list, and then convert it back to a tuple
list1=list(tup6) # this will give us a new list with the same elements
print(list1)
list1[0] = 10 # this will mutate the list by changing the first element to 10
print(list1)

