def isPrime(n):
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            return False
    return True


a = int(input("Enter a : "))
b = int(input("Enter b : "))
primes = []
for i in range(a, b + 1):
    if i != 0 and i != 1 and isPrime(i):
        primes.append(i)
print(primes)