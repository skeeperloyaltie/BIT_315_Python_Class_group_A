""" 
    Write a program to prompt the user to for hours and rate per hour 
    to compute gross pay
    
"""

# Initialize values 

hours = int(input('Enter the total numbe rof hours worked: '))

rate = float(input("Enter the rate per hour: "))
# Calculate gross pay

gross_pay = hours * rate

print("Total Pay is :  ", gross_pay)
