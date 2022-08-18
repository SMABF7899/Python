import math

a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))
if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Area of the triangle is " + str(s))
else:
    print("This triangle is not defined")