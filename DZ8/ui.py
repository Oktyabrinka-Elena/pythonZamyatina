# взаимодействие с пользователем
from script import input_data, delete_data, put_data, print_data

def interface():
    print('Привет! вы тут! Можем!\n'
          '1.Записать данные в 2х форматах \n'
          '2.Удалить данные \n'
          '3.Изменить данные \n'
          '4.Вывести данные \n')
    command = int(input("Введите номер операции: "))
# interface()

    while command < 1 or command > 4:
        print('Неверно. Повторите')
        command = int(input("Введите номер операции: "))
    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()            
  