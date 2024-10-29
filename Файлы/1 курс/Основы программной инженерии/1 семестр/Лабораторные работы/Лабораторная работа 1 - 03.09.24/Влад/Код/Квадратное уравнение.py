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

a, b, c = Check()

Dis = b**2 - 4 * a * c
print(f"Диксриминат равен {Dis}")
if Dis == 0:
    print("Один корень")
    x = int(-b / 2 * a)
    print(f"Корень уравнения: x = {x}")
elif Dis < 0:
    print("Корней нет")
else:
    print("Два корня")
    x1 = (-b + Dis**0.5) / (2 * a)
    x2 = (-b - Dis**0.5) / (2 * a)
    print(f"Корни уравнения: x1 = {x1:.3f}, x2 = {x2:.3f}")