import numpy as np
import math
from collections import Counter
import re
import heapq

# ============================================================
# ЧТЕНИЕ И ПОДГОТОВКА ТЕКСТА
# ============================================================

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Оставляем только русские буквы и пробелы
text_clean = re.sub(r'[^а-яА-ЯёЁ\s]', '', text.lower())
text_clean = re.sub(r'\s+', ' ', text_clean).strip()

# Подсчёт частот символов
char_counts = Counter(text_clean)
total_chars = len(text_clean)
probs = {ch: count / total_chars for ch, count in char_counts.items()}

# Алфавит
alphabet = sorted(char_counts.keys())
n = len(alphabet)

# ============================================================
# ЗАДАНИЕ 1: ИЗБЫТОЧНОСТЬ
# ============================================================

# H1(X) - энтропия по отдельным символам
H1 = -sum(p * math.log2(p) for p in probs.values() if p > 0)
H_max = math.log2(n)
D_p = 1 - H1 / H_max

# H2(X) - энтропия по биграммам
bigrams = [(text_clean[i], text_clean[i+1]) for i in range(len(text_clean)-1)]
bigram_counts = Counter(bigrams)
total_bigrams = len(bigrams)
bigram_probs = {bg: count / total_bigrams for bg, count in bigram_counts.items()}

H2_joint = -sum(p * math.log2(p) for p in bigram_probs.values() if p > 0)
H2_cond = H2_joint - H1  # H(Y|X)
D_s = 1 - H2_cond / H1
D = 1 - H2_cond / H_max

print(f"H1(X) = {H1:.4f} бит/сим")
print(f"D_p = {D_p:.4f} ({D_p*100:.2f}%)")
print(f"H(Y|X) = {H2_cond:.4f} бит/сим")
print(f"D_s = {D_s:.4f} ({D_s*100:.2f}%)")
print(f"D = {D:.4f} ({D*100:.2f}%)")

# ============================================================
# ЗАДАНИЕ 2: МЕТОД ШЕННОНА-ФАНО
# ============================================================

sorted_chars = sorted(probs.keys(), key=lambda x: -probs[x])
sorted_probs = [probs[ch] for ch in sorted_chars]

def shannon_fano(chars, probs):
    if len(chars) == 1:
        return {chars[0]: ''}
    
    total = sum(probs)
    half = total / 2
    
    best_split = 1
    best_diff = abs(sum(probs[:1]) - half)
    
    for i in range(2, len(probs)):
        diff = abs(sum(probs[:i]) - half)
        if diff < best_diff:
            best_diff = diff
            best_split = i
    
    left = shannon_fano(chars[:best_split], probs[:best_split])
    right = shannon_fano(chars[best_split:], probs[best_split:])
    
    codes = {}
    for ch, code in left.items():
        codes[ch] = '0' + code
    for ch, code in right.items():
        codes[ch] = '1' + code
    return codes

sf_codes = shannon_fano(sorted_chars, sorted_probs)

# ============================================================
# ЗАДАНИЕ 2: МЕТОД ХАФФМАНА
# ============================================================

class HuffmanNode:
    def __init__(self, char, prob):
        self.char = char
        self.prob = prob
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.prob < other.prob

def build_huffman_tree(chars, probs):
    heap = [HuffmanNode(ch, p) for ch, p in zip(chars, probs)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.prob + right.prob)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def get_huffman_codes(node, prefix='', code_dict=None):
    if code_dict is None:
        code_dict = {}
    if node.char is not None:
        code_dict[node.char] = prefix if prefix else '0'
        return code_dict
    if node.left:
        get_huffman_codes(node.left, prefix + '0', code_dict)
    if node.right:
        get_huffman_codes(node.right, prefix + '1', code_dict)
    return code_dict

huff_tree = build_huffman_tree(sorted_chars, sorted_probs)
huff_codes = get_huffman_codes(huff_tree)

# ============================================================
# ЗАДАНИЕ 3: ПОКАЗАТЕЛИ ЭФФЕКТИВНОСТИ
# ============================================================

l_fixed = math.ceil(math.log2(n))

l_avg_sf = sum(probs[ch] * len(sf_codes[ch]) for ch in alphabet)
l_avg_huff = sum(probs[ch] * len(huff_codes[ch]) for ch in alphabet)

K_cc_sf = l_fixed / l_avg_sf
K_cc_huff = l_fixed / l_avg_huff

K_oe_sf = H1 / l_avg_sf
K_oe_huff = H1 / l_avg_huff

print(f"\nШеннон-Фано: l_ср = {l_avg_sf:.4f}, K_сс = {K_cc_sf:.4f}, K_оэ = {K_oe_sf:.4f}")
print(f"Хаффман:     l_ср = {l_avg_huff:.4f}, K_сс = {K_cc_huff:.4f}, K_оэ = {K_oe_huff:.4f}")

# ============================================================
# ЗАДАНИЕ 4: КОДИРОВАНИЕ И ДЕКОДИРОВАНИЕ
# ============================================================

sample = "слишком много желающих узнать наши реальные имена оборотень шумно втягивает воздух хмурится она пыталась тебя пометить я знаю не беспокойся это просто журналистка"

# Шеннон-Фано
encoded_sf = ''.join(sf_codes[ch] for ch in sample)
sf_decode_map = {code: ch for ch, code in sf_codes.items()}

def decode_sf(encoded):
    decoded, buffer = [], ''
    for bit in encoded:
        buffer += bit
        if buffer in sf_decode_map:
            decoded.append(sf_decode_map[buffer])
            buffer = ''
    return ''.join(decoded)

decoded_sf = decode_sf(encoded_sf)
print(f"\nШеннон-Фано: совпадение = {sample == decoded_sf}")

# Хаффман
encoded_huff = ''.join(huff_codes[ch] for ch in sample)
huff_decode_map = {code: ch for ch, code in huff_codes.items()}

def decode_huff(encoded):
    decoded, buffer = [], ''
    for bit in encoded:
        buffer += bit
        if buffer in huff_decode_map:
            decoded.append(huff_decode_map[buffer])
            buffer = ''
    return ''.join(decoded)

decoded_huff = decode_huff(encoded_huff)
print(decoded_huff)
print(f"Хаффман:     совпадение = {sample == decoded_huff}")