import math
import sys

def calc_area(r):
    """doc"""
    area = math.pi * r**2
    return area

#Cálculo del área del círculo
radius=5 
area = calc_area(radius) 
print ("Area of circle:", area)
