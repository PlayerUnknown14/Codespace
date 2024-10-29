#Получаем коэффиценты степенного уравнения >> выводим корни уравнения

#ТЗ: ввести 3 коэффицента a, b, c и получить корни x1 и x2; защита от ввода букв вместо цифр

def Check():
    while True:
        try:
            inp = input("\nВведите коэффиценты a, b, c (через пробел): ")
            a, b, c = map(float, inp.split(" "))
            break
        except ValueError:
            print("Некорректый ввод")
    return a, b, c

def Solve(a, b, c):
    Dis = b**2 - 4 * a * c
    if Dis == 0:
        x1 = int(-b / 2 * a)
        x2 = x1
        return x1, x2
    elif Dis < 0:
        return "Нет корней"
    else:
        x1 = (-b + Dis**0.5) / (2 * a)
        x2 = (-b - Dis**0.5) / (2 * a)
        return x1, x2

a, b, c = Check()
print(Solve(a, b, c))