import math

# =====================================================================
# ПУНКТ 1: Расчет параметров кода
# =====================================================================
# Количество сообщений для Варианта 12
kolichestvo_soobsh = 32784

# Число информационных разрядов (n_и)
n_i = math.ceil(math.log2(kolichestvo_soobsh))

# Число контрольных разрядов для стандартного кода Хемминга (n_к)
n_k_stand = math.ceil(math.log2((n_i + 1) + math.log2(n_i + 1)))

# Для расширенного кода Хемминга (исправление одиночной и обнаружение двойной ошибки)
# Добавляется 1 общий контрольный бит четности
n_k_ext = n_k_stand + 1

# Общая разрядность кода (n)
n_stand = n_i + n_k_stand
n_ext = n_i + n_k_ext

print("="*60)
print("ПУНКТ 1: РАСЧЕТ ПАРАМЕТРОВ КОДА (Вариант 12)")
print("="*60)
print(f"Количество сообщений: N = {kolichestvo_soobsh}")
print(f"Число информационных разрядов: n_и = {n_i}")
print(f"Число контрольных разрядов (стандартный): n_к = {n_k_stand}")
print(f"Число контрольных разрядов (расширенный): n_к = {n_k_ext}")
print(f"Общая разрядность кода (стандартный): n = {n_stand}")
print(f"Общая разрядность кода (расширенный): n = {n_ext}")
print("\n")


# =====================================================================
# ПУНКТ 2: Построение 10 кодовых сообщений
# =====================================================================
def kodirovat_hamming_extended(iskhodnye_bity):
    kombinaciya = [0] * 23 # 1-индексация (индекс 0 не используется)
    
    # Записываем информационные биты на позиции, не являющиеся степенями двойки
    info_idx = 0
    for i in range(1, 22):
        if (i & (i - 1)) != 0: # если i не степень двойки
            kombinaciya[i] = iskhodnye_bity[info_idx]
            info_idx += 1
            
    # Вычисляем 5 стандартных контрольных разрядов (на позициях 1, 2, 4, 8, 16)
    for k in [1, 2, 4, 8, 16]:
        sum_xor = 0
        for i in range(1, 22):
            if i != k and (i & k) != 0:
                sum_xor ^= kombinaciya[i]
        kombinaciya[k] = sum_xor
        
    # Вычисляем общий бит четности (позиция 22)
    obshchaya_chetnost = 0
    for i in range(1, 22):
        obshchaya_chetnost ^= kombinaciya[i]
    kombinaciya[22] = obshchaya_chetnost
    
    return kombinaciya[1:] # возвращаем список из 22 бит

print("="*60)
print("ПУНКТ 2: ПРИМЕР ПОСТРОЕНИЯ 10 КОДОВЫХ СООБЩЕНИЙ")
print("="*60)
print(f"{'№':<3} | {'Информационные биты (16)':<26} | {'Закодированное сообщение (22)':<34}")
print("-" * 75)

spisok_soobshcheniy = []
for index in range(1, 11):
    # Генерируем простое уникальное 16-битное сообщение (числа от 1 до 10 в двоичном виде)
    dvoichniy_format = f"{index:016b}"
    bity = [int(bit) for bit in dvoichniy_format]
    spisok_soobshcheniy.append(bity)
    
    zakodirovannoe = kodirovat_hamming_extended(bity)
    stroka_info = "".join(map(str, bity))
    stroka_kod = "".join(map(str, zakodirovannoe))
    print(f"{index:<3} | {stroka_info} | {stroka_kod}")
print("\n")


