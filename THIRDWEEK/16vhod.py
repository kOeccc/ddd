k = input()
ff = k.find('f')
i = 0
while i <= 2:
    print(ff)
    ff = k.find('f', ff + 1)
    i += 1
    n = ff + k.find('f') - 1
if i == 1:
    print('9999')
elif i == 0:
    print('-2')
