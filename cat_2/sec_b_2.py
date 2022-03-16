# a)  Write a python function to calculate volume of a sphere (Use the formula provided)

def volume_sphere(radius):
    return (4/3) * 3.14 * radius**3

def main():
    print("Enter a radius:")
    radius = float(input())
    print("Volume of sphere: " + str(volume_sphere(radius)))

if __name__ == '__main__':
    main()