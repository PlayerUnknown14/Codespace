#To-do:
#Сделать функцию-инициализацию: прогон файла и занесение в таблицу
from prettytable import PrettyTable
class Car():
    def __init__(self, number, mark, model, yearofmodel, color, hp, carmile):
        self.number = number
        self.mark = mark
        self.model = model
        self.yearofmodel = yearofmodel
        self.color = color
        self.hp = hp
        self.carmile = carmile
    def inittable():
        table = PrettyTable(["Номер", "Марка", "Модель", "Год выпуска", "Цвет", "Лошадиные силы", "Пробег, км"])
        with open("garage.txt", "r") as t:
            S = t.read().split()
        length = (len(S) + 1) / 7
        first = 0
        last = 7
        for i in range(0, int(length)):
            table.add_row(S[first:last])
            first += 7
            last += 7
        return(print(table))
    def change(self):
        parameter = input("Какой параметр вы хотите изменить?\n")
        match parameter.split():
            case ["Номер"]:
                inp = input("Введите изменённый регистрационный номер автомобиля: ")
                while True:
                    if inp in S:
                        inp = input("Данный регистрационный номер уже находится в базе данных.\nПожалуйста, введите другой номер: ") 
                    else:
                        break
                self.number = inp
                S[first] = self.number
            case ["Марка"]:
                imp = input('Введите изменённую марку автомобиля: ')
                self.mark = imp
                S[first+1] = self.mark
            case ["Модель"]:
                imp = input('Введите изменённую модель автомобиля: ')
                self.model = imp
                S[first+2] = self.model
            case ["Год выпуска"]:
                inp = input("Введите изменённый год выпуска: ")
                self.yearofmodel = inp
                S[first+3] = self.yearofmodel
            case ["Цвет"]:
                imp = input('Введите новый цвет автомобиля: ')
                self.color = imp
                S[first+4] = self.color
            case ["Лошадиные силы"]:
                imp = input('Введите изменённый показатель ЛС: ')
                self.hp  = imp
                S[first+5] = self.hp
            case ["Пробег авто"]:
                imp = input('Введите изменённый показатель пробега автомобиля: ')
                self.carmile = imp
                S[first+6] = self.carmile
                
        for i in range(0,len(S)):
            S[i]=S[i]+' '
        with open('garage.txt', 'w') as f:
            f.writelines(S)
    def delete(self):
        self.number = ''
        self.mark = ''
        self.model = ''
        self.yearofmodel = ''
        self.color = ''
        self.hp  = ''
        self.carmile = ''
        S[first] = self.number
        S[first + 1]= self.mark
        S[first + 2]=self.model
        S[first + 3]=self.yearofmodel
        S[first + 4]=self.color
        S[first + 5]=self.hp
        S[first + 6]=self.carmile
        for i in range(0,len(S)):
            S[i]=S[i]+' '
        with open('garage.txt', 'w') as f:
            f.writelines(S)
        

while True:
    option = input("Выберите нужную опцию:\n1. Вывести таблицу\n2. Добавить автомобиль\n3. Изменить автомобить\n4. Удалить автомобиль\n5. Поиск по параметру\n0. Закрыть программу\n")
    match option.split():
        case ["1"]:#вывести таблицу
            Car.inittable()
        case ["2"]:#добавить авто
            with open ("garage.txt", "r") as t:
                S = t.read().split()
            length = (len(S)+1)/7
            num = input("Введите новый регистрационный номер автомобиля: ")
            while True:
                for i in range(0, int(length)*6, 6):
                    if num == S[i]:
                        num = input("Данный регистрационный номер уже находится в базе данных.\nПожалуйста, введите другой номер: ") 
                else:
                    break
            mark = input('Введите новую марку автомобиля: ')
            model = input('Введите новую модель автомобиля: ')
            yearofmodel = input('Введите новый год выпуска: ')
            color = input('Введите новый цвет автомобиля: ')
            hp  = input('Введите новое значение мощности двигателя автомобиля: ')
            carmile = input('Введите новый показатель пробега авто, км: ')
            S_add = [num,' ', mark,' ', model,' ', yearofmodel,' ', color,' ', hp,' ', carmile,' ']
            with open ("garage.txt", "a") as t:
                t.writelines(S_add)
            print('Таблица после добавления:\n')
            Car.inittable()
        case ["3"]:#изменить авто
            with open ("garage.txt", "r") as t:
                S = t.read().split()
            num = input("Введите регистрационный номер нужного автомобиля: \n")
            length = (len(S) + 1) / 7
            first = 0
            while True:
                for i in range(0, int(length)*7, 7):
                    if num == S[i]:
                        first = i
                        break
                if num == S[i]:
                    break
                else:
                    num = input("Автомобиль с таким номером отсутствует в базе данных.\nПожалуйста, введите другой номер: \n")   
            car = Car(S[first], S[first + 1], S[first + 2], S[first + 3], S[first + 4], S[first + 5], S[first + 6])
            car.change()
            print('Таблица после изменений:\n')
            Car.inittable()
        case ["4"]:#удаление авто
            with open ("garage.txt", "r") as t:
                S = t.read().split()
            length = (len(S) + 1) / 7
            first = 0
            num = input("Введите регистрационный номер нужного автомобиля: \n")
            while True:
                for i in range(0, int(length)*7, 7):
                    if num == S[i]:
                        first = i
                        break
                if num == S[i]:
                    break
                else:
                    num = input("Автомобиль с таким номером отсутствует в базе данных.\nПожалуйста, введите другой номер: \n")
            car = Car(S[first], S[first + 1], S[first + 2], S[first + 3], S[first + 4], S[first + 5], S[first + 6])
            car.delete()
            print('Таблица после удаления:\n')
            Car.inittable()
        case ["5"]:
            with open("garage.txt","r") as t:
                S = t.read().split()
            tablesearch = PrettyTable(["Номер", "Марка", "Модель", "Год выпуска", "Цвет", "Лошадиные силы", "Пробег, км"])
            searchpar = input('Введите параметр, по которому хотите произвести поиск: ')
            length = (len(S) + 1) / 7
            for i in range(0, int(length)*7, 7):
                if searchpar in S[i:i+7]:
                    tablesearch.add_row(S[i:i+7])
            print(tablesearch)
        case ["0"]:
            print("Вы вышли из программы.")
            break