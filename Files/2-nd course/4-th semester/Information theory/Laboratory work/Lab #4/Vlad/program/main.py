from header import HammingCoder

def simulate_error(code_str, positions):
    """Внесение ошибок в строку."""
    code_list = list(code_str)
    for pos in positions:
        idx = pos - 1
        if 0 <= idx < len(code_list):
            code_list[idx] = '1' if code_list[idx] == '0' else '0'
    return "".join(code_list)

def main():
    # 5 вариант: 256 сообщений
    coder = HammingCoder(num_messages=256)

    while True:
        print("\n--- ЛАБОРАТОРНАЯ РАБОТА № 4 ---")
        print("1. Задание 1: Рассчёт параметров кода")
        print("2. Задание 2: Пример построения 10 кодовых сообщений")
        print("3. Задания 3-4: Демонстрация исправления и обнаружения ошибок")
        print("0. Выход")
        
        choice = input("Выбор: ")

        if choice == "1":
            print("\n" + "="*40)
            print("ПАРАМЕТРЫ КОРРЕКТИРУЮЩЕГО КОДА")
            print("="*40)
            print(f"Количество сообщений (N): {256}")
            print(f"Информационных разрядов (n_и): {coder.n_i}")
            print(f"Контрольных разрядов (n_к): {coder.n_k}")
            print(f"Общая длина классического кода Хемминга (n): {coder.n}")
            print(f"Длина расширенного кода: {coder.n_ext}")

        elif choice == "2":
            print("\n" + "="*40)
            print("ПОСТРОЕНИЕ 10 СЛУЧАЙНЫХ СООБЩЕНИЙ")
            print("="*40)
            print(f"{'№':<3} | {'Инфо-данные':<12} | {'Расширенный код Хемминга'}")
            print("-" * 50)
            for i in range(1, 11):
                # Генерируем случайную 8-битную строку
                data = coder.generate_data_string()
                encoded = coder.encode(data)
                print(f"{i:<3} | {data:<12} | {encoded}")

        elif choice == "3":
            print("\n" + "="*40)
            print("СИМУЛЯТОР КАНАЛА С ПОМЕХАМИ")
            print("="*40)
            data = coder.generate_data_string()
            encoded = coder.encode(data)
            print(f"Сгенерированые данные: {data}")
            print(f"Отправленный в канал код: {encoded}")

            err_input = input("\nУкажите до двух позиций ошибок при прохождении через канал (например, 5 или 3,7): ").strip()
            err_positions = [int(x.strip()) for x in err_input.split(",") if x.strip().isdigit()]

            received = simulate_error(encoded, err_positions)
            print(f"\nПолученный из канала код (с ошибками): {received}")
            
            status, corrected, decoded_data = coder.decode(received)
            print(f"\nСтатус декодирования: {status}")
            print(f"Исправленный код: {corrected}")
            print(f"Итоговая последовательность данных: {decoded_data}")

        elif choice == "0":
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()