n = int(input())
k = 0
m = 1
i = 1
while i <= n:
    k = k + (m * i)
    m += 1
    i += 1
print(k)
