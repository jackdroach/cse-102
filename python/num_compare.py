# Author: Jack Roach
# Email: roachjd2@miamioh.edu
# Section: D
# Date: 9/29/2021

"""
Basic Python number comparison program using if/else. Gets user input as 2 numbers and compares them using comparison
operators. Prints the result.
"""

# Get user input
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

# Calculate the comparison
if firstNumber == secondNumber:  # #1 equal to #2
    print(f"The number {firstNumber} is equal to {secondNumber}")  # Prints result
elif firstNumber > secondNumber:  # #1 greater than #2
    print(f"The number {firstNumber} is greater than {secondNumber}")  # Prints result
elif firstNumber < secondNumber:  # #1 less than #2
    print(f"The number {firstNumber} is less than {secondNumber}")  # Prints result
else:  # Fallback if none of the conditions above are met.
    print("Unable to compute.")
