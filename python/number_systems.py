# Author: Jack Roach
# Date: 9/15/2021

'''
Python program to convert decimal number into binary,
octal, and hexadecimal number system
'''

dec = int(input("enter any decimal number: "))

print("The input decimal value is:",dec)
print()
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")
