def factorial(n):
    i = 2
    k = 1
    while i <= n:
        k = k * i
        i += 1
    return k  # возвращаем к из функции т.е. что будет выдавать в (n)


n = int(input())
print(factorial(5))
print(factorial(n) - factorial(n - 1))
