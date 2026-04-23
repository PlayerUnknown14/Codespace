import numpy as np

#Генерируем случайную матрицу 10x10 и нормализуем (сумма = 1)
np.random.seed(40) # Фиксируем сид для повторяемости
raw_matrix = np.random.rand(10, 10)
matrix_p_ij = raw_matrix / np.sum(raw_matrix)

#p(xi) - суммы по столбцам
p_x = np.sum(matrix_p_ij, axis=0)

#r(yj) - суммы по строкам
p_y = np.sum(matrix_p_ij, axis=1)

#расчет энтропии строки или столбца
def calculate_entropy(probs):
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))

#H(Y/xi) и H(Y/X)
h_y_xi = []
for i in range(10):
    # Условная вероятность p(yj|xi) = p_ij / p(xi)
    cond_prob_y_given_x = matrix_p_ij[:, i] / p_x[i]
    h_y_xi.append(calculate_entropy(cond_prob_y_given_x))

full_h_y_x = np.sum(p_x * h_y_xi)

#H(X/yj) и H(X/Y)
h_x_yj = []
for j in range(10):
    # Условная вероятность p(xi|yj) = p_ij / r(yj)
    cond_prob_x_given_y = matrix_p_ij[j, :] / p_y[j]
    h_x_yj.append(calculate_entropy(cond_prob_x_given_y))

full_h_x_y = np.sum(p_y * h_x_yj)

print(f"Полная условная энтропия H(Y|X): {full_h_y_x:.4f} бит")
print(f"Полная условная энтропия H(X|Y): {full_h_x_y:.4f} бит")

for i in range(3):
    print(f"Частные потери H(Y|x{i+1}): {h_y_xi[i]:.4f} бит")