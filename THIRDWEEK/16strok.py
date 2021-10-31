n = input()
h1 = n.find('h')  # at start string to first letter
h2 = n[::-1].find('h')  # at end string to first leter(reverse)
h3 = len(n) - h2  # at start to second(at end) letter
print(n[0:h1], n[h3:], sep='')
