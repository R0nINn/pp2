# import math

# x = int(input())

# def deg_to_rad(x):
#     y = math.radians(x)
#     print("degree in radians:",y)

# deg_to_rad(x)

# h = int(input())
# b1 = int(input())
# b2 = int(input())

# def areaOfTrap(h,b1,b2):
#     return print(((b1+b2)*h)/2)

# areaOfTrap(h,b1,b2)
    
    
from math import tan,pi

n =int(input("Enter a number of sides:"))
l = int(input("Enter a lendth of side:"))

def area(n,l):
    return print("area of a polygon => " , n * (l ** 2) / (4 * tan(pi / n)))
area(n,l)

l = int(input())
h = int(input())

def pal(l,h):
    return print(l*n)

pal(l,n)
