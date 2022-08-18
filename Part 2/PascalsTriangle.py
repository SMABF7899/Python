def Factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


n = int(input("Enter n : "))
p = 0
for i in range(n):
    for j in range(i + 1):
        print(str(int(Factorial(i) / (Factorial(j) * Factorial(i - j)))) + " ", end="")
    print()
