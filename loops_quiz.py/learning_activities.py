from numpy import ones


# Activity one

# Write a Python program to find numbers between 100 and 400 (both included) where each digit
# of a number is an even number. The numbers obtained should be printed in a comma-separated
# sequence.

# Solution 1

for i in range(100, 400):
    if i % 10 == 0 and i % 20 == 0:
        print(i, end=',')
print( 
)

# Activity two

# Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor Note : The
# Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, .... Every next number is
# found by adding up the two numbers before it
# Solution 2 

for i in range(50):
    if i == 0:
        print(i, end=',')
    elif i == 1:
        print(i, end=',')
    else:
        print(i, end=',')
        print(i + i - 1, end=',')