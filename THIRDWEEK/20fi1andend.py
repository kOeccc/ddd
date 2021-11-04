n = input()
one = n.find('h') + 1
end = n.rfind('h')
middle = n[one:end].replace('h', 'H')
cut = 0
print(n[:one], middle, n[end::], sep="")
