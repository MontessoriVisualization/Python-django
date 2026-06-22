# 4. Function with *args
# Write a function student_marks multiple subjects that returns:

# # total marks
# # average marks
def student_marks(*args):
    print(args)
    marks=sum(args)
    average_marks= marks/len(args)
    return marks, average_marks


total, average=student_marks(50,50,50,50)
print("Total marks=",total)
print("Average=", average)


# Function with **kwargs
# Write a function student(**details) that prints all key-value pairs.

def student(**details):
    print(details)
    for key, value in details.items():
        print(f"{key}:{value}")

student(
    Name ="Aakriti",
    age=19,
    club='Software'
    
)