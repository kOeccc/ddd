k = input()
po = k.find('f')
po1 = k[::-1].find('f')  # ���_����.find(��� ����)
if k.find('f') != -1:
    if len(k) == po + po1 + 1:
        print(po)
    else:
        print(po, len(k) - po1 - 1)
