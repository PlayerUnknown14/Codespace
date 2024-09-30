 #ТЗ: создать приложение - таблица, содержащая в себе характеристики различных автомобилей. Возможность изменять данные в таблице. Использовать фреймворки в коде

from prettytable import PrettyTable

class Car():
    def __init__(self, number, brand, model, engine_type, color, power):
        self.number = number
        self.brand = brand
        self.model = model
        self.engine_type = engine_type
        self.color = color
        self.power = power
    def delete(self):
        self.number = ''
        self.brand = ''
        self.model = ''
        self.engine_type = ''
        self.color = ''
        self.power = ''
        list[n1] = self.number
        list[n1 + 1]= self.brand
        list[n1 + 2]=self.model
        list[n1 + 3]=self.engine_type
        list[n1 + 4]=self.color
        list[n1 + 5]=self.power
        print(list)
        for i in range(0,len(list)):
            list[i]=list[i]+' '
        with open(r'Codespace\Файлы\1 курс\Основы программной инженерии\1 семестр\Лабораторные работы\Наработки\Работа над гаражом\garage.txt', 'w') as f:
            f.writelines(list)
    def change(self):
        parameter = input("Какой параметр вы хотите изменить?\n")
        match parameter.split():
            case ["Номер"]:
                inp = input("Введите новый регистрационный номер автомобиля: \n")
                while True:
                    if num in S:
                        inp = input("Данный регистрационный номер уже находится в базе данных.\n\
                                    Пожалуйста, введите другой номер: \n") 
                    else:
                        break
                self.number = inp
                list[n1] = self.number
            case ["Марка"]:
                imp = input('Введите новую марку автомобиля: \n')
                self.brand = imp
                list[n1+1] = self.brand
            case ["Модель"]:
                imp = input('Введите новую модель автомобиля: \n')
                self.model = imp
                list[n1+2] = self.model
            case ["Тип двигателя"]:
                inp = input("Введите новый тип двигателя автомобиля - внутреннего сгорания (1), электродвигатель (2), гибридный (3): \n")
                while True:
                    if inp != "1" and inp != "2" and inp != "3":
                        print("Введено неправильное значение.\n")
                        inp = input("Введите новый тип двигателя автомобиля - \
                                     внутреннего сгорания (1), электродвигатель (2), гибридный (3): \n")
                    else:
                        break
                if inp == "1": inp = "Внутреннего сгорания"
                elif inp == "2": inp = "Электродвигатель"
                elif inp == "3": inp = "Гибридный"
                self.engine_type = inp
                list[n1+3] = self.engine_type
            case ["Цвет"]:
                imp = input('Введите новый цвет автомобиля: \n')
                self.color = imp
                list[n1+4] = self.color
            case ["Мощность"]:
                imp = input('Введите новое значение мощности двигателя автомобиля: \n')
                self.power = imp
                list[n1+5] = self.power
                
        for i in range(0,len(list)):
            list[i]=list[i]+' '
        with open(r'Codespace\Файлы\1 курс\Основы программной инженерии\1 семестр\Лабораторные работы\Наработки\Работа над гаражом\garage.txt', 'w') as f:
            f.writelines(list)
    
while True:
    option = input("Выберите нужную опцию:\n\n\
                1. Вывести таблицу\n\
                2. Добавить автомобиль\n\
                3. Изменить автомобить\n\
                4. Удалить автомобиль\n\
                5. Найти автомобиль в таблице\n\
                6. Закрыть программу\n")
    match option.split():
        case ["1"]:
            table = PrettyTable(["Номер", "Марка", "Модель", "Тип двигателя", "Цвет", "Мощность"])
            with open(r"Codespace\Файлы\1 курс\Основы программной инженерии\1 семестр\Лабораторные работы\Наработки\Работа над гаражом\garage.txt", "r") as t:
                S = t.read().split()
            length = (len(S) + 1) / 6
            first = 0
            last = 6
            for i in range(0, int(length)):
                table.add_row(S[first:last])
                first += 6
                last += 6
            print(table)
        case ["2"]:
            with open(r"Codespace\Файлы\1 курс\Основы программной инженерии\1 семестр\Лабораторные работы\Наработки\Работа над гаражом\garage.txt", "r") as t:
                S = t.read()
            num = input("Введите новый регистрационный номер автомобиля: \n")
            while True:
                if num in S:
                   inp = input("Данный регистрационный номер уже находится в базе данных.\n\
                                Пожалуйста, введите другой номер: \n") 
                else:
                    break
            brand = input('Введите новую марку автомобиля: \n')
            model = input('Введите новую модель автомобиля: \n')
            engine_type = input("Введите новый тип двигателя автомобиля - \
                         внутреннего сгорания (1), электродвигатель (2), гибридный (3): \n")
            while True:
                if engine_type != "1" and engine_type != "2" and engine_type != "3":
                    print("Введено неправильное значение.\n")
                    engine_type = input("Введите новый тип двигателя автомобиля - внутреннего сгорания (1), электродвигатель (2), гибридный (3): \n")
                else:
                    break
            if engine_type == "1": inp = "Внутреннего сгорания"
            elif engine_type == "2": inp = "Электродвигатель"
            elif engine_type == "3": inp = "Гибридный"
            color = input('Введите новый цвет автомобиля: \n')
            power = input('Введите новое значение мощности двигателя автомобиля: \n')
            list_add = [num,' ', brand,' ', model,' ', engine_type,' ', color,' ', power,' ']
            with open (r"Codespace\Файлы\1 курс\Основы программной инженерии\1 семестр\Лабораторные работы\Наработки\Работа над гаражом\garage.txt", "a") as t:
                t.writelines(list_add)
                