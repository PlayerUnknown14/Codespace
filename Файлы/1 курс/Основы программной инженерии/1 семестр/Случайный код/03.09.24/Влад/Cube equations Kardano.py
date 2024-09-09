#Решение кубического уравнения через формулу Кардано
#Получаем коэффиценты степенного уравнения >> выводим корни уравнения
import cmath

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
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
    Disc = (q/2)**2 + (p/3)**3
    if q < 0:
        f = cmath.atan((cmath.sqrt(-Disc))/(-(q/2)))
    elif q > 0:
        f = cmath.atan((cmath.sqrt(-Disc))/(-(q/2))) + cmath.pi
    else:
        f = cmath.pi / 2
    
    if Disc > 0:
        Alfa = (-q / 2 + Disc ** 0.5) ** (1 / 3)
        Beta = -abs((-q / 2 - Disc ** 0.5) ** (1 / 3))
        y1 = Alfa + Beta
        y2 = complex(-((Alfa + Beta) / 2), (Alfa - Beta) / 2 * 3 ** 0.5)
        y3 = complex(-((Alfa + Beta) / 2), -(Alfa - Beta) / 2 * 3 ** 0.5)
        x1 = y1 - b / (3 * a)
        x1 = round(x1, 5)
        x2 = y2 - b / (3 * a)
        x2 = round(x2.real, 5) + round(x2.imag, 5) * 1j
        x3 = y3 - b / (3 * a)
        x3 = round(x3.real, 5) + round(x3.imag, 5) * 1j        
        print(f"Уравнение имеет 3 корня: x1 = {x1}, x2 = {x2}, x3 = {x3}")        
    elif Disc < 0:
        x1 = 2 * (-p / 3)**0.5 * cmath.cos(f / 3) - b / (3 * a)
        x1 = round(x1.real, 5) 
        x2 = 2 * (-p / 3)**0.5 * cmath.cos((f / 3) + 2 * cmath.pi / 3) - b / (3 * a)
        x2 = round(x2.real, 5)
        x3 = 2 * (-p / 3)**0.5 * cmath.cos((f / 3) + 4 * cmath.pi / 3) - b / (3 * a)
        x3 = round(x3.real, 5)
        print(f"Уравнение имеет 3 корня: x1 = {x1}, x2 = {x2}, x3 = {x3}")
    else:
        x1 = 2 * (-q / 2) ** (1 / 3) - b / (3 * a)
        x2 = (-q / 2) ** (-1 / 3) - b / (3 * a)
        x3 = (-q / 2) ** (-1 / 3) - b / (3 * a)
        print(f"Уравнение имеет 3 корня: x1 = {x1}, x2 = {x2}, x3 = {x3}")        

    
#================================

a, b, c, d = Input_koefs()
solve_cubic(a, b, c, d)