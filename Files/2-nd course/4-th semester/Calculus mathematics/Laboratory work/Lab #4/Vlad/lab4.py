import numpy as np

# Исходные данные (5 вариант)
n = 10
h = 1.0 / n
def f(x):
    return (3 + 2 * x**2) ** (-0.5)

# Узлы интерполяции и значения функции
# t_j = (j-1)*h; (j = 1, 2, ..., n+1)
nodes = np.array([(j - 1) * h for j in range(1, n + 2)])
f_vals = f(nodes) # f(t_j)

# Таблица разделённых разностей
# diff_table[i][k] = разделённая разность f[t_i, ..., t_{i+k}]
diff_table = np.zeros((n + 1, n + 1))
diff_table[:, 0] = f_vals # нулевой порядок = f(t_j)

for k in range(1, n + 1): # порядок разности
    for i in range(n + 1 - k): # начальный индекс
        diff_table[i][k] = (diff_table[i + 1][k - 1] - diff_table[i][k - 1]) / (nodes[i + k] - nodes[i])

# Интерполяционный многочлен Ньютона
# N_10(t) = f[t1] + f[t1,t2](t-t1) + f[t1,t2,t3](t-t1)(t-t2) + ...
def newton_poly(t):
    result = diff_table[0][n] # коэффициент при старшем члене
    for k in range(n - 1, -1, -1):
        result = result * (t - nodes[k]) + diff_table[0][k]
    return result

# Значения в точках с полуцелыми индексами
# t_{j-1/2} = (j - 0.5)*h; (j = 1, 2, ..., 10)
half_nodes = np.array([(j - 0.5) * h for j in range(1, n + 1)])

f_half = f(half_nodes) # точные значения
N_half = np.array([newton_poly(t) for t in half_nodes]) # значения многочлена
errors = f_half - N_half # локальная погрешность интерполирования ε_{j-1/2}

max_err = np.max(np.abs(errors)) # максимальная погрешность
rms_err = np.sqrt(np.sum(errors**2) / n) # среднеквадратичная погрешность

print("\nУзлы интерполяции и значения функции")
print(f"{'j':>3}  {'t_j':>8}  {'f(t_j)':>14}")
for j in range(n + 1):
    print(f"{j+1:>3}  {nodes[j]:>8.4f}  {f_vals[j]:>14.8f}")

print("\nРазделённые разности 1-го порядка f(t_i, t_{i+1})")
for i in range(n):
    print(f"  f[t{i+1}, t{i+2}] = {diff_table[i][1]:8f}")

print("\nПогрешность в полуцелых узлах")
print(f"{'j':>3}  {'t_{j-1/2}':>10}  {'f(t)':>14}  {'N10(t)':>14}  {'ε':>14}")
for j in range(n):
    print(f"{j+1:>3}  {half_nodes[j]:>10.4f}  {f_half[j]:>14.8f}"
        f"  {N_half[j]:>14.8f}  {errors[j]:>14.2e}")

print(f"\nМаксимальная погрешность ε_max = {max_err:.6e}")
print(f"Среднеквадратичная погрешность ε_ср = {rms_err:.6e}")
print("=" * 65)