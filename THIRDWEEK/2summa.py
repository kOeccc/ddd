n = float(input())
i = 1
k = 1
sum = float(0)
while i <= n:
    sum = 1 / (i ** 2) + sum
    i += 1
    k += 1
print('{0:.6f}'.format(sum))
