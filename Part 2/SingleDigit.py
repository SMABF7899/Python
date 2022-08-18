n = int(input("Enter n : "))
s = 0
while True:
    s = 0
    length = len(str(n))
    for i in range(length):
        figure = str(n)[i]
        s += int(figure)
    if s >= 10:
        n = s
    if s < 10:
        break
print(s)