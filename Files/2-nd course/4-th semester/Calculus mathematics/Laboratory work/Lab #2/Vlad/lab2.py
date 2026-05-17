import numpy as np
import matplotlib.pyplot as plt

# Исходные данные (5 вариант)
# Исходный многочлен для обработки: F(x) = u0 + u1*x + u2*x^2 + u3*x^3 + u4*x^4
x = np.array([0.034, 0.394, 0.754, 1.114, 1.474, 1.833, 2.193, 2.553, 2.913])
f = np.array([-0.495, -2.646, -1.581, 0.052, 0.692, -0.128, -1.798, -2.617, 0.206])
node_count = len(x) # количество узлов массива
p = 4 # степень многочлена

# Составление нормальной системы уравнений
A = np.zeros((p + 1, p + 1)) # Матрица A
b = np.zeros(p + 1) # Правая часть матрицы b

for j in range(p + 1): # вычисление элементов системы
    for k in range(p + 1):
        A[j, k] = np.sum(x ** (j + k))
    b[j] = np.sum(x ** j * f)

print("Матрица нормальной системы A:")
print(np.array2string(A, precision=4, suppress_small=True))
print("\nПравая часть b:", np.round(b, 4))

# Решение методом Гаусса с выбором главного элемента
def gauss(A, b):
    node_count = len(b)
    # Расширенная матрица вида [A | b]
    M = np.hstack([A.copy().astype(float), b.copy().reshape(-1, 1).astype(float)])

    # Прямой ход
    for col in range(node_count):
        # Выбор главного элемента (максимального по модулю) в текущем столбце
        max_row = col + np.argmax(np.abs(M[col:, col]))
        M[[col, max_row]] = M[[max_row, col]] # переставляем его в верх столбца

        pivot = M[col, col]
        if abs(pivot) < 1e-12:
            raise ValueError("Матрица вырожденная!")

        M[col] /= pivot # нормирование строки

        # Обнуление элементов ниже главного
        for row in range(col + 1, node_count):
            M[row] -= M[row, col] * M[col]

    # Обратный ход
    u = np.zeros(node_count)
    for i in range(node_count - 1, -1, -1):
        u[i] = M[i, node_count] - np.dot(M[i, i + 1:node_count], u[i + 1:node_count])

    return u

# Получение коэффициентов исходного многочлена
coeffs = gauss(A, b)  # coeffs = [u0, u1, u2, u3, u4]
print("\nКоэффициенты многочлена (u0..u4):", np.round(coeffs, 6))

# Вычисление невязок (степеней отклонения) многочленна r_k = F(x_k) - f(x_k)
def F_poly(x_val, u):
    return sum(u[j] * x_val ** j for j in range(len(u)))

# Значения многочлена в узловых точках
F_vals = np.array([F_poly(xi, coeffs) for xi in x])
residuals = F_vals - f  # невязки r_k

print("\nНевязки r_k = F(x_k) - f(x_k):")
for k in range(node_count):
    print(f"  r_{k+1} = {residuals[k]:+.6f}")

# Построение графиков по полученным результатам
x_plot = np.linspace(x[0], x[-1], 500)
F_plot = np.array([F_poly(xi, coeffs) for xi in x_plot])

plt.figure(figsize=(9, 5))
plt.plot(x_plot, F_plot, 'b-', linewidth=2, label='Многочлен F(x)')
plt.plot(x, f, 'ro', markersize=7, label='Табличные данные f(xᵢ)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Лабораторная работа №2. Вариант 5\nАппроксимация функций методом наименьших квадратов')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()