n = int(input("Enter n : "))
length = len(str(n))
for i in range(length):
    x = str(n)[i]
    print(x + ": ", end="")
    for j in range(1, int(x) + 1):
        print(x, end="")
    print()
