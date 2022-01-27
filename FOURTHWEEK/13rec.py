def power(a, n):
    i = 1
    if n == 0:
        return 1
    if i < n:
        a = a * a ** (n - 1)
        i += 1
    return a


a = float(input())
n = int(input())
print(power(a, n))
