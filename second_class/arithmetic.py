# Operators
# Class work
# Arithmetic Operators.
# initialize basic Operator functions
# Functions 

def arithmetic_functions( val_a, val_b):
    val_a = 0
    val_b = 0
    
    choice = input("Enter your choice: ")
    
    if choice == "+":
        print("Addition: ", val_a + val_b)
    elif choice == "-":
        if val_a > val_b:
            print("Subtraction: ", val_a - val_b)
        elif val_b > val_a:
            print("Subtraction: ", val_b - val_a)
    elif choice == "//":
        print("Floor Division: ", val_a // val_b)
        
    elif choice == "*":
        print("Multiplication: ", val_a * val_b)
        
    elif choice == "/":
        print("Division: ", val_a / val_b)  
    elif choice == "%":
        print("Modulus: ", val_a % val_b)
        
    elif choice == "**":
        print("Exponential: ", val_a ** val_b)
    
    else:
        print("Wrong Choice:")
        
    return arithmetic_functions()


if __name__ == '__main__':
    def main():
        value_a = int(input("Enter a number one: "))
        value_b = int(input("Enter another number: "))
        
        print(arithmetic_functions(value_a, value_b))
        
    main()
        
    