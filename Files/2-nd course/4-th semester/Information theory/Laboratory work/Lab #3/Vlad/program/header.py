import math
import re
from collections import Counter

class TextAnalyzer:
    def __init__(self):
        self.alphabet_size = 32 # Длина используемого алфавита
        self.processed_text = "" # Текст после предобработки
        self.text_length = 0 # Длина текста после предобработки
        self.probs = {} # Словарь вероятностей символов p(xi)
        self.codes = {} # Словарь кодов для каждого символа
        self.hx = 0 # Энтропия источника H(X)
        self.hyx = 0 # Условная энтропия H(Y|X)

    def _clean_text(self, text):
        """Предобработка текста (32 символа, ь/ъ объединены)."""
        text = text.lower()
        text = re.sub(r'[^а-яё \n]', '', text) # Убираем лишние символы
        text = text.replace('ъ', 'ь')
        return text

    def load_file(self, filename):
        """Загрузка текста из файла."""
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    def preprocess_text(self, text):
        """Предобработка текста и расчет вероятностей символов."""
        self.processed_text = self._clean_text(text)
        self.text_length = len(self.processed_text)
        counts = Counter(self.processed_text)
        self.probs = {char: count/self.text_length for char, count in counts.items()}
        return self.processed_text

    def analyze_redundancy(self, text):
        """Расчет избыточности текста."""
        # Энтропия источника H(X)
        self.hx = -sum(p * math.log2(p) for p in self.probs.values() if p > 0)
        # Условная энтропия H(Y|X) через биграммы
        pairs = [text[i:i+2] for i in range(0, len(text) - 1, 2)]
        pair_counts = Counter(pairs)
        h_xy = -sum(c/(self.text_length-1) * math.log2(c/(self.text_length-1)) for c in pair_counts.values() if c > 0)
        self.hyx = h_xy - self.hx
        # Расчет избыточностей трёх видов
        h_max = math.log2(self.alphabet_size)
        dp = 1 - (self.hx / h_max)
        ds = 1 - (self.hyx / self.hx)
        d_total = ds + dp - (ds * dp)
        
        return dp, ds, d_total

    def build_shannon_fano(self):
        """Построение кодов методом Шеннона-Фано."""
        # Сортировка по убыванию вероятности
        items = sorted(self.probs.items(), key=lambda x: x[1], reverse=True)
        chars = [x[0] for x in items]
        probs = [x[1] for x in items]
        self.codes = {c: "" for c in chars}

        def divide(c_list, p_list):
            """Рекурсивное разделение алфавита на две группы
            и присвоение бита на каждой итерации."""
            if len(c_list) <= 1: # базовый случай
                return

            min_diff = float('inf') # минимальная разница сумм
            best_split = 1 # индекс разделения
            # Поиск точки разделения
            for i in range(1, len(p_list)):
                diff = abs(sum(p_list[:i]) - sum(p_list[i:]))
                if diff <= min_diff:
                    min_diff = diff
                    best_split = i
            
            for i in range(len(c_list)):
                self.codes[c_list[i]] += "1" if i < best_split else "0"
            
            divide(c_list[:best_split], p_list[:best_split])
            divide(c_list[best_split:], p_list[best_split:])

        divide(chars, probs)

    def build_huffman(self):
        """Построение кодов методом Хаффмана."""
        from typing import Optional
        # Вспомогательный класс узла дерева
        class Node:
            def __init__(self, char, p):
                self.char, self.p = char, p # символ и его вероятность
                self.left: Optional['Node'] = None # левый потомок
                self.right: Optional['Node'] = None # правый потомок
        # Инициализация узлов для каждого символа
        nodes = [Node(c, p) for c, p in self.probs.items()]
        # Построение дерева Хаффмана (пока не останется только корень)
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.p)
            n1, n2 = nodes.pop(0), nodes.pop(0) # два узла с мин. вероятностями
            parent = Node(None, n1.p + n2.p) # новый узел-родитель
            parent.left, parent.right = n1, n2 # потомки нового узла
            nodes.append(parent)
        
        # Генерация кодов
        self.codes = {c: "" for c in self.probs}
        def walk(node, code):
            """Рекурсивный обход дерева от корня к листьям."""
            if node.char: # базовый случай (есть символ = дошли до листа = сохраняем код)
                self.codes[node.char] = code 
                return
            walk(node.left, code + "0")
            walk(node.right, code + "1")
        
        if nodes: 
            walk(nodes[0], "")

    def get_efficiency(self):
        """Параметры оптимальности текста."""
        # Средняя длина символа кодового алфавита
        l_cp = sum(self.probs[c] * len(code) for c, code in self.codes.items())
        # Коэффициент статического сжатия
        h_max = math.log2(self.alphabet_size)
        k_cc = h_max / l_cp
        # Коэффициент относительной эффективности
        k_oe = self.hx / l_cp 
        return l_cp, k_cc, k_oe

    def encode(self, text):
        """Кодирование текста по построенным кодам."""
        clean = self._clean_text(text)
        return "".join(self.codes.get(c, "") for c in clean)

    def decode(self, binary_str):
        """Декодирование бинарной строки в текст."""
        inv = {v: k for k, v in self.codes.items()}
        res, temp = "", ""
        for bit in binary_str:
            temp += bit
            if temp in inv:
                res += inv[temp]
                temp = ""
        return res