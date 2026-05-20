import math
import re
from collections import Counter

def get_filtered_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except:
        with open(file_name, 'r', encoding='cp1251') as f:
            raw_text = f.read()
    
    text = raw_text.lower()
    text = text.replace('ё', 'е').replace('ъ', 'ь')
    # Добавляем \n, чтобы сохранить структуру абзацев для Задания 4
    allowed_chars = "абвгдежзийклмнопрстуфхцчшщыьэюя \n"
    return "".join([char for char in text if char in allowed_chars])

def get_shannon_fano_codes(probs_list):
    if len(probs_list) == 1:
        return {probs_list[0][0]: ""}
    
    # Поиск точки разделения для минимальной разницы сумм вероятностей
    split_idx = 0
    total_sum = sum(p for c, p in probs_list)
    acc = 0
    min_diff = total_sum
    
    for i in range(len(probs_list)):
        acc += probs_list[i][1]
        diff = abs(acc - (total_sum - acc))
        if diff < min_diff:
            min_diff = diff
            split_idx = i + 1
        else:
            break
            
    codes = {}
    # Рекурсивное построение кодов
    left_part = get_shannon_fano_codes(probs_list[:split_idx])
    right_part = get_shannon_fano_codes(probs_list[split_idx:])
    
    for char in left_part: codes[char] = "0" + left_part[char]
    for char in right_part: codes[char] = "1" + right_part[char]
    return codes

class Node:
    def __init__(self, char, prob, left=None, right=None):
        self.char = char
        self.prob = prob
        self.left = left
        self.right = right

def build_huffman(probs_list):
    nodes = [Node(c, p) for c, p in probs_list]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.prob)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(None, left.prob + right.prob, left, right)
        nodes.append(parent)
    
    code_map = {}
    def generate_codes(node, current_code=""):
        if node:
            if node.char:
                code_map[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")
    
    generate_codes(nodes[0])
    return nodes[0], code_map

def print_huffman_tree(node, indent=""):
    if node:
        if node.char:
            char_repr = 'NL' if node.char == '\n' else node.char
            print(f"{indent}└── '{char_repr}' ({node.prob:.4f})")
        else:
            print(f"{indent}├── Узел ({node.prob:.4f})")
            print_huffman_tree(node.left, indent + "│   ")
            print_huffman_tree(node.right, indent + "    ")

def decode_text(encoded_str, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded = []
    temp = ""
    for bit in encoded_str:
        temp += bit
        if temp in reverse_codes:
            decoded.append(reverse_codes[temp])
            temp = ""
    return "".join(decoded)


if __name__ == "__main__":
    text = get_filtered_text('input.txt')
    n = len(text)
    m = 32
    h_max = math.log2(m)

    # задание 1
    counts = Counter(text)
    p_dict = {c: count/n for c, count in counts.items()}
    h_x = -sum(p * math.log2(p) for p in p_dict.values())
    
    # Условная энтропия через биграммы
    bigrams = [text[i:i+2] for i in range(n-1)]
    h_xy = -sum((count/(n-1)) * math.log2(count/(n-1)) for count in Counter(bigrams).values())
    h_yx = h_xy - h_x

    dp = 1 - (h_x / h_max)
    ds = (h_x - h_yx) / h_max
    d_total = 1 - (h_yx / h_max)

    print("=== ЗАДАНИЕ 1: РАСЧЕТ ИЗБЫТОЧНОСТИ ===")
    print(f"Энтропия H(X): {h_x:.4f}")
    print(f"Избыточность Dp (неравновероятность): {dp:.4f}")
    print(f"Избыточность Ds (стат. связи): {ds:.4f}")
    print(f"Полная избыточность D: {d_total:.4f}\n")

    # задание 2
    probs_sorted = sorted(p_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Шеннон-Фано
    codes_sf = get_shannon_fano_codes(probs_sorted)
    
    # Хаффман
    huff_root, codes_hf = build_huffman(probs_sorted)
    
    print("=== ЗАДАНИЕ 2: ВИЗУАЛИЗАЦИЯ ДЕРЕВА ХАФФМАНА ===")
    print_huffman_tree(huff_root)
    
    print("\n=== ТАБЛИЦА КОДОВ ===")
    print(f"{'Символ':<8} | {'Вер-ть':<8} | {'Шеннон-Фано':<12} | {'Хаффман':<12}")
    for char, prob in probs_sorted:
        c_disp = 'NEWLINE' if char == '\n' else f"'{char}'"
        print(f"{c_disp:<8} | {prob:<8.4f} | {codes_sf[char]:<12} | {codes_hf[char]:<12}")

    # задание 3
    def calc_metrics(codes, name):
        l_cp = sum(p_dict[c] * len(codes[c]) for c in codes)
        k_cc = 6 / l_cp 
        k_oe = h_x / l_cp
        print(f"\nМетрики {name}:")
        print(f"  Средняя длина l_cp: {l_cp:.4f} бит/симв")
        print(f"  Коэф. сжатия Kcc: {k_cc:.4f}")
        print(f"  Коэф. эффективности Koe: {k_oe:.4f}")

    calc_metrics(codes_sf, "Шеннон-Фано")
    calc_metrics(codes_hf, "Хаффман")

    # задание 4: делим текст на абзацы и берем первые 4
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    if len(paragraphs) >= 4:
        fragment = "\n\n".join(paragraphs[:4])
        
        print("\n=== ЗАДАНИЕ 4: ВЫДЕЛЕННЫЕ 4 АБЗАЦА ТЕКСТА ===")
        print("-" * 50)
        print(fragment)
        print("-" * 50)

        # 1. МЕТОД ХАФФМАНА
        encoded_hf = "".join(codes_hf[c] for c in fragment)
        decoded_hf = decode_text(encoded_hf, codes_hf)
        
        print(f"\n[МЕТОД ХАФФМАНА]")
        print(f"Закодировано (первые 60 бит): {encoded_hf[:60]}...")
        print(f"Общий объем: {len(encoded_hf)} бит")
        print(f"Декодирование успешно: {decoded_hf == fragment}")

        # 2. МЕТОД ШЕННОНА-ФАНО
        encoded_sf = "".join(codes_sf[c] for c in fragment)
        decoded_sf = decode_text(encoded_sf, codes_sf)
        
        print(f"\n[МЕТОД ШЕННОНА-ФАНО]")
        print(f"Закодировано (первые 60 бит): {encoded_sf[:60]}...")
        print(f"Общий объем: {len(encoded_sf)} бит")
        print(f"Декодирование успешно: {decoded_sf == fragment}")
        
    else:
        print("\nОшибка: В файле недостаточно абзацев.")