# Author: Jack Roach
# Email: roachjd2@miamioh.edu
# Section: D
# Date: 9/22/2021

"""
Python program to calculate change. Gets input in cost from a user and then prints the output as the change the user
gets back.
"""

# Descriptor of program
print("Change Calculator")
print()

# Requests the item price
price = round(100*float(input("Enter the price of the item you bought: ")))

# Requests the amount of money given to the cashier in dollars & cents
pay = round(100*float(input("Enter the amount of money you gave the cashier: ")))
print()

# Calculate the total change in cents
change = pay - price

# Calculate the amount of dollars
dollars = round((change / 100) % 100)

# Calculate the amount of quarters
change2 = change - (dollars * 100)
quarters = round((change2 % 25) / 25)

# Calculate the amount of dimes
change3 = change2 - (quarters * 25)
dimes = round((change3 % 10) / 10)

# Calculate the amount of nickles
change4 = change3 - (dimes * 10)
nickles = round((change4 % 5) / 5)

# Calculate the amount of pennies
change5 = change4 - (nickles * 5)
pennies = round(change5 / 1)

# Prints the number of coins
print(f"Your change: ")
print(f"   dollars       {dollars}")
print(f"   quarters      {quarters}")
print(f"   dimes         {dimes}")
print(f"   nickels       {nickles}")
print(f"   pennies       {pennies}")
print()

# Informs the user that the process has exited
print("Thank you for your business")