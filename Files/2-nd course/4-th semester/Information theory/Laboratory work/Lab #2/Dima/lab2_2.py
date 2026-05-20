import math
import re
from collections import Counter

def solve_task_2(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except UnicodeDecodeError:
        with open(file_name, 'r', encoding='cp1251') as f:
            raw_text = f.read()

    text = raw_text.lower()
    text = text.replace('ё', 'е')
    text = text.replace('ъ', 'ь')
    allowed_chars = "абвгдежзийклмнопрстуфхцчшщыьэюя "
    filtered_text = "".join([char for char in text if char in allowed_chars])

    total_len = len(filtered_text)
    if total_len == 0:
        return "Файл пуст или не содержит русских букв."
    
    N = len(text)
    if N == 0:
        return 0, 0, 0
    
    #вероятности одиночных букв p(x)
    char_counts = Counter(text)
    h_x = 0
    for char in char_counts:
        p_x = char_counts[char] / N
        h_x -= p_x * math.log2(p_x)
        
    #вероятности биграмм p(x, y)
    bigrams = [text[i:i+2] for i in range(len(text) - 1)]
    N_bg = len(bigrams)
    bg_counts = Counter(bigrams)
    
    h_xy = 0
    for bg in bg_counts:
        p_xy = bg_counts[bg] / N_bg
        h_xy -= p_xy * math.log2(p_xy)
        
    #условная энтропия по теореме сложения
    h_y_cond_x = h_xy - h_x
    
    return h_x, h_xy, h_y_cond_x

hx, hxy, hyx = solve_task_2('input.txt')

print(f"Энтропия одного символа H(X): {hx:.4f} бит")
print(f"Совместная энтропия биграммы H(X,Y): {hxy:.4f} бит")
print(f"Условная энтропия H(Y|X): {hyx:.4f} бит")