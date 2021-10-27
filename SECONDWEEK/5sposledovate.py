n = int(input())
m = 0
ave = 0
while n != 0:
    m = n + m
    ave += 1
    n = int(input())
print(m / ave)
