n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
# f n3 - n1 <= 2 or n1 - n3 <= 2:
if -1 <= (n1 - n3) < 2 and -1 <= (n2 - n4) < 2:
    print('YES')
else:
    print('NO')
