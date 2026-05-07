import numpy as np

def solve_gauss_with_pivoting(A_orig, f_orig):
    """
    Решение СЛАУ методом Гаусса с выбором главного элемента по столбцам.
    """
    A = A_orig.copy().astype(float)
    f = f_orig.copy().astype(float)
    n = len(f)
    
    # Прямой ход
    for i in range(n):
        # Поиск главного элемента в столбце i
        max_el = abs(A[i, i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > max_el:
                max_el = abs(A[k, i])
                max_row = k
        
        # Перестановка строк
        A[[i, max_row]] = A[[max_row, i]]
        f[[i, max_row]] = f[[max_row, i]]
        
        # Исключение элементов
        for k in range(i + 1, n):
            c = A[k, i] / A[i, i]
            A[k, i:] -= c * A[i, i:]
            f[k] -= c * f[i]
            
    # Обратный ход
    u = np.zeros(n)
    for i in range(n - 1, -1, -1):
        u[i] = (f[i] - np.dot(A[i, i+1:], u[i+1:])) / A[i, i]
        
    return u

def octahedral_norm_vector(v):
    """Октаэдрическая норма вектора (L1)"""
    return np.sum(np.abs(v))

def octahedral_norm_matrix(M):
    """Норма матрицы, согласованная с октаэдрической нормой вектора (max abs column sum)"""
    return np.max(np.sum(np.abs(M), axis=0))

def solve_simple_iteration(A, f, eps, U_exact):
    """
    Решение СЛАУ методом простой итерации.
    """
    n = len(f)
    # Выбор параметра tau. Для сходимости достаточно, чтобы tau < 2/||A||.
    # Хороший выбор: tau = 1 / max_diagonal_element или адаптивно.
    # Возьмем tau так, чтобы минимизировать норму B = E - tau*A
    tau = 1.0 / np.max(np.diag(A))
    
    E = np.eye(n)
    B = E - tau * A
    F = tau * f
    
    q = octahedral_norm_matrix(B)
    print(f"Выбранное значение tau: {tau:.4f}")
    print(f"Норма матрицы B (q): {q:.4f}")
    
    if q >= 1:
        print("Внимание: достаточное условие сходимости не выполнено (q >= 1).")
        # Попробуем уменьшить tau
        tau = 0.5 * tau
        B = E - tau * A
        F = tau * f
        q = octahedral_norm_matrix(B)
        print(f"Пересчитанное tau: {tau:.4f}, новое q: {q:.4f}")

    u_k = np.zeros(n) # Начальное приближение u0 = 0
    k = 0
    u_history = [u_k.copy()]
    errors = []
    
    while True:
        k += 1
        u_next = np.dot(B, u_k) + F
        
        # Расчет погрешности epsilon_k = u_k - U (относительно точного Гаусса)
        eps_k = u_next - U_exact
        errors.append(eps_k)
        
        # Условие остановки: ||u_{k+1} - u_k|| < eps * (1-q) / 1 (согласно формуле 3)
        # В задании: ||u_{k+1} - u_k|| < (1-q) * eps
        diff_norm = octahedral_norm_vector(u_next - u_k)
        stop_criterion = (1 - q) * eps
        
        u_history.append(u_next.copy())
        u_k = u_next
        
        if diff_norm < stop_criterion:
            break
            
    return u_k, k, errors, u_history

# --- Исходные данные варианта 12 ---
A = np.array([
    [3.869, 0.512, 0.205, 0.164],
    [0.253, 4.102, 0.156, 0.235],
    [0.416, 0.341, 3.879, 0.189],
    [0.382, 0.425, 0.346, 4.351]
])

f = np.array([0.802, 0.591, 0.263, 0.671])
epsilon = 0.01

print("--- РЕЗУЛЬТАТЫ ЛАБОРАТОРНОЙ РАБОТЫ №1 ---")
print(f"Вариант: 12\n")

# 1. Метод Гаусса
U_gauss = solve_gauss_with_pivoting(A, f)
print("1. Результат метода Гаусса (вектор U):")
print(U_gauss)
print("-" * 40)

# 2. Метод простой итерации
u_final, K, errors, history = solve_simple_iteration(A, f, epsilon, U_gauss)

print(f"\n2. Результаты метода простой итерации:")
print(f"Количество итераций K: {K}")
print(f"Приближенное решение u_K:")
print(u_final)

print("\n3. Векторы погрешностей epsilon_k = u_k - U (на каждой итерации):")
for i, err in enumerate(errors):
    print(f"Итерация {i+1}: {err}")

print("\n4. Проверка точности финального вектора:")
final_err_norm = octahedral_norm_vector(u_final - U_gauss)
print(f"||u_K - U|| = {final_err_norm:.6f} (Требуемая точность: {epsilon})")