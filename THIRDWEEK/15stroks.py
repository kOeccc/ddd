k = input()
po = k.find('f')  # считает с начала строки до буквы ф
po1 = k[::-1].find('f')
cut = len(k) - po1 - 1
po3 = k[po1+1:cut:].find('f')
print(po, po1, len(k), po3, cut, po1 + po3 + 1)
if k.find('f') != -1:
    if len(k) == po + po1 + 1:
        print(po)
    else:
        print(po, len(k) - po1 - 1)
