a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
abe = (a * d) - (b * c)
delY = (e * d) - (b * f)
delX = (a * f) - (e * c)
x = delX / abe
y = delY / abe
print(x, y)
