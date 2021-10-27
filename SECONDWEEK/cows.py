b = int(input())
n = b % 10
if b == 0 or n == 0 or 5 <= n <= 9 or 5 <= b <= 19:
    print(b, 'korov')
elif n == 1 and b != 11:
    print(b, 'korova')
elif n >= 2 <= 4:
    print(b, 'korovy')
