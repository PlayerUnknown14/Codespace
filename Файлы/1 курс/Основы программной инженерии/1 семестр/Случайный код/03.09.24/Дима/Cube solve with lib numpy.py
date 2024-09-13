from numpy.polynomial import *

def check():
    while True:
        try:
            print("Введите коэффиценты")
            a, b, c, d = map(float, input().split())
            5/a, 5/b, 5/c, 5/d
            break
        except ValueError:
            print("Коэффиценты введены неверно")
        except ZeroDivisionError:
            print("Коэффиценты не могут быть равны нулю")
    return a, b, c, d

a, b, c, d = check()
x = Polynomial([a,b,c,d])
x_mass = []
print(x)
print(x.roots())
