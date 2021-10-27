n = int(input())
hour = n // 3600 % 24
min = n // 600 % 6
min1 = n // 60
sec = n % 3600 % 60 // 10
sec1 = n % 3600 % 60
print(hour, ':', min, min1 % 10, ':', sec, sec1 % 10, sep='')
