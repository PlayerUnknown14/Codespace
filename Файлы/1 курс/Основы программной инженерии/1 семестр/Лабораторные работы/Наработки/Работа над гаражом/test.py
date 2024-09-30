from prettytable import *
table = PrettyTable()
table.field_names = ['Mark', 'Model','Year of model', 'Colour', 'HP', 'Car mileage']
mark = ''
model = ''
yearofmodel = ''
colour = ''
hp = ''

def dobavl():
    mark = input('Введите марку: ')
    model = input('Введите модель: ')
    yearofmodel = input('Введите год выпуска авто: ')
    colour = input('Введите цвет: ')
    hp = input('Введите лошадиные силы: ')
    carmile = input('Введите пробег авто: ')
    return mark, model, yearofmodel, colour, hp, carmile

def clear():
    mark = ''
    model = ''
    yearofmodel = ''
    colour = ''
    hp = ''
    return mark, model, yearofmodel, colour, hp, carmile
def delete(self):
    self.Number = ''
    self.Brand = ''
    self.Model = ''
    self.Ton = ''
    self.Color = ''
    self.Type_of_engine = ''
    list[j1] = self.Number
    list[j1 + 1]= self.Brand
    list[j1 + 2]=self.Model
    list[j1 + 3]=self.Ton
    list[j1 + 4]=self.Color
    list[j1 + 5]=self.Type_of_engine
    print(list)
    for i in range(0,len(list)):
        list[i]=list[i]+' '
    with open(r'C:\Users\luvid\OneDrive\Desktop\python\Codespace\Файлы\1 курс\Основы программной инженерии\1 семестр\Лабораторные работы\Наработки\Работа над гаражом\garage.txt', 'w') as f:
        f.writelines(list)
def change():
    return 0

while True:
    deystv = input('1. Добавить автомобиль\n2.Редактировать автомобиль\n3. Удалить автомобиль\n0. Завершить программу\nВведите число 0-3 для выполнения действий:  ')
    if deystv!="0" and deystv!="1" and deystv!="2" and deystv!="3":
        print('Число введено неверно. Такого действия нет')
    if deystv == "1":
        mark, model, yearofmodel, colour, hp, carmile = dobavl()
        table.add_row([mark, model, yearofmodel, colour, hp, carmile])
        mark, model, yearofmodel, colour, hp, carmile = clear()
        print(table)
    if deystv == "3":
        print(table)
        with open(r'C:\Users\luvid\OneDrive\Desktop\python\Codespace\Файлы\1 курс\Основы программной инженерии\1 семестр\Лабораторные работы\Наработки\Работа над гаражом\garage.txt', 'r') as f:
            x = f.read()
        list = x.split()
        t = PrettyTable(['Номер ', 'Марка ', 'Модель ', 'Тонировка ', 'Цвет ', 'Тип_двигателя '])
        t.padding_width = 1
        i = (len(lst) + 1) / 6
        j = 0
        m = 6
        for i1 in range(0, int(i)):
            t.add_row(lst[j:m])
            j = j + 6
            m = m + 6
        print(t)
        j=0
        m=6
        c=0
        b=input('Введите номер строки машины, которую хотите удалить: ')
        for i1 in range(0, int(i)):
            try:
                c=1
            j1=j
            j = j + 6
            m = m + 6
        if c == 1:
            gar = Garage(lst[j1],lst[j1+1],lst[j1+2],lst[j1+3],lst[j1+4],lst[j1+5])
            gar.delete()
        if c == 0:
            print('Машины с таким регестрационным номером нет.\n')
        try:
            delete(nor)
        except IndexError:
            print("Машины с таким номером в списке нет")
    if deystv == "0":
        break