import math


def MinDivisor(n):
    i = 2
    while n % i != 0:
        i += 1
        if i > math.sqrt(n):  # �������� �� ���������� ������ ����� �� �������
            return (n)
    return(i)


n = int(input())
print(MinDivisor(n))
