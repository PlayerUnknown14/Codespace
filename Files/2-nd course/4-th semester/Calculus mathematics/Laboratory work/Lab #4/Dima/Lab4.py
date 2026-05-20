import numpy as np

# 1. Заданная функция
def f(x):
    return (np.cos(np.pi * np.sqrt(x)))**2

n = 10
h = 1.0 / n

# Узлы интерполяции (равноотстоящие)
t = np.array([i * h for i in range(n + 1)])
y = f(t)

# 2. Вычисление разделенных разностей
# dd - двумерный массив (таблица) разделенных разностей
# dd[i, k] означает разделенную разность k-го порядка, начинающуюся с узла i
dd = np.zeros((n + 1, n + 1))
dd[:, 0] = y  # Нулевой порядок - сами значения функции

for k in range(1, n + 1):
    for i in range(n + 1 - k):
        # Формула: ( f(t_{i+1}...t_{i+k}) - f(t_{i}...t_{i+k-1}) ) / (t_{i+k} - t_i)
        dd[i, k] = (dd[i + 1, k - 1] - dd[i, k - 1]) / (t[i + k] - t[i])

# Извлекаем коэффициенты для многочлена Ньютона (верхняя строка таблицы)
coefs = dd[0, :]

# 3. Функция для вычисления интерполяционного многочлена Ньютона
def N_poly(val, t_nodes, c, degree):
    res = c[0]
    prod = 1.0
    for k in range(1, degree + 1):
        prod *= (val - t_nodes[k - 1])
        res += c[k] * prod
    return res

# 4. Вычисление в точках с полуцелыми индексами и поиск погрешностей
# Узлы t_{j-1/2} = (j - 0.5) * h
t_half = np.array([(j - 0.5) * h for j in range(1, n + 1)])

# Истинные значения и значения по многочлену
f_half = f(t_half)
N_half = np.array([N_poly(val, t, coefs, n) for val in t_half])

# Погрешности
errs = np.abs(f_half - N_half)
max_err = np.max(errs)
rms_err = np.sqrt(np.sum(errs**2) / n)

# --- ВЫВОД РЕЗУЛЬТАТОВ ---
print("--- РЕЗУЛЬТАТЫ ЛАБОРАТОРНОЙ РАБОТЫ №4 ---")
print(f"Вариант: 12")
print(f"Функция: f(x) = cos^2(pi * sqrt(x)), n = {n}, h = {h}\n")

print("1. Значения разделенных разностей f(t1...tk), используемых в многочлене Ньютона:")
for i in range(n + 1):
    print(f"Порядок {i}: {coefs[i]:.6f}")

print("\n2. Значения в точках с полуцелыми индексами t_{j-1/2}:")
print(f"{'j':<4} | {'t_half':<8} | {'f(t)':<10} | {'N_10(t)':<10} | {'Погрешность (eps)':<15}")
print("-" * 55)
for j in range(n):
    print(f"{j+1:<4} | {t_half[j]:<8.2f} | {f_half[j]:<10.6f} | {N_half[j]:<10.6f} | {errs[j]:.6e}")

print("\n3. Итоговые погрешности:")
print(f"Максимальная погрешность (eps_max): {max_err:.6e}")
print(f"Среднеквадратичная погрешность (eps_cp): {rms_err:.6e}")