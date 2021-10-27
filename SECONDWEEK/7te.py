n = int(input())
m = 0
k = -1
while n != 0:
    if m < n:
        k += 1
        m = n
    if m > n:
        m = n
    n = int(input())
print(k)
