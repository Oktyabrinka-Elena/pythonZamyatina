# ## Задача 18: 

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5 - количество элементов в массиве
#1 2 3 4 5 - массив
#6 - заданное число
#-> 5 - ближайшее число

import random
print('введите количество элементов массива -  ')
N = int(input())
Array = [random.randint(0, 9) for _ in range(N)]    #создаём массив
print('число, которое ищем в массиве -  ')
Ai = int(input())

