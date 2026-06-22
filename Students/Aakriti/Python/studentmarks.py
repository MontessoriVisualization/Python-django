# 2.Write a function student_marks(math, science) that returns:

# total marks
# average marks

def student_marks(math,science):
    total_marks=math+science
    average_marks=total_marks/2
    return total_marks,average_marks

math_marks=int(input("Enter marks for Math: "))
science_marks=int(input("Enter marks for Science: "))
total, average = student_marks(math_marks,science_marks)
print(f"Total marks: {total}")
print(f"Average marks: {average}")