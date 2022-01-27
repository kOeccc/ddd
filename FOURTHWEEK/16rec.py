def rec(a, n):
    if n == 0:
        return 1
    elif a == 0:
        return 0
    elif n % 2 == 0:
        return rec(a * a, n // 2)
    elif n > 0:
        return rec(a, n - 1) * a


a = float(input())
n = int(input())
print(rec(a, n))
