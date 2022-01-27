def power(a, n):
    i = 1
    a = a * a ** (n - 1)
    i += 1
    return a


a = float(input())
n = int(input())
print(power(a, n))
