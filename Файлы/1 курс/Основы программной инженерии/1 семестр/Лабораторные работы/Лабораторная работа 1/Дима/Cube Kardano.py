#Вычисление кубического уравнения по формуле Кардано

import cmath

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
maxerror = 1.0e-12

#Вычисление корней кубического уравнения по формуле Кардано
#http://surl.li/jltmfa

p = (3 * a * c - b ** 2) / (3 * a ** 2)
q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
Q = (p / 3) ** 3 + (q / 2) ** 2
print('p = ', p, '\nq = ', q, '\nQ = ', Q)
if q == 0:
    F = cmath.pi/2
if q < 0:
    F = cmath.atan(-2 * cmath.sqrt(-Q) / q)
if q > 0:
    F = cmath.atan(-2 * cmath.sqrt(-Q) / q) + cmath.pi
        
if Q < 0:
    x1 = 2 * (-p / 3)**0.5 * cmath.cos(F / 3) - b / (3 * a)
    
    x2 = 2 * (-p / 3)**0.5 * cmath.cos((F / 3) + 2 * cmath.pi / 3) - b / (3 * a)
    
    x3 = 2 * (-p / 3)**0.5 * cmath.cos((F / 3) + 4 * cmath.pi / 3) - b / (3 * a)
    
    Ans1 = a*x1**3+b*x1**2+c*x1+d
    Ans2 = a*x2**3+b*x2**2+c*x2+d
    Ans3 = a*x3**3+b*x3**2+c*x3+d
    print('\nx1 =', x1, '\nx2 =', x2, '\nx3 =', x3)
    print('Уравнение с первым корнем = ',Ans1)
    print('Уравнение со вторым корнем = ',Ans2)
    print('Уравнение с третьим корнем = ',Ans3)
    
elif Q == 0:
    x1 = 2 * (-q / 2) ** (1 / 3) - b / (3 * a)
    x2 = (-q / 2) ** (-1 / 3) - b / (3 * a)
    x3 = (-q / 2) ** (-1 / 3) - b / (3 * a)
    print('\nx1 =', x1, '\nx2 =', x2, '\nx3 =', x3)
    Ans1 = a*x1**3+b*x1**2+c*x1+d
    Ans2 = a*x2**3+b*x2**2+c*x2+d
    Ans3 = a*x3**3+b*x3**2+c*x3+d
    print('Уравнение с первым корнем = ',Ans1)
    print('Уравнение со вторым корнем = ',Ans2)
    print('Уравнение с третьим корнем = ',Ans3)
elif Q > 0:
    alfa = (-q / 2 + Q ** 0.5) ** (1 / 3)
    beta = -abs((-q / 2 - Q ** 0.5) ** (1 / 3))
    y1 = alfa + beta
    y2 = complex(-((alfa + beta) / 2), (alfa - beta) / 2 * 3 ** 0.5)
    y3 = complex(-((alfa + beta) / 2), -(alfa - beta) / 2 * 3 ** 0.5)
    x1 = y1 - b / (3 * a)
    x2 = y2 - b / (3 * a)
    x2 = x2.real + x2.imag * 1j
    x3 = y3 - b / (3 * a)
    x3 = x3.real + x3.imag * 1j
    Ans1 = a*x1**3+b*x1**2+c*x1+d
    Ans2 = a*x2**3+b*x2**2+c*x2+d
    Ans3 = a*x3**3+b*x3**2+c*x3+d
    print('\nalfa =', alfa, '\nbeta =', beta, '\n\nx1 =', x1, '\nx2 =', x2, '\nx3 =', x3)
    print('Уравнение с первым корнем = ',Ans1)
    print('Уравнение со вторым корнем = ',Ans2)
    print('Уравнение с третьим корнем = ',Ans3)