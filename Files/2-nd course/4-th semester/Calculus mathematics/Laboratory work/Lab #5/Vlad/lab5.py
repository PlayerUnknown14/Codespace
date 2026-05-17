import numpy as np
import matplotlib.pyplot as plt

# Исходные данные (5 вариант)
def f(x):
    return (x - 1) ** (-2)
a, b = 2.0, 4.0 # границы интервала
eps = 0.001 # требуемая точность

# Точное значение интеграла (формула Ньютона–Лейбница)
# Первообразная: F(x) = -(x-1)^(-1)
def F(x):
    return -(x - 1) ** (-1)

exact = F(b) - F(a) # точное значение
print(f"Точное значение интеграла I = {exact:.10f}")
print(f"F(b) - F(a) = {F(b):.6f} - ({F(a):.6f}) = {exact:.6f}\n")

# Формула трапеций: f(x) = tau/2 * (f0 + 2*f1 + ... + 2*f_{N-1} + fN)
# tk = a + k*tau, tau = (b - a) / N
print("Метод трапеций")
print(f"{'N':>5}  {'I_trap':>14}  {'|ошибка|':>12}")

N_trap = 0
errors_trap = [] # абсолютные погрешности для всех N
N_vals_trap = [] # все значения N

for N in range(2, 10000): # перебираем N, пока не достигнем точности
    tau = (b - a) / N
    nodes = np.linspace(a, b, N + 1) # N+1 узлов: t_0, t_1, ..., t_N
    f_vals = f(nodes)

    I_trap = tau / 2 * (f_vals[0] + 2 * np.sum(f_vals[1:-1]) + f_vals[-1])
    err = abs(I_trap - exact) # абсолютная погрешность

    errors_trap.append(err)
    N_vals_trap.append(N)
    print(f"{N:>5}  {I_trap:>14.8f}  {err:>12.8f}")

    if err < eps:
        N_trap = N
        break

print(f"\nФормула трапеций: точность ε = {eps} достигнута при N = {N_trap}.")
print(f"Число узлов: N_тр + 1 = {N_trap + 1}\n")

# Формула Симпсона
# I ≈ tau/3 * [f(t0) + 4*f(t1) + 2*f(t2) + 4*f(t3) + ... + 4*f(t_{N-1}) + f(t_N)]
# N должно быть чётным

print("Метод Симпсона")
print(f"{'N':>5}  {'I_simp':>14}  {'|ошибка|':>12}")

N_simp = 0
errors_simp = [] # абсолютные погрешности для всех N
N_vals_simp = [] # все значения N

for N in range(2, 10000, 2): # только чётные N
    tau = (b - a) / N
    nodes = np.linspace(a, b, N + 1)
    f_vals = f(nodes)

    # Коэффициенты по правилу Симпсона: 1, 4, 2, 4, 2, ...
    coeffs = np.ones(N + 1)
    coeffs[1:-1:2] = 4 # нечётные индексы
    coeffs[2:-2:2] = 2 # чётные внутренние индексы

    I_simp = tau / 3 * np.dot(coeffs, f_vals)
    err = abs(I_simp - exact)

    errors_simp.append(err)
    N_vals_simp.append(N)
    print(f"{N:>5}  {I_simp:>14.8f}  {err:>12.8f}")

    if err < eps:
        N_simp = N
        break

print(f"\nФормула Симпсона: точность ε = {eps} достигнута при N = {N_simp}.")
print(f"Число узлов: N_с + 1 = {N_simp + 1}\n")

# Сравнение методов
print(f"Точное значение I = {exact:.8f}")
print(f"Трапеции (N = {N_trap}): узлов = {N_trap + 1}")
print(f"Симпсон (N = {N_simp}): узлов = {N_simp + 1}")
print(f"Симпсон потребовал в {(N_trap + 1) / (N_simp + 1):.1f} раза меньше узлов для той же точности.")