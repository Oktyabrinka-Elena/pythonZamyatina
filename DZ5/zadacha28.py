# ## Задача 28: 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
# 4 

import random

A = random.randint(0,10)
B = random.randint(0,10)

def sum(B, A):
    if B == 0:
        return A
    else:
        return sum(B - 1 , A + 1)
    
print(sum(B , A))
print(B)
print(A)