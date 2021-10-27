a = int(input())
b = int(input())
c = int(input())
if a > b:
    (b, a) = (a, b)
if b > c:
    (c, b) = (b, c)
if a > b:
    (a, b) = (b, a)
print(a, b, c)
