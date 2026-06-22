#Write a function circle(radius) that returns:
# area
# circumference
import math
def circle(radius):
    area=math.pi*radius**2
    circum=2*math.pi*radius

    return area,circum

AreaOfCircle, PeriOfCircle=circle(24)
print(f"The area of given circle is : {round(AreaOfCircle,2)}")
print(f" The circumference of circle is : {round(PeriOfCircle,2)}")