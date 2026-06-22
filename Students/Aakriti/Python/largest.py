# Create a function that finds the largest number using *args

def largest(*args):
    lar=0
    for x in args:
        if x >lar:
            lar=x
    print(f"The largest number is :{lar}")



largest(1,2,30,400,5,6,7)