def nn(n):
    if n != 0:
        a = int(input())
        if a != 0:
            return nn(n + a)
        return n
    return n


n = int(input())
print(nn(n))
