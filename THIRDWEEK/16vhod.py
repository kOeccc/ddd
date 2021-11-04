k = input()
po = k.find('f')  # считает с начала строки до буквы ф
po1 = k[po + 1::]  # делаем строку с найденного символа до конца
cut = po1.find('f')  # ищем в строке снова ф, уже вторая
ss = po + cut + 1
if cut == -1 and po >= 0:
    print(cut)
elif cut + po == -2:
    print('-2')
elif po < ss:
    print(ss)
