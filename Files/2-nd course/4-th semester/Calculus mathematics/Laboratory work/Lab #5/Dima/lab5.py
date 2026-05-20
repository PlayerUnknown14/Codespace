import math

# 1. Заданная функция
def f(x):
    return math.exp(-x) * math.cos(x)

# 2. Точное значение по формуле Ньютона-Лейбница
# Интеграл от exp(-x)cos(x) dx = (exp(-x) * (sin(x) - cos(x))) / 2
def get_exact(a, b):
    def F(x):
        return (math.exp(-x) * (math.sin(x) - math.cos(x))) / 2
    return F(b) - F(a)

# 3. Метод трапеций
def trapezoid_rule(a, b, n):
    h = (b - a) / n
    res = (f(a) + f(b)) / 2
    for i in range(1, n):
        res += f(a + i * h)
    return res * h

# 4. Метод Симпсона (N должно быть четным)
def simpson_rule(a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(1, n):
        k = 4 if i % 2 != 0 else 2
        res += k * f(a + i * h)
    return (h / 3) * res

# --- ОСНОВНОЙ ПРОЦЕСС ВЫЧИСЛЕНИЙ ---
a, b = 0, 2
eps = 0.001
exact = get_exact(a, b)

print("--- РЕЗУЛЬТАТЫ ЛАБОРАТОРНОЙ РАБОТЫ №5 ---")
print(f"Вариант: 12. Интеграл от e^-x * cos(x) на [{a}, {b}]")
print(f"Точное значение: {exact:.6f}\n")

# Поиск N для метода трапеций
n_tr = 2
while True:
    val_tr = trapezoid_rule(a, b, n_tr)
    err_tr = abs(exact - val_tr)
    if err_tr < eps:
        break
    n_tr += 1

print(f"МЕТОД ТРАПЕЦИЙ:")
print(f"Количество интервалов N_тр: {n_tr}")
print(f"Количество узлов (N_тр + 1): {n_tr + 1}")
print(f"Приближенное значение: {val_tr:.6f}")
print(f"Абсолютная погрешность: {err_tr:.6f}\n")

# Поиск N для метода Симпсона
n_si = 2
while True:
    val_si = simpson_rule(a, b, n_si)
    err_si = abs(exact - val_si)
    if err_si < eps:
        break
    n_si += 2  # N должно быть четным

print(f"МЕТОД СИМПСОНА:")
print(f"Количество интервалов N_с: {n_si}")
print(f"Количество узлов (N_с + 1): {n_si + 1}")
print(f"Приближенное значение: {val_si:.6f}")
print(f"Абсолютная погрешность: {err_si:.6f}\n")

# 5. Сравнение результатов
print("СРАВНЕНИЕ:")
print(f"Разница в количестве узлов: {(n_tr + 1) - (n_si + 1)}")
if n_si < n_tr:
    print("Метод Симпсона оказался эффективнее (требует меньше узлов).")