def add(num1,num2):
    print( num1 + num2)

add(423,3243)

def multiply(p1,p2):
    print(p1*p2)

multiply(34234,2434)
multiply('q',5)
multiply(45,'q')

import math
def circle_stats(radius):
    area = math.pi* (radius**2)
    circumference = 2 * math.pi * radius
    return area,circumference

print(circle_stats(45))

a,c = circle_stats(3)

def greet(name = "Useer"):
    return "Hello, "+  name +" !"



