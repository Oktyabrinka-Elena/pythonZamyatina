# ## Задача 18: 

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5 - количество элементов в массиве
#1 2 3 4 5 - массив
#6 - заданное число
#-> 5 - ближайшее число

# Код не работает пока. Я переделаю =)

import random
print('введите количество элементов массива -  ')
N = int(input())
Array = [random.randint(0, 9) for _ in range(N)]    #создаём массив
Array.sort() # сортируем по увеличению список
print('число, которое ищем в массиве -  ')
X = int(input())

if len(Array) < X:
    print(f'{Array[-1]}')
else:
    min = X - Array[0]
    i = 0
    for j in range(1,N):
        count = X - Array[j]
        if count < min:
            min = count
            i = j
    print(f'Ближайшее число равно {Array[i]} ')
    print(f'{Array}')       
