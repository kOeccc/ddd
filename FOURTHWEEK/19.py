def phib(n):
    # определить две переменные соответсвующие фибо 1 и 1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


k = int(input())
print(phib(k))
