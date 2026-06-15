import numpy as np, math
from collections import Counter
import re

# Чтение и очистка текста
with open('input.txt', 'r', encoding='utf-8') as f:
    text = re.sub(r'[^а-яё\s]', '', f.read().lower())
    text = re.sub(r'\s+', ' ', text).strip()

# Алфавит: список уникальных символов тек   ста, отсортированный
# Например: [' ', 'а', 'б', 'в', ...]
alphabet = sorted(set(text))
n = len(alphabet)  # количество уникальных символов (например, 32)

# Словарь "символ → индекс": {' ': 0, 'а': 1, 'б': 2, ...}
# Нужен для перевода букв в числа, чтобы работать с матрицей
ch2i = {c: i for i, c in enumerate(alphabet)}

# НЕПЕРЕКРЫВАЮЩИЕСЯ биграммы: "голова" → "го", "ло", "ва"
# Берём пары символов с шагом 2: (0,1), (2,3), (4,5), ...
# text[i] — первая буква пары (X), text[i+1] — вторая (Y)
bigrams = []
for i in range(0, len(text) - 1, 2):  # шаг 2 — пары не перекрываются
    x = ch2i[text[i]]      # индекс первой буквы в алфавите
    y = ch2i[text[i + 1]]  # индекс второй буквы в алфавите
    bigrams.append((x, y))

# Матрица совместных вероятностей P(X,Y) размером n×n
# Строка i = символ X, столбец j = символ Y
# Элемент [i,j] = сколько раз встретилась пара (X=i, Y=j)
P_joint = np.zeros((n, n))
for x, y in bigrams:
    P_joint[x, y] += 1
P_joint /= P_joint.sum()  # делим на сумму → получаем вероятности

# Маргинальные вероятности
P_x = P_joint.sum(axis=1)  # P(X): сумма по столбцам = вероятности первых букв
P_y = P_joint.sum(axis=0)  # P(Y): сумма по строкам = вероятности вторых букв

# Канальная матрица со стороны источника P(Y|X)
# P(y_j|x_i) = P(x_i, y_j) / P(x_i)
# Каждая строка = условные вероятности для фиксированного x_i
P_Yx = np.zeros((n, n))
for i in range(n):
    if P_x[i] > 0:
        P_Yx[i] = P_joint[i] / P_x[i]

# Канальная матрица со стороны приёмника P(X|Y)
# P(x_i|y_j) = P(x_i, y_j) / P(y_j)
# Каждый столбец = условные вероятности для фиксированного y_j
P_Xy = np.zeros((n, n))
for j in range(n):
    if P_y[j] > 0:
        P_Xy[:, j] = P_joint[:, j] / P_y[j]

# Энтропия H(X,Y) = -sum(p_ij * log2(p_ij))
H_XY = -sum(p * math.log2(p) for p in P_joint.flat if p > 0)

# Условная энтропия H(Y|X) через канальную матрицу P(Y|X)
# H(Y|X) = sum(P(x_i) * H(Y|x_i))
# H(Y|x_i) = -sum(P(y_j|x_i) * log2(P(y_j|x_i)))
H_Yx = 0
for i in range(n):
    if P_x[i] > 0:
        h = sum(-p * math.log2(p) for p in P_Yx[i] if p > 0)
        H_Yx += P_x[i] * h

# Энтропии отдельных символов
H_X = sum(-p * math.log2(p) for p in P_x if p > 0)
H_Y = sum(-p * math.log2(p) for p in P_y if p > 0)

# H(X|Y) через теорему сложения
H_Xy = H_XY - H_Y

print(f"H(X,Y) = {H_XY:.4f} бит/сим")
print(f"H(Y|X) = {H_Yx:.4f} бит/сим")
print(f"H(X)   = {H_X:.4f} бит/сим")
print(f"H(Y)   = {H_Y:.4f} бит/сим")
print(f"H(X|Y) = {H_Xy:.4f} бит/сим")
print(f"Проверка: H(X)+H(Y|X) = {H_X + H_Yx:.4f} ≈ H(X,Y)")