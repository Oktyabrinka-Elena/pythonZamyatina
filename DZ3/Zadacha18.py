# ## Задача 18: 

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5 - количество элементов в массиве
#1 2 3 4 5 - массив
#6 - заданное число
#-> 5 - ближайшее число

# Код не работает пока нормально. Я переделаю =)

import random
print('введите количество элементов массива -  ')
N = int(input())
Array = [random.randint(0, 9) for _ in range(N)]    #создаём массив
print(Array) #для проверки с результатом
if len(Array) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - Array[0])
    index = 0
    for i in range(1, N):
        count = abs(X - Array[i])
        if count < min:
            min = count
            index = i
    print(f'Число {Array[index]} в списке ближайшее к числу {X}, их разница равна {abs(X - Array[index])}')