import numpy as np
import matplotlib.pyplot as plt

# Исходные данные (5 вариант)
eps = 0.05 # требуемая точность
# Исходная функция и две её производных
def f(x):
    return 4 - 0.5 * x**2 + 0.2 / (x + 1)

def df(x):
    return -x - 0.2 / (x + 1)**2

def ddf(x):
    return -1 + 0.4 / (x + 1)**3

# Графический метод локализации корня
# Приводим к виду g(x) = h(x): 4 + 0.2/(x+1) = 0.5*x^2
def g(x): # левая часть
    return 4 + 0.2 / (x + 1)

def h(x): # правая часть
    return 0.5 * x**2

# Вывод на графике
x_plot = np.linspace(0.01, 4, 500)
plt.figure(figsize=(9, 5))
plt.plot(x_plot, g(x_plot), 'b-', linewidth=2, label='g(x) = 4 + 0.2/(x+1)')
plt.plot(x_plot, h(x_plot), 'r-', linewidth=2, label='h(x) = 0.5·x²')
plt.axhline(0, color='k', linewidth=0.7)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Лабораторная работа №3. Вариант 5\nГрафический метод локализации корня')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Поиск интервала локализации (a, b), где f меняет знак
a, b = 0.0, 0.0
x_scan = np.arange(0.1, 4.0, 0.1) # шаг 0.1
for i in range(len(x_scan) - 1):
    if f(x_scan[i]) * f(x_scan[i + 1]) < 0:
        a, b = x_scan[i], x_scan[i + 1]
        break # берём первый (меньший) положительный корень

# Вывод результатов + проверка условий (2)-(4)
print(f"Интервал локализации корня: ({a:.1f}, {b:.1f})")
print(f"  f(a) = f({a:.1f}) = {f(a):.6f}")
print(f"  f(b) = f({b:.1f}) = {f(b):.6f}")
print(f"  f(a)·f(b) = {f(a)*f(b):.6f} < 0 (условие 2)")

x_check = np.linspace(a, b, 1000)
df_vals  = df(x_check)
ddf_vals = ddf(x_check)

print(f"\n  f'(x) на ({a:.1f},{b:.1f}): min={df_vals.min():.4f}, max={df_vals.max():.4f}")
print(f"  f''(x) на ({a:.1f},{b:.1f}): min={ddf_vals.min():.4f}, max={ddf_vals.max():.4f}")
print("  f'(x) и f''(x) не меняют знак (условие 3)")

x0 = (a + b) / 2 # начальное приближение и проверка его корректности
print(f"\n  x0 = (a+b)/2 = {x0:.4f}")
print(f"  f(x0)·f''(x0) = {f(x0)*ddf(x0):.6f} > 0 (условие 4)")

# Метод Ньютона
print("\n Метод Ньютона")
# Выводим в виде таблицы
print(f"  {'k':>3}  {'x_k':>12}  {'f(x_k)':>12}  {'|x_{k+1}-x_k|':>14}")

xk = x0
history = [xk] # массив значений для построения графика

for k in range(1, 100):
    xk1 = xk - f(xk) / df(xk) # формула Ньютона
    history.append(xk1)
    diff = abs(xk1 - xk)
    print(f"  {k:>3}  {xk1:>12.8f}  {f(xk1):>12.8f}  {diff:>14.8f}")

    if diff < eps: # критерий остановки: |x_{k+1} - x_k| < ε
        print(f"\nСошлось за {k} итераций.")
        break
    xk = xk1

x_star = xk1
print(f"\nПриближённый корень: x* ≈ {x_star:.6f}")
print(f"Проверка: f(x*) = {f(x_star):.8f}")

# График сходимости
x_fine = np.linspace(a - 0.3, b + 0.3, 500)
plt.figure(figsize=(8, 4))
plt.plot(x_fine, f(x_fine), 'b-', linewidth=2, label='f(x)')
plt.axhline(0, color='k', linewidth=0.7)
plt.axvline(x_star, color='r', linestyle='--', linewidth=1.2,
            label=f'x* ≈ {x_star:.4f}')
plt.scatter(history, [f(xk) for xk in history], color='orange',
            zorder=5, label='Итерации Ньютона')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График f(x) и итерации метода Ньютона')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()