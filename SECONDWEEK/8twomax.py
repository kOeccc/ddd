n = int(input())
m = 0
k = n
i = 0
p = 0
while n != 0:
    if n == k:
        i += 1
        if i > m:
            m = i
    else:
        i, k = 1, n
    n = int(input())
print(m)
