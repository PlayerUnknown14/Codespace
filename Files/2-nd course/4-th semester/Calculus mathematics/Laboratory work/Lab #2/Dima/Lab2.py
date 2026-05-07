import numpy as np
import matplotlib.pyplot as plt

def solve_gauss(A, b):
    """Решение СЛАУ методом Гаусса (из лаб №1)"""
    n = len(b)
    # Прямой ход
    for i in range(n):
        for k in range(i + 1, n):
            c = A[k, i] / A[i, i]
            A[k, i:] -= c * A[i, i:]
            b[k] -= c * b[i]
    # Обратный ход
    u = np.zeros(n)
    for i in range(n - 1, -1, -1):
        u[i] = (b[i] - np.dot(A[i, i+1:], u[i+1:])) / A[i, i]
    return u

# --- Исходные данные Вариант 12 ---
x_v = np.array([0.324, 0.645, 0.966, 1.287, 1.609, 1.930, 2.251, 2.572, 2.893])
f_v = np.array([-0.181, -1.215, -0.763, -0.024, 0.289, -0.057, -0.803, -1.210, -0.055])
n = 9
p = 4

# 1. Построение нормальной системы уравнений (1)
# Матрица системы состоит из сумм степеней x
A = np.zeros((p + 1, p + 1))
B = np.zeros(p + 1)

for j in range(p + 1):
    for k in range(p + 1):
        # Элемент матрицы - сумма x_i в степени (j + k)
        A[j, k] = np.sum(x_v ** (j + k))
    # Элемент вектора правой части - сумма f(x_i) * x_i в степени j
    B[j] = np.sum(f_v * (x_v ** j))

# 2. Решение системы методом Гаусса для поиска коэффициентов u_j
u_params = solve_gauss(A.copy(), B.copy())

print("--- РЕЗУЛЬТАТЫ ЛАБОРАТОРНОЙ РАБОТЫ №2 ---")
print(f"Коэффициенты многочлена u_j: {u_params}")

# 3. Вычисление невязок r_k (Формула 2)
def F(x, params):
    """Вычисление значения многочлена в точке x"""
    res = 0
    for j, u in enumerate(params):
        res += u * (x ** j)
    return res

residuals = []
for k in range(n):
    rk = F(x_v[k], u_params) - f_v[k]
    residuals.append(rk)

print("\nНевязки r_k:")
for k, r in enumerate(residuals):
    print(f"r_{k+1}: {r:.6f}")

# 4. Построение графиков
x_plot = np.linspace(min(x_v), max(x_v), 100)
y_plot = [F(val, u_params) for val in x_plot]

plt.figure(figsize=(10, 6))
plt.scatter(x_v, f_v, color='red', label='Табличные данные (Вариант 12)')
plt.plot(x_plot, y_plot, label=f'Аппроксимация (p={p})', color='blue')
plt.title('Аппроксимация функций методом наименьших квадратов')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()