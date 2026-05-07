import numpy as np
import matplotlib.pyplot as plt

# 1. Определение правой части уравнения и точного решения
def f(t, u):
    return (t - 1) * np.exp(t) * (u**2) - t * u

def exact_u(t):
    return np.exp(-t)

# Параметры задачи
a, T = 0, 2
u0 = 1
eps = 1e-3

# 2. Реализация методов
def solve_euler(N):
    h = (T - a) / N
    t = np.linspace(a, T, N + 1)
    u = np.zeros(N + 1)
    u[0] = u0
    for i in range(N):
        u[i+1] = u[i] + h * f(t[i], u[i])
    return t, u

def solve_rk(N):
    h = (T - a) / N
    t = np.linspace(a, T, N + 1)
    u = np.zeros(N + 1)
    u[0] = u0
    for i in range(N):
        k1 = h * f(t[i], u[i])
        k2 = h * f(t[i] + 0.5*h, u[i] + 0.5*k1)
        k3 = h * f(t[i] + 0.5*h, u[i] + 0.5*k2)
        k4 = h * f(t[i] + h, u[i] + k3)
        u[i+1] = u[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return t, u

# 3. Нахождение решения методом Эйлера с контролем точности
print("--- МЕТОД ЭЙЛЕРА ---")
n_eul = 2
while True:
    t_2n, u_2n = solve_euler(n_eul)
    t_n, u_n = solve_euler(n_eul // 2) if n_eul > 2 else (None, None)
    
    if u_n is not None:
        # Сравнение в общих точках (каждая вторая точка u_2n)
        diff = np.abs(u_2n[::2] - u_n)
        max_diff = np.max(diff)
        if max_diff < eps:
            break
    n_eul *= 2

print(f"Число разбиений N: {n_eul}")
max_err_eul = np.max(np.abs(u_2n - exact_u(t_2n)))
print(f"Макс. отклонение от точного решения: {max_err_eul:.6f}\n")

# 4. Нахождение решения методом Рунге-Кутты с контролем точности
print("--- МЕТОД РУНГЕ-КУТТЫ (4-й порядок) ---")
n_rk = 2
while True:
    t_2n_rk, u_2n_rk = solve_rk(n_rk)
    t_n_rk, u_n_rk = solve_rk(n_rk // 2) if n_rk > 2 else (None, None)
    
    if u_n_rk is not None:
        # Правило Рунге для 4 порядка: (1/15) * |u_2n - u_n|
        diff = np.abs(u_2n_rk[::2] - u_n_rk) / 15
        max_diff = np.max(diff)
        if max_diff < eps:
            break
    n_rk *= 2

print(f"Число разбиений N: {n_rk}")
max_err_rk = np.max(np.abs(u_2n_rk - exact_u(t_2n_rk)))
print(f"Макс. отклонение от точного решения: {max_err_rk:.6f}")

# 5. Построение графиков
t_exact = np.linspace(a, T, 100)
u_exact_vals = exact_u(t_exact)

plt.figure(figsize=(10, 6))
plt.plot(t_exact, u_exact_vals, 'k-', label='Точное решение U(t)')
plt.plot(t_2n, u_2n, 'r--', label=f'Эйлер (N={n_eul})')
plt.plot(t_2n_rk, u_2n_rk, 'b:', label=f'Рунге-Кутта (N={n_rk})')
plt.title('Решение задачи Коши (Вариант 12)')
plt.xlabel('t')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()