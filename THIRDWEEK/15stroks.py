k = input()
po = k.find('f')  # где_ищем.find(что ищем)
ks = k[::-1]
n2 = len(k) - ks - 1
ll = ks.find('f')
print(po, ks, n2)
