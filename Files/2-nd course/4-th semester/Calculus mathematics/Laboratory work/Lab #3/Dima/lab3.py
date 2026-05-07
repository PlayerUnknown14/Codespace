import math
import numpy as np
import matplotlib.pyplot as plt

# 1. Определение функции и её производных
def f(x):
    return 1 + math.log(x) - math.sqrt(x**3)

def df(x):
    # Производная: 1/x - 1.5 * x^0.5
    return 1/x - 1.5 * math.sqrt(x)

def d2f(x):
    # Вторая производная: -1/x^2 - 0.75 * x^-0.5
    return -1/(x**2) - 0.75 / math.sqrt(x)

# 2. Построение графиков для локализации корня
x_vals = np.linspace(0.1, 2.0, 400)
g_vals = [1 + math.log(v) for v in x_vals]
h_vals = [math.sqrt(v**3) for v in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, g_vals, label='g(x) = 1 + ln(x)')
plt.plot(x_vals, h_vals, label='h(x) = sqrt(x^3)')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Локализация корней уравнения (Вариант 12)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# Из графика видно два корня: x=1 и корень в районе 0.5-0.6.
# По заданию локализуем МЕНЬШИЙ корень.
a, b = 0.5, 0.6
eps = 0.03

print("--- РЕЗУЛЬТАТЫ ЛАБОРАТОРНОЙ РАБОТЫ №3 ---")
print(f"Выбранный интервал локализации: [{a}, {b}]")

# 3. Проверка условий сходимости на [a, b]
# f(a)*f(b) < 0
fa, fb = f(a), f(b)
print(f"f(a) = {fa:.4f}, f(b) = {fb:.4f}")
if fa * fb < 0:
    print("Условие f(a)*f(b) < 0 выполнено.")

# Выбор начального приближения x0: f(x0)*f''(x0) > 0
# Т.к. d2f(x) всегда отрицательна для x > 0, выбираем x0 там, где f(x) < 0.
if f(a) < 0:
    x0 = a
else:
    x0 = b
print(f"Начальное приближение x0 = {x0}")

# 4. Метод Ньютона
x_curr = x0
k = 0
history = [x_curr]

while True:
    k += 1
    # Формула Ньютона: x_next = x_curr - f(x_curr)/f'(x_curr)
    x_next = x_curr - f(x_curr) / df(x_curr)
    history.append(x_next)
    
    # Условие остановки: |x_next - x_curr| < eps
    if abs(x_next - x_curr) < eps:
        break
    x_curr = x_next

print(f"\nКоличество итераций K: {k}")
print(f"Приближенное решение x_K: {x_next:.6f}")
print("\nИстория приближений:")
for i, val in enumerate(history):
    print(f"x_{i}: {val:.6f}")