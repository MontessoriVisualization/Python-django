#list is python 
student_present=["sunday","monday","tuesday"]
print(student_present[0])
student_present[0]="sunday morning"
print(student_present)
#length
print(len(student_present))

#appending
student_present.append("wednesday")
print(student_present[-1])

#slicing
#[sunday morning, monday, tuesday, wednesday]
print(student_present[1:3]) # this will give us a new list with the elements from index 1 to index 2 (3 is not included)

#negativve slicing
print(student_present[-3:-1]) # this will give us a new list with the elements from index -3 to index -2 (-1 is not included)

list1=[1,2,3]
list2=list1[:] # this will give us a new list with the same elements as list1 but it will be a different list in memory
print(list1)
print(list2)
list1.append(4)
print(list1)
print(list2) # this will also give us [1,2,3,4] because list1 and list2 are pointing to the same list in memory


list1[0] = [10,20,30]
print(list1)
print(list2)
print(list1[0][0]) # this will give us 10

#insert
student_present.insert(1,"thursday")
print(student_present)


#extend
friends_list1=["ram","shyam","hari"]
friends_list2=["sita","gita","radha"]
friends_list1.extend(friends_list2)
print(friends_list1)
print(friends_list2)

#remove
friends_list1.remove("shyam")
print(friends_list1)#does not include shyam

#pop
print(friends_list1.pop()) # this will remove the last element from the list and return it
print(friends_list1)
poped_friend=friends_list1.pop(1) # this will remove the element at index 1 and return it
print(friends_list1)
print(poped_friend)


#del
del friends_list1[0] # this will remove the element at index 0 from the list
print(friends_list1)
del friends_list2 # this will delete the entire list from memory

# print(friends_list2) # this will give us an error because friends_list2 has been deleted from memory

#clear
friends_list1.clear() # this will remove all the elements from the list but the list itself will still exist in memory
print(friends_list1) # this will give us an empty list []

#copy list
list3=list1.copy() # this will give us a new list with the same elements as list1 but it will be a different list in memory
list3=list1[:] # this will also give us a new list with the same elements as list1 but it will be a different list in memory

#adding and extend
list4=[1,2,3]
list5=[4,5,6]
list6=list4+list5 # this will give us a new list with the elements of list4 and list5
print(list6)
list4.extend(list5) # this will add the elements of list5 to the end of list4
print(list4)

