# Python Variables
import random

# Type conversion 

# convert an string to an INT

n = 12

print(n)


# Convert a float to an INT

num_float = 10.167

print(int(num_float))

# cONVERT A STRING TO AN INT

val = "Skeeper"

#print(int(val)) # Generates an error


# Concatenate values
a = "Skeeper"

b = "Loyaltie"

c = 12 

v = c * c 

u = v // c

h = u ** v % v

""" 
    The way to add values and concatenate strings
    
    add integers to values and see outcome
    
    generate senetesnes by adding strings or iusing operaors to format code
    
    
"""

print(a*5)

print(v, u, h)

# Getting type error

print(a + c) # Generates a Type Error


""" 
    Python Variables 
        Local and Global Variables
"""

# Defining  Global variables

val_a = random.randint(range(12, 100))

def summation():
    # Define Local Variables
    
    b = random.randint(12,67)
    
    sum = val_a + b
    
    print(sum)
    
print(summation())

"""
    Python Functions
"""