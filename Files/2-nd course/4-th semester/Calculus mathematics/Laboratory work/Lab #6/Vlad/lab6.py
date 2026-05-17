import numpy as np
import matplotlib.pyplot as plt

# Исходные данные (5 вариант)
a = 0.0
T = 0.8
u0 = -1.0
eps = 1e-3
def f(t, u):
    return -4 * t**3 * u + 4 * u**2 * np.exp(4 * t) * (1 - t**3)

# Точное решение залачи Коши
# U(t) = -e^(-4t)
def U_exact(t):
    return -np.exp(-4 * t)

print("Точное решение: U(t) = -exp(-4t)")
print(f"Проверка: U(0) = {U_exact(0):.1f} (должно быть -1)\n")

# Метод Эйлера
def euler(N):
    tau = (T - a) / N
    t = a + np.arange(N + 1) * tau
    u = np.zeros(N + 1)
    u[0] = u0
    for n in range(N):
        u[n + 1] = u[n] + tau * f(t[n], u[n])
    return t, u

# Метод Рунге–Кутты 4-го порядка
def runge_kutta(N):
    tau = (T - a) / N
    t = a + np.arange(N + 1) * tau
    u = np.zeros(N + 1)
    u[0] = u0
    for n in range(N):
        k1 = f(t[n], u[n])
        k2 = f(t[n] + tau/2, u[n] + tau/2 * k1)
        k3 = f(t[n] + tau/2, u[n] + tau/2 * k2)
        k4 = f(t[n] + tau, u[n] + tau * k3)
        u[n + 1] = u[n] + tau / 6 * (k1 + 2*k2 + 2*k3 + k4)
    return t, u

# Критерий остановки (удвоение N)
def find_N(method, coeff):
    N = 2 # начинаем с N=2
    print(f"  {'N':>6}  {'Дельта':>14}")
    while True:
        _, u_N = method(N) # решение для N разбиений
        _, u_2N = method(2*N) # решение для 2N разбиений

        # Каждый второй узел сетки 2N совпадает с узлом сетки N
        u_2N_on_N = u_2N[::2]
        delta = coeff * np.max(np.abs(u_2N_on_N - u_N))
        print(f"  {N:>6}  {delta:>14.6e}")

        if delta < eps:
            break
        N *= 2 # удваиваем N и повторяем

    N_final = 2 * N # последнее N, для которого были проведены вычисления
    return N_final, method(N_final)

# Вывод результатов
print("Метод Эйлера")
N_euler, (t_euler, u_euler) = find_N(euler, coeff=0.5)
max_err_euler = np.max(np.abs(u_euler - U_exact(t_euler)))
print(f"\nДостигнута точность при N = {N_euler // 2} (финальное N = {N_euler})")
print(f"max|u_n - U(t_n)| = {max_err_euler:.6e}\n")

print("Метод Рунге–Кутты")
N_rk, (t_rk, u_rk) = find_N(runge_kutta, coeff=1/15)
max_err_rk = np.max(np.abs(u_rk - U_exact(t_rk)))
print(f"\nДостигнута точность при N = {N_rk // 2} (финальное N = {N_rk})")
print(f"max|u_n - U(t_n)| = {max_err_rk:.6e}\n")

print("Сравнение методов")
print(f"Метод Эйлера: N = {N_euler}, узлов = {N_euler + 1}, max|err| = {max_err_euler:.2e}")
print(f"Метод Рунге–Кутты: N = {N_rk}, узлов = {N_rk + 1}, max|err| = {max_err_rk:.2e}")
print(f"Метод Рунге–Кутты потребовал в {N_euler / N_rk:.0f} раза меньше разбиений, чем метод Эйлера.")

# Графики
t_fine = np.linspace(a, T, 500)
U_fine = U_exact(t_fine)

plt.figure(figsize=(10, 5))
plt.plot(t_fine, U_fine, 'k-', linewidth=2.5, label='Точное решение U(t) = -e^(-4t)')
plt.plot(t_euler, u_euler, 'b--o', markersize=4, linewidth=1.2, label=f'Метод Эйлера (N = {N_euler})')
plt.plot(t_rk, u_rk, 'r--s', markersize=4, linewidth=1.2, label=f'Метод Рунге–Кутты (N = {N_rk})')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.title('Лабораторная работа №6. Вариант 5\n' 'Численное решение задачи Коши для ОДУ 1-го порядка')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()