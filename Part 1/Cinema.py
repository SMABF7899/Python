import math

r = int(input("Enter r : "))
c = int(input("Enter c : "))
if 10 >= c > 0:
    print("Right " + str(math.fabs(r - 11)) + " " + str(c))
else:
    print("Left " + str(math.fabs(r - 11)) + " " + str(math.fabs(c - 21)))
