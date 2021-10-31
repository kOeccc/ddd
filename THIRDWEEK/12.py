a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
abe = (a * d) - (b * c)
delY = (e * d) - (b * f)
delX = (a * f) - (e * c)
x = delX / abe
y = delY / abe
print(y, x)
