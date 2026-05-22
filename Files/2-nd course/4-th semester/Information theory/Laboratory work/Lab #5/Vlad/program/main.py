from header import LinearGroupCoder

def simulate_error(code_str, position):
    """Внесение ошибки в строку."""
    code_list = list(code_str)
    idx = position - 1
    if 0 <= idx < len(code_list):
        code_list[idx] = '1' if code_list[idx] == '0' else '0'
    return "".join(code_list)

def main():
    # 5 вариант: 256 сообщений
    coder = LinearGroupCoder(num_messages=256)

    while True:
        print("\n--- ЛАБОРАТОРНАЯ РАБОТА № 5 ---")
        print("1. Расчёт параметров и вывод порождающей матрицы G")
        print("2. Пример построения 10 кодовых сообщений")
        print("3. Демонстрация исправления одиночной ошибки")
        print("0. Выход")
        
        choice = input("Выбор: ")

        if choice == "1":
            print("\n" + "="*40)
            print("ПАРАМЕТРЫ ЛГК")
            print("="*40)
            print(f"Количество сообщений (N): {256}")
            print(f"Информационных разрядов (n_и): {coder.n_i}")
            print(f"Контрольных разрядов (n_к): {coder.n_k}")
            print(f"Общая длина кода (n): {coder.n}")
            print("\nПорождающая матрица G = [ I | P ]:")
            # Выводим матрицу G для наглядности (I - единичная 8x8, P - 8x4)
            for i in range(coder.n_i):
                i_row = ["1" if k == i else "0" for k in range(coder.n_i)]
                p_row = [str(x) for x in coder.P[i]]
                print(f"  {' '.join(i_row)} | {' '.join(p_row)}")

        elif choice == "2":
            print("\n" + "="*40)
            print("ПОСТРОЕНИЕ 10 СЛУЧАЙНЫХ СООБЩЕНИЙ")
            print("="*40)
            print(f"{'№':<3} | {'Инфо-данные':<12} | {'Систематический ЛГК (Инфо + Проверка)'}")
            print("-" * 65)
            for i in range(1, 11):
                # Генерируем случайную 8-битную строку
                data = coder.generate_data_string()
                encoded = coder.encode(data)
                formatted_encoded = f"{encoded[:coder.n_i]} {encoded[coder.n_i:]}"
                print(f"{i:<3} | {data:<12} | {formatted_encoded}")

        elif choice == "3":
            print("\n" + "="*40)
            print("СИМУЛЯТОР КАНАЛА С ПОМЕХАМИ")
            print("="*40)
            data = coder.generate_data_string()
            encoded = coder.encode(data)
            print(f"Сгенерированые данные: {data}")
            print(f"Отправленный в канал ЛГК: {encoded}")

            err_input = input("\nУкажите позицию для внесения ошибки (от 1 до 12): ").strip()               
            err_pos = int(err_input)
            received = simulate_error(encoded, err_pos)
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