# =====================================================================
# ПУНКТ 4: Декодирование с исправлением/обнаружением ошибок
# =====================================================================
def dekodirovat_hamming_extended(poluchennaya_kombinaciya):
    komb = [0] + poluchennaya_kombinaciya # переходим к 1-индексации
    
    # Вычисляем синдром
    sindrom = 0
    for step, k in enumerate([1, 2, 4, 8, 16]):
        sum_xor = 0
        for i in range(1, 22):
            if (i & k) != 0:
                sum_xor ^= komb[i]
        if sum_xor != 0:
            sindrom += k
            
    # Вычисляем общую четность по всем 22 позициям
    obshchaya_chetnost = 0
    for i in range(1, 23):
        obshchaya_chetnost ^= komb[i]
        
    # Анализируем синдром и общую четность
    iskhodnye_bity_vosstanovlennye = []
    sobytie = ""
    oshibochniy_razryad = -1
    
    if sindrom == 0 and obshchaya_chetnost == 0:
        sobytie = "Ошибок не обнаружено. Сообщение передано верно."
    elif sindrom != 0 and obshchaya_chetnost == 1:
        sobytie = f"Обнаружена одиночная ошибка в разряде {sindrom}. Ошибка исправлена."
        komb[sindrom] ^= 1 # Исправляем
        oshibochniy_razryad = sindrom
    elif sindrom == 0 and obshchaya_chetnost == 1:
        sobytie = "Обнаружена одиночная ошибка в общем контрольном бите (разряд 22). Ошибка исправлена."
        komb[22] ^= 1
        oshibochniy_razryad = 22
    elif sindrom != 0 and obshchaya_chetnost == 0:
        sobytie = "Обнаружена ДВОЙНАЯ ошибка! Исправление невозможно."
        
    # Выделяем информационные биты (позиции не степени двойки)
    if sindrom == 0 or obshchaya_chetnost == 1: 
        for i in range(1, 22):
            if (i & (i - 1)) != 0:
                iskhodnye_bity_vosstanovlennye.append(komb[i])
                
    return sobytie, iskhodnye_bity_vosstanovlennye, oshibochniy_razryad

# Демонстрация работы на примере 10-го сообщения (0000000000001010)
print("="*60)
print("ПУНКТ 4: ДЕМОНСТРАЦИЯ РАБОТЫ ДЕКОДЕРА (Пример 10)")
print("="*60)

vibrannoe_soobshchenie = spisok_soobshcheniy[9] # 10-ое сообщение
stroka_vibrannogo = "".join(map(str, vibrannoe_soobshchenie))
print(f"Исходное сообщение (16 бит):   {stroka_vibrannogo}")

# Кодирование
pravilniy_kod = kodirovat_hamming_extended(vibrannoe_soobshchenie)
stroka_pravilnogo = "".join(map(str, pravilniy_kod))
print(f"Закодированный вектор (22 бита): {stroka_pravilnogo}")

# 1. Декодирование без ошибок
status, rez, _ = dekodirovat_hamming_extended(pravilniy_kod)
print(f"\nСлучай 1: Передача без ошибок")
print(f"Результат декодирования:        {status}")
print(f"Восстановленное сообщение:      {''.join(map(str, rez)) if rez else '---'}")

# 2. Имитация одиночной ошибки в 5-м разряде
kod_s_odnoy_oshibkoy = list(pravilniy_kod)
kod_s_odnoy_oshibkoy[4] ^= 1 # Искажаем 5-й разряд (индекс 4)
print(f"\nСлучай 2: Имитация одиночной ошибки в 5-м разряде")
print(f"Искаженный вектор:              {''.join(map(str, kod_s_odnoy_oshibkoy))}")
status, rez, _ = dekodirovat_hamming_extended(kod_s_odnoy_oshibkoy)
print(f"Результат декодирования:        {status}")
print(f"Восстановленное сообщение:      {''.join(map(str, rez)) if rez else '---'}")

# 3. Имитация двойной ошибки в 5-м и 12-м разрядах
kod_s_dvumya_oshibkami = list(pravilniy_kod)
kod_s_dvumya_oshibkami[4] ^= 1  # 5-й разряд (индекс 4)
kod_s_dvumya_oshibkami[11] ^= 1 # 12-й разряд (индекс 11)
print(f"\nСлучай 3: Имитация двойной ошибки в 5-м и 12-м разрядах")
print(f"Искаженный вектор:              {''.join(map(str, kod_s_dvumya_oshibkami))}")
status, rez, _ = dekodirovat_hamming_extended(kod_s_dvumya_oshibkami)
print(f"Результат декодирования:        {status}")
print(f"Восстановленное сообщение:      {''.join(map(str, rez)) if rez else '---'}")
print("="*60)