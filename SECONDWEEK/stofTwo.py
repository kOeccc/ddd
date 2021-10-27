n = int(input())
m = 1
while m <= n:
    if n == m:
        print('YES')
    elif m * 2 > n:
        print('NO')
    m = m * 2
