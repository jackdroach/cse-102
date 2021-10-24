# Author: Jack Roach
# Email: roachjd2@miamioh.edu
# Section: D
# Date: 10/04/2021

"""
Python program that uses if/else statements to determine weight in pounds based off of user input in ounces.
"""

# How many ounces? 43
# There are 2 pounds and 11 ounces left over.

# Get user input
ounces = int(input("How many ounces? "))

# Calculate pounds and left over ounces
pounds = ounces / 16
leftOver = ounces % 16

# Print the result
if ounces > 16:
    print(f"There are {int(pounds)} pounds and {leftOver} ounces left over.")
elif ounces < 0:
    print("The number of ounces cannot be negative.")
else:
    print(f"There are {leftOver} ounces.")
