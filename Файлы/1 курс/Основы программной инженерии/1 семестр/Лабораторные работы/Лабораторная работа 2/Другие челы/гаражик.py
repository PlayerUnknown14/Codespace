class Garage():
    def __init__(self,Number,Brand,Model,Ton,Color,Type_of_engine):
        self.Number=Number
        self.Brand=Brand
        self.Model = Model
        self.Ton=Ton
        self.Color=Color
        self.Type_of_engine=Type_of_engine
    def delete(self):
        self.Number = ''
        self.Brand = ''
        self.Model = ''
        self.Ton = ''
        self.Color = ''
        self.Type_of_engine = ''
        lst[j1] = self.Number
        lst[j1 + 1]= self.Brand
        lst[j1 + 2]=self.Model
        lst[j1 + 3]=self.Ton
        lst[j1 + 4]=self.Color
        lst[j1 + 5]=self.Type_of_engine
        print(lst)
        for i in range(0,len(lst)):
            lst[i]=lst[i]+' '
        with open('garage.txt', 'w') as f:
            f.writelines(lst)
    def izm(self):
        par = input('Какой параметр хотите изменить.\n')
        if par == 'Номер':
            reg = input('Новый номер.\n')
            k=0
            while k == 0:
                if reg in x:
                    reg = input('Такой номер в базе уже есть введите другой.\n')
                if reg not in x:
                    k = 1
            self.Number = reg
            lst[j1] = self.Number
        if par == 'Марка':
            reg = input('Новую марку.\n')
            self.Brand = reg
            lst[j1+1] = self.Brand
        if par == 'Модель':
            reg = input('Новую модель\n')
            self.Model = reg
            lst[j1+2] = self.Model
        if par == 'Тонировка':
            reg = input('Новое значение тонировки.\n')
            v = []
            for i in range(0, 100):
                v = v + [str(i)]
            while reg not in v:
                if reg in v:
                    break
                reg = input('!!!Показатель тонировки  должен быть больше или равен 0 и не больше 100\n')
            reg = reg + '%'
            self.Ton = reg
            lst[j1+3] = self.Ton
        if par == 'Цвет':
            reg = input('Новый цвет.\n')
            self.Color = reg
            lst[j1+4] = self.Color
        if par == 'Тип двигателя':
            reg = input('Новый тип двигателя.\n')
            k = 0
            while k == 0:
                if reg != 'электро' and reg != 'гибридный' and reg != 'внутреннего_сгорания':
                    reg = input('Тип двигателя (гибридный, электро, внутреннего_сгорания) вводите в точности как в скобках:\n')
                if reg == 'электро' or reg == 'гибридный' or reg == 'внутреннего_сгорания':
                    k = 1
            self.Type_of_engine = reg
            lst[j1+5]=self.Type_of_engine
        for i in range(0,len(lst)):
            lst[i]=lst[i]+' '
        with open('garage.txt', 'w') as f:
            f.writelines(lst)
    def unit_test(self, par, reg1):
        if par == 'Номер':
            self.Number = reg1
        if par == 'Марка':
            self.Brand = reg1
        if par == 'Модель':
            self.Model = reg1
        if par == 'Тонировка':
            self.Ton = reg1
        if par == 'Цвет':
            self.Color = reg1
        if par == 'Тип двигателя':
            self.Type_of_engine = reg1
        print([self.Number,' ',self.Brand,' ',self.Model,' ',self.Ton,' ',self.Color,' ',self.Type_of_engine])
        if self.Number == reg1 or self.Brand == reg1 or self.Model == reg1 or self.Ton == reg1 or self.Color == reg1 or self.Type_of_engine == reg1:
            print('Юнит тест пройден успешно')
        else:
            print('Юнит тест не пройден')

    def integ1(self):
        par = input('Введите парметр по нему будет выполнен тест\n')
        self.par = par
        reg1 = input('Введите новое значение:\n')
        self.reg1 = reg1
    def integ2(self):
        print([self.Number, ' ', self.Brand, ' ', self.Model, ' ', self.Ton, ' ', self.Color, ' ', self.Type_of_engine])
        if self.par == 'Номер':
            self.Number = self.reg1
        if self.par == 'Марка':
            self.Brand = self.reg1
        if self.par == 'Модель':
            self.Model = self.reg1
        if self.par == 'Тонировка':
            self.Ton = self.reg1
        if self.par == 'Цвет':
            self.Color = self.reg1
        if self.par == 'Тип двигателя':
            self.Type_of_engine = self.reg1
        print([self.Number, ' ', self.Brand, ' ', self.Model, ' ', self.Ton, ' ', self.Color, ' ', self.Type_of_engine])
        if self.Number == self.reg1 or self.Brand == self.reg1 or self.Model == self.reg1 or self.Ton == self.reg1 or self.Color == self.reg1 or self.Type_of_engine == self.reg1:
            print('Интеграционный тест пройден успешно')
        else:
            print('Интеграционный тест не пройден')
