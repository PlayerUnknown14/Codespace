class HammingCoder:
    def __init__(self, num_messages=256):
        """
        Инициализация параметров кода Хемминга на основе количества сообщений.
        Для Варианта 5: num_messages = 256.
        """
        import math
        # 1. Вычисляем количество информационных разрядов (n_и)
        self.n_i = int(math.log2(num_messages)) 
        
        # 2. Вычисляем количество контрольных разрядов (n_к)
        # Условие: 2^(n_к) >= n_и + n_к + 1
        self.n_k = 0
        while (2 ** self.n_k) < (self.n_i + self.n_k + 1):
            self.n_k += 1
            
        # 3. Общая длина классического кода Хемминга (n = n_и + n_к)
        self.n = self.n_i + self.n_k
        
        # 4. Общая длина расширенного кода (добавляем 1 бит общей чётности)
        self.n_ext = self.n + 1

    def encode(self, data: str) -> str:
        """
        Кодирование информационной строки расширенным кодом Хемминга.
        """
        if len(data) != self.n_i:
            raise ValueError(f"Длина данных должна быть ровно {self.n_i} бит.")

        # Массив для формирования кода (индексация с 1 для удобства степеней двойки)
        code = [0] * (self.n + 1)
        
        # 1. Расставляем информационные биты (на позиции, не являющиеся степенями 2)
        j = 0
        for i in range(1, self.n + 1):
            if (i & (i - 1)) != 0: # Побитовая проверка: i не является степенью двойки
                code[i] = int(data[j])
                j += 1

        # 2. Вычисляем контрольные биты (на позициях 1, 2, 4, 8...)
        for i in range(self.n_k):
            pos = 2 ** i
            parity = 0
            for k in range(1, self.n + 1):
                # Если в позиции k бит, проверяемый текущим контрольным разрядом, равен 1
                if (k & pos) != 0:
                    parity ^= code[k] # XOR сумма
            code[pos] = parity

        # 3. Вычисляем общий бит чётности для расширенного кода (сумма всех бит)
        # Добавляет единицу, если сумма нечетная, чтобы сделать общую сумму четной
        overall_parity = sum(code[1:]) % 2

        # Формируем итоговую строку (исключаем нулевой индекс)
        result = "".join(map(str, code[1:])) + str(overall_parity)
        return result

    def decode(self, code_str: str):
        """
        Декодирование с проверкой на наличие одиночных и двойных ошибок.
        Возвращает: (статус_сообщения, исправленный_код, извлеченные_данные)
        """
        if len(code_str) != self.n_ext:
            raise ValueError(f"Длина кода должна быть ровно {self.n_ext} бит.")

        # Преобразуем строку в список чисел (первый элемент фиктивный для 1-индексации)
        code = [0] + [int(x) for x in code_str[:-1]]
        overall_bit = int(code_str[-1])
        
        # 1. Проверка общей чётности (Этап 1 из методички)
        current_overall_parity = (sum(code[1:]) + overall_bit) % 2
        
        # 2. Вычисление синдрома (Этап 2 из методички)
        syndrome = 0
        for i in range(self.n_k):
            pos = 2 ** i
            parity = 0
            for k in range(1, self.n + 1):
                if (k & pos) != 0:
                    parity ^= code[k]
            if parity != 0:
                syndrome += pos # Накапливаем номер ошибочного бита

        status = ""
        corrected_code = code.copy()
        corrected_overall = overall_bit

        # Логика принятия решений по теореме Хемминга
        if current_overall_parity == 0:
            if syndrome == 0:
                status = "Ошибок нет."
            else:
                status = f"ОБНАРУЖЕНА ДВОЙНАЯ ОШИБКА (синдром={syndrome}). Исправление невозможно!"
        else:
            if syndrome == 0:
                status = "Одиночная ошибка в общем бите чётности. Исправлена."
                corrected_overall ^= 1
            else:
                status = f"ОДИНОЧНАЯ ОШИБКА в позиции {syndrome}. Успешно исправлена."
                corrected_code[syndrome] ^= 1 # Исправляем ошибку инверсией бита

        # 3. Извлечение информационной части из исправленного кода
        data = ""
        for i in range(1, self.n + 1):
            if (i & (i - 1)) != 0:
                data += str(corrected_code[i])

        final_code_str = "".join(map(str, corrected_code[1:])) + str(corrected_overall)
        return status, final_code_str, data