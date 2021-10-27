perc = int(input())
x = int(input())
y = int(input())
pxy = (x * 100 + y) * (100 + perc)
r = pxy // 10000
k = (pxy - (pxy // 10000) * 10000) // 100
m = (pxy - pxy // 10000)
print(r, k, pxy, m)
