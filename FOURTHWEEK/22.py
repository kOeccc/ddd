from re import S


def move(n, st, fn):
    if n == 1:
        print(n, st, fn)
    else:
        tmp = 6 - st - fn
        move(n - 1, st, tmp)
        print(n, st, fn)
        move(n - 1, tmp, fn)


n = int(input())
move(n, 1, 3)