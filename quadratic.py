import math

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coeffiicients (a,b,c): "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()

    if a > 0 and b > 0 and c > 0:
        print("The solutions are:", root1, root2)
    else:
        print("The equation has no real roots!")
    
main()