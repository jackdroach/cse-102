# Author: Jack Roach
# Email: roachjd2@miamioh.edu
# Section: D
# Date: 10/04/2021

"""
Python program that uses if/else statements to determine the price of a ticket based off of age as input.
"""

# Get user input
age = int(input("Enter your age: "))

# Finding the matching age and price
if age > 50:
    price = 12
elif age < 20:
    price = 12
else:
    price = 20

# Printing the results of the if/else statement above
if age > 10:
    print(f"Ticket price is ${price}")
else:
    print("You're not eligible to buy a ticket.")
