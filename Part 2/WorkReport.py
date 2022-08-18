total = 0
n = int(input("Enter number of bottles (n) : "))
k = int(input("Enter volume amount (k) : "))
c = list(range(n))
for i in range(n):
    c[i] = int(input("Enter Bottle volume " + str(i + 1) + " : "))
    total += c[i]
if total >= k:
    print("YES")
else:
    print("NO")
