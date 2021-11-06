n = input()
i = 0
while len(n) > i:
    if i % 3 == 0:
        k = n[1 + i:i + 3:]
        print(k, end='')
    i += 1
