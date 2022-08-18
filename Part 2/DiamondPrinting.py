n = int(input("Enter n (0 <= n <= 10): "))
diameter = 2 * n + 1
if 1 <= n <= 10:
    for i in range(1, int(diameter / 2) + 2):
        for j in range(int(diameter / 2 - i + 1)):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    for i in range(1, int(diameter / 2 + 1)):
        for j in range(i):
            print(" ", end="")
        for j in range(int(diameter - (2 * i))):
            print("*", end="")
        print()
else:
    print("Your number is out of the range of 1 to 10")
