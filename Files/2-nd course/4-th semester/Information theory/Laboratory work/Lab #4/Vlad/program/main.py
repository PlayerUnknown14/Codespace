import random
from header import HammingCoder

def simulate_error(code_str: str, positions: list) -> str:
    """Функция для искусственного внесения ошибки (инверсии битов) в строку."""
    code_list = list(code_str)
    for pos in positions:
        # Индексация для пользователя с 1, поэтому отнимаем 1 для массива
        idx = pos - 1
        if 0 <= idx < len(code_list):
            code_list[idx] = '1' if code_list[idx] == '0' else '0'
    return "".join(code_list)

def main():
    # Инициализация для 5 варианта (256 сообщений)
    coder = HammingCoder(num_messages=256)

    while True:
        print("\n" + "="*50)
        print(" ЛАБОРАТОРНАЯ РАБОТА № 4. КОД ХЕММИНГА (Вар. 5)")
        print("="*50)
        print("1. Рассчитать параметры кода (n_и, n_к, n)")
        print("2. Пример построения 10 кодовых сообщений")
        print("3. Демонстрация исправления и обнаружения ошибок")
        print("0. Выход")
        
        choice = input("\nВыберите пункт меню: ")

        if choice == "1":
            print("\n--- ПАРАМЕТРЫ КОРРЕКТИРУЮЩЕГО КОДА ---")
            print(f"Количество сообщений (N): {256}")
            print(f"Информационных разрядов (n_и): {coder.n_i}")
            print(f"Контрольных разрядов (n_к):    {coder.n_k}")
            print(f"Общая длина клас. кода (n):    {coder.n}")
            print(f"Длина расширенного кода:       {coder.n_ext}")
            print("Минимальное кодовое расстояние d_min = 4")

        elif choice == "2":
            print("\n--- ПОСТРОЕНИЕ 10 СЛУЧАЙНЫХ СООБЩЕНИЙ ---")
            print(f"{'№':<3} | {'Инфо-данные':<12} | {'Расширенный код Хемминга'}")
            print("-" * 50)
            for i in range(1, 11):
                # Генерируем случайную 8-битную строку
                rand_data = "".join(random.choice("01") for _ in range(coder.n_i))
                encoded = coder.encode(rand_data)
                print(f"{i:<3} | {rand_data:<12} | {encoded}")

        elif choice == "3":
            print("\n--- СИМУЛЯТОР КАНАЛА С ПОМЕХАМИ ---")
            data = input(f"Введите {coder.n_i} бит информации (или Enter для случайных): ").strip()
            if not data or len(data) != coder.n_i or not all(c in "01" for c in data):
                data = "".join(random.choice("01") for _ in range(coder.n_i))
                print(f"Сгенерированы данные: {data}")

            # 1. Кодирование
            encoded = coder.encode(data)
            print(f"\nОтправлено в канал:   {encoded}")

            # 2. Внесение ошибок
            err_input = input("Введите позиции ошибок через запятую (например: 5 или 3,7): ").strip()
            err_positions =[int(x.strip()) for x in err_input.split(",") if x.strip().isdigit()]
            
            received = simulate_error(encoded, err_positions)
            print(f"Принято из канала:    {received}")

            # 3. Декодирование
            status, corrected, decoded_data = coder.decode(received)
            print("\n--- РЕЗУЛЬТАТ РАБОТЫ ДЕКОДЕРА ---")
            print(f"Статус:         {status}")
            print(f"Код на выходе:  {corrected}")
            print(f"Данные (n_и):   {decoded_data}")

        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, повторите попытку.")

if __name__ == "__main__":
    main()