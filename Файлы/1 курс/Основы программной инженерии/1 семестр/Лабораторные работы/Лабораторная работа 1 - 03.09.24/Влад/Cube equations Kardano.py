#Решение кубического уравнения через формулу Кардано
#Получаем коэффиценты степенного уравнения >> выводим корни уравнения
#Проверяем корни, подставляем в уравнение
import cmath

#================================

def Input_koefs():
    while True:
        try:
            a, b, c, d = map(float, input("Введите коэффиценты a, b, c, d (через запятую): ").split(", "))
            break
        except ValueError:
            print("Ошибка: некорректый ввод")
        except ZeroDivisionError:
            print("Ошибка: введённые коэффиценты равны нулю")
    return a, b, c, d

def solve_cubic(a, b, c, d):
    #Находим коэффиценты p, q, а также дискриминат
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
    Disc = (q/2)**2 + (p/3)**3
    #Оцениваем коэффицент q, находим коэффицент f
    if q < 0:
        f = cmath.atan((cmath.sqrt(-Disc))/(-(q/2)))
    elif q > 0:
        f = cmath.atan((cmath.sqrt(-Disc))/(-(q/2))) + cmath.pi
    else:
        f = cmath.pi / 2
    #Оцениваем дискриминат, находим и возвращаем значения корней
    if Disc > 0:
        Alfa = (-q / 2 + Disc ** 0.5) ** (1 / 3)
        Beta = -abs((-q / 2 - Disc ** 0.5) ** (1 / 3))
        y1 = Alfa + Beta
        y2 = complex(-((Alfa + Beta) / 2), (Alfa - Beta) / 2 * 3 ** 0.5)
        y3 = complex(-((Alfa + Beta) / 2), -(Alfa - Beta) / 2 * 3 ** 0.5)
        x1 = y1 - b / (3 * a)
        x1 = round(x1.real, 5)
        x2 = y2 - b / (3 * a)
        x2 = round(x2.real, 5) + round(x2.imag, 5) * 1j
        x3 = y3 - b / (3 * a)
        x3 = round(x3.real, 5) + round(x3.imag, 5) * 1j                
    elif Disc < 0:
        x1 = 2 * (-p / 3)**0.5 * cmath.cos(f / 3) - b / (3 * a)
        x1 = round(x1.real, 5) 
        x2 = 2 * (-p / 3)**0.5 * cmath.cos((f / 3) + 2 * cmath.pi / 3) - b / (3 * a)
        x2 = round(x2.real, 5)
        x3 = 2 * (-p / 3)**0.5 * cmath.cos((f / 3) + 4 * cmath.pi / 3) - b / (3 * a)
        x3 = round(x3.real, 5)
    else:
        x1 = 2 * (-q / 2) ** (1 / 3) - b / (3 * a)
        x2 = (-q / 2) ** (-1 / 3) - b / (3 * a)
        x3 = (-q / 2) ** (-1 / 3) - b / (3 * a)
    return x1, x2, x3        
    
#================================

#Запрашиваем у пользователя коэффциенты уравнения, находим корни, выводим их
a, b, c, d = Input_koefs()
x1, x2, x3 = solve_cubic(a, b, c, d)
print(f"\n\nКорни уравнения: {x1}; {x2}; {x3}")

#Проверяем найденные корни, подставляя их в уравнение
if      (a * x1**3 + b * x1**2 + c * x1 + d) == 0\
    and (a * x2**3 + b * x2**2 + c * x2 + d) == 0\
    and (a * x3**3 + b * x3**2 + c * x3 + d) == 0:
        print("Проверка корней, корни подходят.")
        print(a * x1**3 + b * x1**2 + c * x1 + d)
        print(a * x2**3 + b * x2**2 + c * x2 + d)
        print(a * x3**3 + b * x3**2 + c * x3 + d)
else:
    print("Проверка корней, корни не подходят.")
    print(a * x1**3 + b * x1**2 + c * x1 + d)
    print(a * x2**3 + b * x2**2 + c * x2 + d)
    print(a * x3**3 + b * x3**2 + c * x3 + d)