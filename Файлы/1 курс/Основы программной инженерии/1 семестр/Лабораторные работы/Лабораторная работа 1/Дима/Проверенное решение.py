from cmath import *


def cbrt(polynomial):
    solution = set()
    root1 = polynomial ** (1 / 3)
    root2 = (polynomial ** (1 / 3)) * (-1 / 2 + (sqrt(3) * 1j) / 2)
    root3 = (polynomial ** (1 / 3)) * (-1 / 2 - (sqrt(3) * 1j) / 2)
    solution.update({root1, root2, root3})
    return solution


def linear(a, b):
    solutions = set()
    if a == 0 and b == 0:
        solutions.add(True)

    if a == 0 and b != 0:
        solutions.add(False)

    if a != 0:
        solutions.add(-b / a)
    return solutions


def quadratic(a, b, c):
    solutions = set()
    if a != 0:
        D = b ** 2 - 4 * a * c
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        solutions.update({x1, x2})
    else:
        solutions.update(linear(b, c))
    return solutions


def cubic(a, b, c, d):
    solutions = set()
    if a != 0:
        p = (3 * a * c - b ** 2) / (3 * a ** 2)
        q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
        alpha = cbrt(-q / 2 + sqrt((q / 2) ** 2 + (p / 3) ** 3))
        beta = cbrt(-q / 2 - sqrt((q / 2) ** 2 + (p / 3) ** 3))
        for i in alpha:
            for j in beta:
                if abs((i * j) + p / 3) <= 0.0001:
                    x = i + j - b / (3 * a)
                    solutions.add(x)
    else:
        solutions.update(quadratic(b, c, d))
    return solutions


print('ax^3+bx^2+cx+d=0')
a, b, c, d = map(complex, input().split())

print(cubic(a, b, c, d))