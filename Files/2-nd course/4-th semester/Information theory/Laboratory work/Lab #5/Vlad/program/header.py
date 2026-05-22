import math
import random

class LinearGroupCoder:
    def __init__(self, num_messages):
        """Инициализация параметров кода Хемминга. 256 сообщений для 5 варианта."""
        self.n_i = int(math.log2(num_messages)) # количество информационных разрядов
        self.n_k = 0 # количество контрольных разрядов
        # формула для вычисления
        while (2 ** self.n_k) < (self.n_i + self.n_k + 1):
            self.n_k += 1
        self.n = self.n_i + self.n_k # длина классического кода Хемминга (разрядность кода)
        # Построение матрицы П (Проверочная часть порождающей матрицы G)
        # Правило: Вес каждой строки матрицы П должен быть >= d_min - 1 (то есть >= 2).
        # Нам нужно 8 уникальных строк длиной 4 бита с минимум двумя единицами.
        self.P = [
            [0, 0, 1, 1], # 1
            [0, 1, 0, 1], # 2
            [0, 1, 1, 0], # 3
            [1, 0, 0, 1], # 4
            [1, 0, 1, 0], # 5
            [1, 1, 0, 0], # 6
            [0, 1, 1, 1], # 7
            [1, 0, 1, 1]  # 8
        ]

    def generate_data_string(self):
        """Генерация случайной последовательности данных."""
        return "".join(random.choice("01") for _ in range(self.n_i))

    def encode(self, data_string):
        """
        Кодирование ЛГК.
        Вектор V = U * G, где G = [ I | P ].
        Результат: сначала идут информационные биты, затем контрольные.
        """
        u = [int(bit) for bit in data_string]
        
        # Информационная часть (единичная матрица I просто переносит биты)
        code = u.copy()
        
        # Проверочная часть (умножение вектора U на матрицу П по модулю 2)
        for j in range(self.n_k):
            # Суммируем (XOR) элементы столбца j матрицы P, если соответствующий бит u[i] == 1
            check_bit = sum(u[i] * self.P[i][j] for i in range(self.n_i)) % 2
            code.append(check_bit)
            
        return "".join(map(str, code))

    def decode(self, code_str):
        """
        Декодирование ЛГК и исправление одиночной ошибки через Синдром.
        Вектор синдрома S = V_прин * H^T.
        """
        v = [int(bit) for bit in code_str]
        
        # Извлекаем принятые информационные и контрольные биты
        u_recv = v[:self.n_i]
        c_recv = v[self.n_i:]
        
        # Вычисляем Синдром. 
        # S_j = (сумма(u_recv[i] * P[i][j]) + c_recv[j]) mod 2
        syndrome = []
        for j in range(self.n_k):
            s_bit = (sum(u_recv[i] * self.P[i][j] for i in range(self.n_i)) + c_recv[j]) % 2
            syndrome.append(s_bit)
            
        status = ""
        corrected_code = v.copy()
        
        # Анализ синдрома
        if all(bit == 0 for bit in syndrome):
            status = "Ошибок нет."
        else:
            # Ищем, какому столбцу проверочной матрицы H соответствует синдром.
            # Матрица H = [ P^T | I ]. Ее столбцы — это строки P и строки единичной матрицы.
            
            error_pos = -1
            
            # Проверяем информационную часть (совпадает ли синдром со строкой матрицы P)
            for i in range(self.n_i):
                if self.P[i] == syndrome:
                    error_pos = i
                    break
            
            # Проверяем контрольную часть (совпадает ли синдром с единичной матрицей)
            if error_pos == -1:
                for j in range(self.n_k):
                    # Генерируем столбец единичной матрицы
                    i_col = [1 if k == j else 0 for k in range(self.n_k)]
                    if i_col == syndrome:
                        error_pos = self.n_i + j
                        break
            
            if error_pos != -1:
                status = f"Одиночная ошибка в позиции {error_pos + 1}. Исправление выполнено."
                corrected_code[error_pos] ^= 1 # Инвертируем ошибочный бит
            else:
                status = f"Неизвестный синдром {syndrome}. Множественная ошибка!"

        # Извлечение информационной части из исправленного кода
        data = "".join(map(str, corrected_code[:self.n_i]))
        final_code_str = "".join(map(str, corrected_code))
        
        return status, final_code_str, data