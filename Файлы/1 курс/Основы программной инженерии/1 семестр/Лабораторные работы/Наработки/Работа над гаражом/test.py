from prettytable import PrettyTable

class garage():
    def __init__(self, number, mark, model, yearofmodel, color, hp):
        self.number = number
        self.mark = mark
        self.model = model
        self.yearofmodel = yearofmodel
        self.color = color
        self.hp = hp
    def change(self):
        par = input("Введите параметр, что хотите изменить: ")
        match par.split():
            case ["Номер"]:
                inp = input("Введите изменённый номер автомобиля: ")
                while True:
                    if num in S:
                        inp = input("Номер уже находится в базе данных. Введите другой номер: ") 
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
                self.yearofmodel = inp
                S[first+3] = self.yearofmodel
            case ["Цвет"]:
                imp = input('Введите новый цвет автомобиля: \n')
                self.color = imp
                S[first+4] = self.color
            case ["Мощность"]:
                imp = input('Введите новое значение мощности двигателя автомобиля: \n')
                self.hp = imp
                S[first+5] = self.hp
                
        for i in range(0,len(S)):
            S[i]=S[i]+' '
        with open('cars_table.txt', 'w') as f:
            f.writelines(S)
    def delete(self):
        self.number = ''
        self.mark = ''
        self.model = ''
        self.yearofmodel = ''
        self.color = ''
        self.hp = ''
        S[first] = self.number
        S[first + 1]= self.mark
        S[first + 2]=self.model
        S[first + 3]=self.yearofmodel
        S[first + 4]=self.color
        S[first + 5]=self.hp
        print(S)
        for i in range(0,len(S)):
            S[i]=S[i]+' '
        with open('cars_table.txt', 'w') as f:
            f.writelines(S)

while True:
    option = input("Выберите нужную опцию:\n\n\t1. Вывести таблицу\n\t2. Добавить автомобиль\n\t3. Изменить автомобить\n\t4. Удалить автомобиль\n\t5. Найти автомобиль в таблице\n\t6. Закрыть программу\n")
    match option.split():
        case ["1"]:#вывести таблицу
            table = PrettyTable(["Номер", "Марка", "Модель", "Тип двигателя", "Цвет", "Мощность"])
            with open("cars_table.txt", "r") as t:
                S = t.read().split()
            length = (len(S) + 1) / 6
            first = 0
            last = 6
            for i in range(0, int(length)):
                table.add_row(S[first:last])
                first += 6
                last += 6
            print(table)
        case ["2"]:#добавить авто
            with open ("cars_table.txt", "r") as t:
                S = t.read().split()
            num = input("Введите новый регистрационный номер автомобиля: \n")
            while True:
                if num in S:
                    num = input("Данный регистрационный номер уже находится в базе данных.\nПожалуйста, введите другой номер: \n") 
                else:
                    break
            mark = input('Введите новую марку автомобиля: \n')
            model = input('Введите новую модель автомобиля: \n')
            yearofmodel = input("Введите новый тип двигателя автомобиля - внутреннего сгорания (1), электродвигатель (2), гибридный (3): \n")
            while True:
                if yearofmodel != "1" and yearofmodel != "2" and yearofmodel != "3":
                    print("Введено неправильное значение.\n")
                    yearofmodel = input("Введите новый тип двигателя автомобиля - внутреннего сгорания (1), электродвигатель (2), гибридный (3): \n")
                else:
                    break
            match yearofmodel.split():
                case ["1"]: inp = "Внутреннего сгорания"
                case ["2"]: inp = "Электродвигатель"
                case ["3"]: inp = "Гибридный"
            color = input('Введите новый цвет автомобиля: \n')
            hp = input('Введите новое значение мощности двигателя автомобиля: \n')
            S_add = [num,' ', mark,' ', model,' ', yearofmodel,' ', color,' ', hp,' ']
            with open ("cars_table.txt", "a") as t:
                t.writelines(S_add)
        case ["3"]:#изменить авто
            with open ("cars_table.txt", "r") as t:
                S = t.read().split()
            num = input("Введите регистрационный номер нужного автомобиля: \n")
            while True:
                if num in S:
                    break
                else:
                    inp = input("Автомобиль с таким номером отсутствует в базе данных.\nПожалуйста, введите другой номер: \n")        
            length = (len(S) + 1) / 6
            first = 0
            for i in range(1, int(length)):
                first += 6
            car = Car(S[first], S[first + 1], S[first + 2], S[first + 3], S[first + 4], S[first + 5])
            car.change()
        