while True:
    d=input('1.Добавить машину\n2.Удалить машину\n3.Изменить машину\n4.Вывести список машин\n5.Выполнить поиск\n6.Выйти из проги\n7.Юнит тест\n8.Интеграционный тест\nВведите номер действия:\n')
    if d != '1' and d!='2' and d!='3' and d!='4' and d!='5' and d!='6' and d!= '7' and d!= '8':
        print('такого действия нет')
    if d == '1' or d=='2' or d=='3' or d=='4' or d=='5' or d == '6' or d == '7' or d == '8':
        d = int(d)
        if d == 1:
            c=0
            v = []
            for i in range(0, 100):
                v=v+[str(i)]
            with open ('garage.txt','r') as f:
                x=f.read()
            reg = input('Регистрационный номер:\n')
            while c == 0:
                if reg in x:
                    reg=input('Такой номер в базе уже есть введите другой.\n')
                if reg not in x:
                    c=1
            car = input('Марка:\n')
            door = input('Модель:\n')
            light = input('Тонировка числовое среднее значение(без процентов):\n')
            while light not in v:
                if light in v:
                    break
                light = input('!!!Показатель тонировки  должен быть больше или равен 0 и не больше 100\n')
            light = light + '%'
            color = input('Цвет:\n')
            engine = input('Тип двигателя (гибридный, электро, внутреннего_сгорания) вводите в точности как в скобках:\n')
            c=0
            while c == 0:
                if engine != 'электро' and engine != 'гибридный' and engine != 'внутреннего_сгорания':
                    engine= input('Тип двигателя (гибридный, электро, внутреннего_сгорания) вводите в точности как в скобках:\n')
                if engine == 'электро' or engine == 'гибридный' or engine == 'внутреннего_сгорания':
                    c=1
            list_gar=[reg,car,door,light,color,engine]
            from prettytable import PrettyTable
            t=PrettyTable(['Номер ', 'Марка ', 'Модель ', 'Тонировка ', 'Цвет ', 'Тип_двигателя '])
            t.padding_width=1
            t.add_row(list_gar)
            print(t)
            list_gar = [reg,' ', car,' ', door,' ', light,' ', color,' ', engine,' ']
            with open ('garage.txt','a') as f:
                f.writelines(list_gar)
        if d == 2:
            with open('garage.txt', 'r') as f:
                x = f.read()
            lst = x.split()
            from prettytable import PrettyTable
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
            b=input('Рег. номер.\n')
            for i1 in range(0, int(i)):
                if b in lst[j:m]:
                    c=1
                    j1=j
                j = j + 6
                m = m + 6
            if c == 1:
                gar = Garage(lst[j1],lst[j1+1],lst[j1+2],lst[j1+3],lst[j1+4],lst[j1+5])
                gar.delete()
            if c == 0:
                print('Машины с таким регестрационным номером нет.\n')
        if d == 3:
            with open('garage.txt', 'r') as f:
                x = f.read()
            lst = x.split()
            print(lst)
            from prettytable import PrettyTable
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
            b=input('Рег. номер.\n')
            for i1 in range(0, int(i)):
                if b in lst[j:m]:
                    c=1
                    j1=j
                j = j + 6
                m = m + 6
            if c == 1:
                gar = Garage(lst[j1], lst[j1 + 1], lst[j1 + 2], lst[j1 + 3], lst[j1 + 4], lst[j1 + 5])
                gar.izm()
            if c == 0:
                print('Машины с таким регестрационным номером нет.\n')
        if d == 4:
            from prettytable import PrettyTable
            t = PrettyTable(['Номер ', 'Марка ', 'Модель ', 'Тонировка ', 'Цвет ', 'Тип_двигателя '])
            t.padding_width = 1
            with open('garage.txt', 'r') as f:
                x = f.read()
            lst = x.split()
            i = (len(lst) + 1) / 6
            j=0
            m=6
            for i1 in range(0, int(i)):
                t.add_row(lst[j:m])
                j = j + 6
                m = m + 6
            print(t)
        if d == 5:
            with open('garage.txt', 'r') as f:
                x = f.read()
            lst = x.split()
            from prettytable import PrettyTable
            t = PrettyTable(['Номер ', 'Марка ', 'Модель ', 'Тонировка ', 'Цвет ', 'Тип_двигателя '])
            t.padding_width = 1
            i = (len(lst) + 1) / 6
            j = 0
            m = 6
            c = 0
            while c == 0:
                stop = ''
                while stop != 'стоп':
                    v = input('введите параметры до 6 штук по ним будет выведем список машин удовлетворяющих этим параметрам\n')
                    stop = input('Напишите <стоп> если парметров достаточно\n')
                for i1 in range(0, int(i)):
                    if v in str(lst[j:m]):
                        t.add_row(lst[j:m])
                        c = 1
                    j = j + 6
                    m = m + 6
                if c == 1:
                    print('Результат поиска:\n', t)
                if c == 0:
                    print('Таких машин нет')
                    c = 1
        if d == 6:
            print('Вы вышли')
            break
        if d == 7:
            reg = '1dfg56'
            car = 'Lada'
            door = 'Granta'
            light = '23%'
            color = 'red'
            engine = 'электро'
            print('Начальная машинка:\n ',[reg,' ',car,' ',door,' ',light,' ',color,' ',engine])
            par = input('Введите парметр по нему будет выполнен тест\n')
            gar = Garage(reg, car, door, light, color, engine)
            reg1 = input('Введите новое значение:\n')
            print('Будет замена на:\n ', reg1)
            gar.unit_test(par, reg1)
        if d == 8:
            reg = '1dfg56'
            car = 'Lada'
            door = 'Granta'
            light = '23%'
            color = 'red'
            engine = 'электро'
            gar = Garage(reg, car, door, light, color, engine)
            gar.integ1()
            gar.integ2()

