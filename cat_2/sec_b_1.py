# b) Write a Python program to convert temperatures to and from celsius and fahrenheit. Use the formula provided below (5 marks)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Enter a temperature in Celsius:")
    celsius = float(input())
    print("Enter a temperature in Fahrenheit:")
    fahrenheit = float(input())
    print("Celsius to Fahrenheit: " + str(celsius_to_fahrenheit(celsius)))
    print("Fahrenheit to Celsius: " + str(fahrenheit_to_celsius(fahrenheit)))

if __name__ == '__main__':
    main()