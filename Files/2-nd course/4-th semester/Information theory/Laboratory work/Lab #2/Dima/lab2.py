import math
from collections import Counter

def analyze_bigrams(file_name):
    # Чтение текста из файла с обработкой кодировки
    try: 
        with open(file_name, 'r', encoding='cp1251') as f: 
            raw_text = f.read() 
    except: 
        with open(file_name, 'r', encoding='utf-8') as f: 
            raw_text = f.read()

    # Очистка и подготовка текста (32 символа)
    text = raw_text.lower().replace('ё', 'е').replace('ъ', 'ь')
    allowed_chars = "абвгдежзийклмнопрстуфхцчшщыьэюя "
    filtered = "".join([char for char in text if char in allowed_chars])
    
    # Формирование биграмм (пар символов)
    bigrams = [filtered[i:i+2] for i in range(len(filtered)-1)]
    total_bigrams = len(bigrams)
    
    if total_bigrams == 0:
        print("Файл пуст или не содержит русских букв.")
        return

    # Подсчет совместных вероятностей P(x_i, y_j)
    bigram_counts = Counter(bigrams)
    
    # Расчет энтропии сложной системы H(X,Y)
    total_entropy_xy = 0
    for count in bigram_counts.values():
        p_xy = count / total_bigrams
        total_entropy_xy -= p_xy * math.log2(p_xy)
        
    # Подсчет вероятностей первого символа P(x_i) для нахождения H(X)
    first_char_counts = Counter([b[0] for b in bigrams])
    total_entropy_x = 0
    for count in first_char_counts.values():
        p_x = count / len(bigrams)
        total_entropy_x -= p_x * math.log2(p_x)
        
    # По теореме сложения энтропий: H(X,Y) = H(X) + H(Y|X) 
    # Отсюда условная энтропия H(Y|X) = H(X,Y) - H(X)
    h_y_given_x = total_entropy_xy - total_entropy_x
    
    # Вывод результатов
    print("-" * 50)
    print(f"Файл: {file_name}")
    print(f"ИТОГО символов: {len(filtered)}")
    print(f"Всего биграмм (X,Y): {total_bigrams}")
    print(f"ЭНТРОПИЯ СЛОЖНОЙ СИСТЕМЫ H(X,Y): {total_entropy_xy:.5f} бит/биграмму")
    print(f"Энтропия источника X (H(X)): {total_entropy_x:.5f} бит/символ")
    print(f"УСЛОВНАЯ ЭНТРОПИЯ H(Y|X): {h_y_given_x:.5f} бит/символ")
    print("-" * 50)

if __name__ == "__main__":
    analyze_bigrams('input.txt')