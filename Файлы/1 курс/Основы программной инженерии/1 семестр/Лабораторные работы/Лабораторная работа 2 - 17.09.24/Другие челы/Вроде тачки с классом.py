from prettytable import PrettyTable
class Garage():
    def __init__(self,lst):
        self.lst=lst
    def search(self):
        global i,k,lst,t
        with open('garage1.txt', 'r') as f:
            x = f.read()
        lst = x.split()
        t = PrettyTable(['Номер ', 'Марка ', 'Модель ', 'Тонировка ', 'Цвет ', 'Тип_двигателя '])
        t.padding_width = 1
        i = (len(lst) + 1) / 6
        j = 0
        m = 6
        c = 0
        k=0
        while c == 0:
            stop = ''
            v1 = ' '
            v2 = ' '
            v3 = ' '
            v4 = ' '
            v5 = ' '
            while stop != 'стоп':
                v = input('введите параметры до 6 штук по ним будет выведем список машин удовлетворяющих этим параметрам\n')
                stop = input('Напишите <стоп> если парметров достаточно\n')
            for i1 in range(0, int(i)):
                if v in str(lst[j:m]) and v1 in str(lst[j:m]) and v2 in str(lst[j:m]) and v3 in str(lst[j:m]) and v4 in str(lst[j:m]) and v5 in str(lst[j:m]):
                    t.add_row(lst[j:m])
                    k = k + 1
                    c = 1
                j = j + 6
                m = m + 6
            if c == 1:
                print('Результат поиска:\n', t)
            if c == 0:
                print('Таких машин нет')
                c = 1
    def delete(self):
        b = input('Введите рег. номер машины, которую хотите удалить.\n')
        i = (len(lst) + 1) / 6
        j = 0
        m = 6
        for i1 in range(0, int(i)):
            if b in str(lst[j:m]):
                del lst[j:m]
            j = j + 6
            m = m + 6
        for i in range(0, len(lst)):
            lst[i] = lst[i] + ' '
        with open('garage1.txt', 'w') as f:
            f.writelines(lst)
    def izm(self):
        b = input('Введите рег. номер машины, которую хотите удалить.\n')
        j = 0
        m = 6
        c = 0
        i = (len(lst) + 1) / 6
        for i1 in range(0, int(i)):
            if b in str(lst[j:m]):
                c = 1
                lst1 = lst[j:m]
                j1 = j
                m1 = m
            j = j + 6
            m = m + 6
        if c == 1:
            t = PrettyTable(['Номер ', 'Марка ', 'Модель ', 'Тонировка ', 'Цвет ', 'Тип_двигателя '])
            t.padding_width = 1
            t.add_row(lst1)
            print(t)
            par = input('Какой параметр хотите изменить\n')
            if par == 'Номер':
                par1 = input('Введите новый номер\n')
                c = 0
                while c == 0:
                    if par1 in x:
                        par1 = input('Такой номер в базе уже есть введите другой.\n')
                    if par1 not in x:
                        c = 1
                lst1[0] = par1
            if par == 'Марка':
                par1 = input('Введите новую марку\n')
                lst1[1] = par1
            if par == 'Модель':
                par1 = input('Введите новую модель\n')
                lst1[2] = par1
            if par == 'Тонировка':
                v = []
                for i in range(0, 99):
                    v = v + [str(i)]
                par1 = input('Введите новый показатель тонировки\n')
                while par1 not in v:
                    if par1 in v:
                        break
                    par1 = input('!!!Показатель тонировки  должен быть больше или равен 0 и не больше 100\n')
                par1 = par1 + '%'
                lst1[3] = par1
            if par == 'Цвет':
                par1 = input('Введите новый цвет\n')
                lst1[4] = par1
            if par == 'Тип двигателя':
                par1 = input('Введите новый тип двигателя\n')
                c = 0
                while c == 0:
                    if par1 != 'электро' and par1 != 'гибридный' and par1 != 'внутреннего_сгорания':
                        par1 = input(
                            'Тип двигателя (гибридный, электро, внутреннего_сгорания) вводите в точности как в скобках:\n')
                    if par1 == 'электро' or par1 == 'гибридный' or par1 == 'внутреннего_сгорания':
                        c = 1
                lst1[5] = par1
            lst[j1:m1] = lst1
            t = PrettyTable(['Номер ', 'Марка ', 'Модель ', 'Тонировка ', 'Цвет ', 'Тип_двигателя '])
            t.padding_width = 1
            t.add_row(lst1)
            print(t)
            for i in range(0, len(lst)):
                lst[i] = lst[i] + ' '
            with open('garage1.txt', 'w') as f:
                f.writelines(lst)
        if c == 0:
            print('Машины с таким номером нет.\n')