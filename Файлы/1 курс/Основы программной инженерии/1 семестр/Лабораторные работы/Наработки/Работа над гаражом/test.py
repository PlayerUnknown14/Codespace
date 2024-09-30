from prettytable import *
table = PrettyTable()
table.field_names = ['Mark', 'Model', 'Colour', 'HP']
r1 = ''
r2 = ''
r3 = ''
r4 = ''

a = [" ".split(i) for i in open(r'C:\Users\luvid\OneDrive\Desktop\python\random\Работа над гаражом\garage.txt')]
print(a)
def dobavl():
    r1 = input('Введите марку:')
    r2 = input('Введите модель:')
    r3 = input('Введите цвет:')
    r4 = input('Введите лошадиные силы:')
    return r1,r2,r3,r4

def clear():
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    return r1,r2,r3,r4
def delete(n):
    table.del_row(n)
    return "Удалена строка ",n,"\n",print(table)


while True:
    deystv = input('1. Добавить автомобиль\n2.Редактировать автомобиль\n3. Удалить автомобиль\n0. Завершить программу\nВведите число 0-3 для выполнения действий:  ')
    if deystv!="0" and deystv!="1" and deystv!="2" and deystv!="3":
        print('Число введено неверно. Такого действия нет')
    if deystv == "1":
        r1,r2,r3,r4 = dobavl()
        table.add_row([r1,r2,r3,r4])
        r1,r2,r3,r4 = clear()
        print(table)
    if deystv == "3":
        print(table)
        nor = int(input('Введите номер строки машины, которую хотите удалить: '))
        delete(nor)
    if deystv == "0":
        break