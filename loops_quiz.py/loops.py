from xml.dom.expatbuilder import FilterVisibilityController


x = ['ab', 'cd']
y = []
for i in x:
    y.append(i.upper())
    
print(y)


# Question two

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    
    i += 1


# Question three

# Write a Python program to convert temperatures to and from celsius, fahrenheit. 
# Formula : c/5 = f-32/9  - where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :  60°C is 140 in Fahrenheit  45°F is 7 in Celsius
# Solution 

while True:
    print("""
    1. Convert from Celsius to Fahrenheit
    2. Convert from Fahrenheit to Celsius
    3. Quit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print("The temperature in Fahrenheit is: ", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The temperature in Celsius is: ", celsius)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
        
        
        
        
        
# Question four
# Write a Python program to check if a number is even or odd .

num = int(input("Enter a number: "))

while True:
    if num % 2 == 0:
        print("{} is even".format(num))
        break
    else:
        print("{} is odd".format(num))
        break


# Question Five 
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

# Note : Use 'continue' statement. 

# Expected Output : 0 1 2 4 5

while True:
    for i in range(6):
        if i == 3 or i == 6:
            continue
        print(i)
        break
    break


# Question Six
#  The examination department has provided you with the following rules for grading.
#  The students are required to take a supplementary examination if they score 39 marks and below.
#  Write a python program to help implement the grading system.  

# Solution 

grade = int(input("Enter your grade: "))

if grade >= 70 and grade <= 100:
    print("A")
elif grade >= 39 and grade <= 69:
    print("B")
elif grade >= 50 and grade <= 59:
    print("C")
elif grade >= 40 and grade <= 49:
    print("D")
else:
    print("E(Fail)")
