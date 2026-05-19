import math
import random

class HammingCoder:
    def __init__(self, num_messages):
        """Инициализация параметров кода Хемминга. 256 сообщений для 5 варианта."""
        self.n_i = int(math.log2(num_messages)) # количество информационных разрядов
        self.n_k = 0 # количество контрольных разрядов
        # формула для вычисления
        while (2 ** self.n_k) < (self.n_i + self.n_k + 1):
            self.n_k += 1
        self.n = self.n_i + self.n_k # длина классического кода Хемминга (разрядность кода)
        self.n_ext = self.n + 1 # длина расширенного кода Хемминга

    def generate_data_string(self):
        """Генерация случайной последовательности данных."""
        return "".join(random.choice("01") for _ in range(self.n_i))

    def encode(self, data_string):
        """Кодирование информационной строки расширенным кодом Хемминга."""
        # Массив для формирования кода (индексация с 1 для удобства степеней двойки)
        code = [0] * (self.n + 1)
        # Расставляем информационные биты на позиции, не являющиеся степенями 2
        j = 0
        for i in range(1, self.n + 1):
            if (i & (i - 1)) != 0:
                code[i] = int(data_string[j])
                j += 1
        # Расставляем контрольные биты на остальные позиции
        for i in range(self.n_k):
            pos = 2 ** i
            parity = 0
            for k in range(1, self.n + 1):
                # Если в позиции k бит, проверяемый текущим контрольным разрядом, равен 1
                if (k & pos) != 0:
                    parity ^= code[k] # XOR сумма
            code[pos] = parity
        # Вычисляем общий бит чётности для расширенного кода (сумма всех бит)
        parity_bit = sum(code[1:]) % 2
        # Формируем итоговую строку (исключаем нулевой индекс)
        result = "".join(map(str, code[1:])) + str(parity_bit)
        return result

    def decode(self, code_str):
        """Декодирование кодовой строки с проверкой на наличие одиночных и двойных ошибок."""
        # Преобразуем строку в список чисел (первый элемент фиктивный для 1-индексации)
        code = [0] + [int(x) for x in code_str[:-1]]
        parity_bit = int(code_str[-1]) # бит чётности
        status = ""
        corrected_code = code.copy()
        corrected_overall = parity_bit        
        # Проверка общей чётности
        current_overall_parity = (sum(code[1:]) + parity_bit) % 2
        # Вычисление синдрома
        syndrome = 0
        for i in range(self.n_k):
            pos = 2 ** i
            parity = 0
            for k in range(1, self.n + 1):
                if (k & pos) != 0:
                    parity ^= code[k]
            if parity != 0:
                syndrome += pos # Накапливаем номер ошибочного бита
        # Принятие решения по теореме Хемминга
        # Ошибка исправляется инверсией бита
        if current_overall_parity == 0:
            if syndrome == 0:
                status = "Ошибок нет."
            else:
                status = f"Двойная ошибка (синдром = {syndrome}). Исправление невозможно."
        else:
            if syndrome == 0:
                status = "Одиночная ошибка в общем бите чётности. Исправление выполнено."
                corrected_overall ^= 1
            else:
                status = f"Одиночная ошибка в позиции {syndrome}. Исправление выполнено."
                corrected_code[syndrome] ^= 1
        # Извлечение информационной части из исправленного кода
        data = ""
        for i in range(1, self.n + 1):
            if (i & (i - 1)) != 0:
                data += str(corrected_code[i])
        final_code_str = "".join(map(str, corrected_code[1:])) + str(corrected_overall)
        return status, final_code_str, data