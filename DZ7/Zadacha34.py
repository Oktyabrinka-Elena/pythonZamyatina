# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

print('Введите текст кричалки') # ВВОДИМ ТЕКСТ КРИЧАЛКИ
list = input().split(',')
new_list = [x.upper() for x in list] #ПЕРЕВОДИМ ТЕКСТ КРИЧАЛКИ В ЕДИНООБРАЗНОЕ ЗНАЧЕНИЕ

# temp = ['Б', 'В', 'Г','Д','Ж','З','Й','К','Л','М','Н','П','Р','С','Т','Ф','Х','Ц','Ч','Ш','Щ']
temp = ['БВГДЖЗЙКЛМНПРСТФХЦЧШЩ']

filtered_list = ' '.join((filter(lambda s: s not in temp, new_list)))
filtered_list =  filtered_list #.split()

print(filtered_list)