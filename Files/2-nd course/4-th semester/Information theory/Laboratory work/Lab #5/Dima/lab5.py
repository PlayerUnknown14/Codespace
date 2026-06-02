# =====================================================================
# ЛАБОРАТОРНАЯ РАБОТА № 5. ВАРИАНТ 12 (ЛГК)
# =====================================================================

# Определение проверочной матрицы P размера 16x5 с весом строк >= 2
matrica_p = [
    [0, 1, 1, 0, 0],  # строка 1
    [0, 1, 0, 1, 0],  # строка 2
    [0, 1, 0, 0, 1],  # строка 3
    [0, 0, 1, 1, 0],  # строка 4
    [0, 0, 1, 0, 1],  # строка 5
    [0, 0, 0, 1, 1],  # строка 6
    [1, 1, 0, 0, 0],  # строка 7
    [1, 0, 1, 0, 0],  # строка 8
    [1, 0, 0, 1, 0],  # строка 9
    [1, 0, 0, 0, 1],  # строка 10
    [1, 1, 1, 0, 0],  # строка 11
    [1, 1, 0, 1, 0],  # строка 12
    [1, 1, 0, 0, 1],  # строка 13
    [1, 0, 1, 1, 0],  # строка 14
    [1, 0, 1, 0, 1],  # строка 15
    [1, 0, 0, 1, 1]   # строка 16
]

# --- ПУНКТ 1: Расчет параметров ---
kolvo_soobshcheniy = 32784
n_i = 16  # Информационные разряды: ceil(log2(32784))
n_k = 5   # Контрольные разряды: удовлетворяют 2^5 >= 16 + 5 + 1
n_total = 21  # Общая длина кода: 16 + 5

print("="*60)
print("ПУНКТ 1: ПАРАМЕТРЫ ЛИНЕЙНОГО ГРУППОВОГО КОДА (ЛГК)")
print("="*60)
print(f"Количество сообщений: N = {kolvo_soobshcheniy}")
print(f"Информационные разряды: n_и = {n_i}")
print(f"Контрольные разряды: n_к = {n_k}")
print(f"Общая длина кодового слова: n = {n_total}\n")


# --- ПУНКТ 2: Кодирование и построение 10 кодовых комбинаций ---
def kodirovat_lgk(bity_info):
    kontrolnye_bity = [0] * 5
    for j in range(5):
        summa = 0
        for i in range(16):
            summa ^= (bity_info[i] & matrica_p[i][j])
        kontrolnye_bity[j] = summa
    return bity_info + kontrolnye_bity

print("="*60)
print("ПУНКТ 2: ПРИМЕР ПОСТРОЕНИЯ 10 КОДОВЫХ КОМБИНАЦИЙ ЛГК")
print("="*60)
print(f"{'№':<3} | {'Информационные разряды (16)':<27} | {'Кодовое слово ЛГК (21)':<25}")
print("-" * 75)

spisok_primerov = []
for idx in range(1, 11):
    dvoichniy_vid = f"{idx:016b}"
    bity = [int(b) for b in dvoichniy_vid]
    spisok_primerov.append(bity)
    
    kodoviy_vektor = kodirovat_lgk(bity)
    str_info = "".join(map(str, bity))
    str_kod = "".join(map(str, kodoviy_vektor[:16])) + " " + "".join(map(str, kodoviy_vektor[16:]))
    print(f"{idx:<3} | {str_info} | {str_kod}")
print("\n")


# --- ПУНКТ 4: Программа декодирования и исправления ошибок ---
def dekodirovat_lgk(kodoviy_vektor):
    bity_info = kodoviy_vektor[:16]
    bity_kontr = kodoviy_vektor[16:]
    
    # Расчет синдрома S = V_info * P ^ V_contr
    sindrom = [0] * 5
    for j in range(5):
        summa = 0
        for i in range(16):
            summa ^= (bity_info[i] & matrica_p[i][j])
        sindrom[j] = summa ^ bity_kontr[j]
        
    if sum(sindrom) == 0:
        return "Ошибок не обнаружено. Сообщение принято верно.", bity_info
        
    # Поиск совпадения синдрома со строками проверочной части P (ошибка в инфо-битах)
    for i in range(16):
        if matrica_p[i] == sindrom:
            ispravlennye = list(bity_info)
            ispravlennye[i] ^= 1
            return f"Исправлена одиночная ошибка в {i+1}-м информационном разряде.", ispravlennye
            
    # Поиск совпадения с единичным вектором (ошибка в контрольных битах)
    for j in range(5):
        edinichniy = [0] * 5
        edinichniy[j] = 1
        if edinichniy == sindrom:
            return f"Исправлена одиночная ошибка в {j+1}-м контрольном разряде.", bity_info
            
    return "Обнаружена неисправимая (кратная) ошибка.", None

# Тестирование на 10-м сообщении (0000000000001010)
print("="*60)
print("ПУНКТ 4: ТЕСТИРОВАНИЕ ДЕКОДЕРА ЛГК (Пример 10)")
print("="*60)

vibrannoe_soobshchenie = spisok_primerov[9] # 10-ое сообщение
str_vibrannogo = "".join(map(str, vibrannoe_soobshchenie))
print(f"Исходный вектор (16 бит):       {str_vibrannogo}")

pravilniy_vektor = kodirovat_lgk(vibrannoe_soobshchenie)
str_pravilnogo = "".join(map(str, pravilniy_vektor[:16])) + " " + "".join(map(str, pravilniy_vektor[16:]))
print(f"Закодированное слово (21 бит):  {str_pravilnogo}")

# Имитация одиночной ошибки в 13-м разряде
vektor_s_oshibkoy = list(pravilniy_vektor)
vektor_s_oshibkoy[12] ^= 1 # Искажаем 13-й информационный бит (индекс 12)
str_oshibki = "".join(map(str, vektor_s_oshibkoy[:16])) + " " + "".join(map(str, vektor_s_oshibkoy[16:]))
print(f"Принятый вектор с ошибкой:      {str_oshibki}")

# Декодирование
status, vosstanovlennoe = dekodirovat_lgk(vektor_s_oshibkoy)
print(f"Результат декодирования:        {status}")
print(f"Восстановленный вектор:         {''.join(map(str, vosstanovlennoe)) if vosstanovlennoe else '---'}")
print("="*60)