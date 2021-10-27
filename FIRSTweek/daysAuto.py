n = int(input())
m = int(input())
k = (m // n) + (m % n + (n - 1)) // n
print(k)
