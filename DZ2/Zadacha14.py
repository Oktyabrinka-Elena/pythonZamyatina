# **Задача 14:**
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

N = abs(int(input('Введите число N ')))
Row = 0
P = 2
for i in range(N):
    if Row != 1:
        P = P ** i
        if P <= N:
            print(P, end=' ')
            P = 2
        else:
            Row = 1
    else:
        i = N

