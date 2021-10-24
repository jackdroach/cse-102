# Author: Jack Roach
# Email: roachjd2@miamioh.edu
# Section: D
# Date: 9/15/2021

'''
Purpose: to find the area of a rectangle, given the length
and the width of the rectangle
Inputs:
User supplies the length and the width of the rectangle as numbers
Outputs:
User greeted and prompted for input of the two dimensions
Rectangle area will be displayed on terminal screen
'''

print("The area of a rectangle")
print()

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print()

area = float(length * width)

print("The area of a rectangle with length",length,"and width",width,"is:",area)
