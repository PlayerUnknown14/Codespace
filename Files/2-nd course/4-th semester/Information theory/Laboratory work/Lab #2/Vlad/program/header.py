import math
import re
import numpy as np

class TextEntropyAnalyzer:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя " # 32 символа, ь/ъ объединены
        self.matrix_joint = None  # P(X, Y) - матрица совместных вероятностей
        self.p_x = None # p(xi) - вероятности на входе (источник)
        self.p_y = None # p(yj) - вероятности на выходе (приемник)
        self.channel_matrice_y_x = None  # P(Y|X) - канальная матрица источника
        self.channel_matrice_x_y = None  # P(X|Y) - канальная матрица приемника
        
    def build_random_matrix(self, size=10):
        """Создание произвольной матрицы совместных вероятностей (10x10)."""
        raw_matrix = np.random.rand(size, size)
        # Нормировка для условия: сумма всех pij матрицы == 1
        self.matrix_joint = raw_matrix / np.sum(raw_matrix)
        self._calculate_marginal_probs()
        self.build_channel_matrices()

    def _clean_text(self, text):
        """Предобработка текста (32 символа, ь/ъ объединены)."""
        text = text.lower()
        text = re.sub(r'[^а-яё ]', '', text) # Убираем лишние символы
        text = text.replace('ъ', 'ь')
        return text

    def build_from_text(self, filepath):
        """Построение матрицы на основе биграмм текста."""
        # Чтение текста из файла
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = self._clean_text(f.read())
        except Exception as e:
            print(f"Ошибка чтения: {e}")
            return False

        # Создаем алфавит (отсортированный список уникальных символов)
        unique_chars = sorted(list(set(self.alphabet)))
        alphabet_len = len(unique_chars)
        # Словарь [символ: индекс]
        char_to_idx = {char: i for i, char in enumerate(unique_chars)}
        # Создаём нулевую матрицу счётчиков биграмм
        counts = np.zeros((alphabet_len, alphabet_len)) 
        total_pairs = 0 # Счётчик биграмм в тексте

        # Считаем биграммы, заполняем матрицу
        for i in range(len(text) - 1):
            char_x = text[i]
            char_y = text[i+1]
            if char_x in char_to_idx and char_y in char_to_idx:
                # Увеличиваем счетчик (число в ячейке) для конкретной биграммы
                counts[char_to_idx[char_x]][char_to_idx[char_y]] += 1
                total_pairs += 1

        # Нормализация для получения матрицы совместных вероятностей
        self.matrix_joint = counts / total_pairs
        self._calculate_marginal_probs()
        self.build_channel_matrices()
        return True

    def _calculate_marginal_probs(self):
        """Расчет p(xi) и p(yj) матрицы путем суммирования строк и столбцов."""
        if self.matrix_joint is None:
            self.p_x = None
            self.p_y = None
            return
        
        self.p_x = np.sum(self.matrix_joint, axis=1) # Сумма по строкам
        self.p_y = np.sum(self.matrix_joint, axis=0) # Сумма по столбцам

    def build_channel_matrices(self):
        if self.matrix_joint is None or self.p_x is None or self.p_y is None:
            return

        # Канальная матрица со стороны источника P(Y|X)
        # P(yj|xi) = P(xi, yj) / P(xi)
        self.channel_matrice_y_x = np.zeros_like(self.matrix_joint)
        for i in range(len(self.p_x)):
            if self.p_x[i] > 0:
                self.channel_matrice_y_x[i, :] = self.matrix_joint[i, :] / self.p_x[i]

        # Канальная матрица со стороны приемника P(X|Y)
        # P(xi|yj) = P(xi, yj) / P(yj)
        self.channel_matrice_x_y = np.zeros_like(self.matrix_joint)
        for j in range(len(self.p_y)):
            if self.p_y[j] > 0:
                self.channel_matrice_x_y[:, j] = self.matrix_joint[:, j] / self.p_y[j]

    def calculate_entropy(self):
        """Рассчёт всех видов энтропии

        Returns:
            Словарь: Все рассчитанные метрики
        """
        if self.matrix_joint is None or self.p_x is None or self.p_y is None:
            return None

        # Энтропия сложной системы H(X,Y) = −∑∑ pij​ * log2(pij​)
        h_xy = 0
        for row in self.matrix_joint:
            for p_ij in row:
                if p_ij > 0:
                    h_xy -= p_ij * math.log2(p_ij)
        
        # Энтропия источника H(X) = H(X)=−∑​p(xi​)log2​p(xi​)
        h_x = sum([-p * math.log2(p) for p in self.p_x if p > 0])
        # Энтропия приемника H(Y) = H(Y)=−∑​p(yj​)log2​p(yj​)
        h_y = sum([-p * math.log2(p) for p in self.p_y if p > 0])
        
        # Полная условная энтропия H(Y/X) (потери при передаче)
        # H(Y/X) = H(X, Y) - H(X)
        h_y_cond_x = 0
        for i in range(len(self.p_x)):
            for j in range(len(self.p_y)):
                p_cond = self.channel_matrice_y_x[i][j]
                if p_cond > 0 and self.p_x[i] > 0:
                    h_y_cond_x -= self.p_x[i] * p_cond * math.log2(p_cond)

        # Полная условная энтропия H(X/Y) (потери при приеме)
        # H(X/Y) = H(X, Y) - H(Y)
        h_x_cond_y = 0
        for j in range(len(self.p_y)):
            for i in range(len(self.p_x)):
                p_cond = self.channel_matrice_x_y[i][j]
                if p_cond > 0 and self.p_y[j] > 0:
                    h_x_cond_y -= self.p_y[j] * p_cond * math.log2(p_cond)

        # Частная условная энтропия H(Y/xi)
        # H(Y/xi​)=−∑p(yj​/xi​) * log2​(p(yj​/xi​))
        partial_h_y_xi = []
        for i in range(len(self.p_x)):
            h_val = 0
            if self.p_x[i] > 0:
                for j in range(len(self.p_y)):
                    p_cond = self.channel_matrice_y_x[i][j]
                    if p_cond > 0:
                        h_val -= p_cond * math.log2(p_cond)
            partial_h_y_xi.append(h_val)

        # Частная условная энтропия H(X/yj)
        # H(X/yj​)=−∑p(xi​/yj​) * log2​(p(xi​/yj​))
        partial_h_x_yj = []
        for j in range(len(self.p_y)):
            h_val = 0
            if self.p_y[j] > 0:
                for i in range(len(self.p_x)):
                    p_cond = self.channel_matrice_x_y[j][i]
                    if p_cond > 0:
                        h_val -= p_cond * math.log2(p_cond)
            partial_h_x_yj.append(h_val)

        return {
            "H(X,Y)": h_xy,
            "H(X)": h_x,
            "H(Y)": h_y,
            "H(Y/X)": h_y_cond_x,
            "H(X/Y)": h_x_cond_y,
            "partial_Y_xi": partial_h_y_xi,
            "partial_X_yj": partial_h_x_yj
        }
    
    def print_channel_matrices(self):
        """Вывод канальных матриц в консоль."""
        if self.channel_matrice_y_x is None:
            print("Канальные матрицы не построены.")
            return

        print("\n" + "="*40)
        print("КАНАЛЬНЫЕ МАТРИЦЫ")
        print("="*40)
        
        print("\n=== Канальная матрица источника P(Y|X) ===")
        self._print_matrix(self.channel_matrice_y_x)

        print("\n=== Канальная матрица приемника P(X|Y) ===")
        self._print_matrix(self.channel_matrice_x_y)
        
        print("="*40)

    def _print_matrix(self, matrix):
        """Вспомогательный метод для вывода матрицы."""
        if matrix is None:
            return
        
        rows, cols = matrix.shape

        for i in range(rows):
            row_str = " | ".join([f"{val:.4f}" for val in matrix[i]])
            print(f"{row_str}")