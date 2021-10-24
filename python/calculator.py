# Author: Jack Roach
# Email: roachjd2@miamioh.edu
# Section: D
# Date: 9/29/2021

"""
Basic Python calculator program using if/else. Gets user input as 2 numbers and an arithmetic operator. Uses the input
to compute and print the results.
"""

# Print some lines to introduce the program to the user
print("Select operation.")
print("      1.Add")
print("      2.Subtract")
print("      3.Multiply")
print("      4.Divide")

# Get user input
operatorNumber = int(input("Enter your choice (1/2/3/4): "))
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))

# Run calculations
if operatorNumber == 1:  # If the user enters 1
    operator = "+"
    result = firstNumber + secondNumber  # Add
    print(f"{int(firstNumber)} {operator} {int(secondNumber)} = {int(result)}")  # Print the result

elif operatorNumber == 2:  # If the user enters 2
    operator = "-"
    result = firstNumber - secondNumber  # Subtract
    print(f"{int(firstNumber)} {operator} {int(secondNumber)} = {int(result)}")  # Print the result

elif operatorNumber == 3:  # If the user enters 3
    operator = "*"
    result = firstNumber * secondNumber  # Multiply
    print(f"{int(firstNumber)} {operator} {int(secondNumber)} = {int(result)}")  # Print the result

elif operatorNumber == 4:  # If the user enters 4
    operator = "/"
    result = firstNumber / secondNumber  # Divide
    print(f"{int(firstNumber)} {operator} {int(secondNumber)} = {int(result)}")  # Print the result

else:  # If the user enters any other number for the operator
    print(f"Operator \"{operatorNumber}\" is invalid.")
