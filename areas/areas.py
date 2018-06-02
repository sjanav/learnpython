#This program will find the ares of a square, rectangle and triangle
import math

def area_square(length):
    areaOfSquare = length * length
    return areaOfSquare
 

def area_rectangle(length,width):
    areaOfRectangle = length * width
    return areaOfRectangle   


def area_triangle(base,height):
    areaOfTriangle = (base * height)/2
    return areaOfTriangle

def area_circle(radius):
    area = math.pi * radius**2
    return area

if __name__ == '__main__':
    print("Area of triangle is "+str(area_triangle(9,5)))
    print("Area of square is "+str(area_square(6)))
    print("Area of rectangle is "+str(area_rectangle(6,7)))
    