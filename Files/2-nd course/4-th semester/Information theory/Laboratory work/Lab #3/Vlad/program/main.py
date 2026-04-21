from header import TextAnalyzer

def demonsrate_text_processing(analyzer):
    if not analyzer.processed_text:
        print("Текст не загружен!")
        return

    # Извлекаем минимум 4 абзаца
    paragraphs = [p.strip() for p in analyzer.processed_text.split('\n') if p.strip()]
    if len(paragraphs) < 4:
        sample_text = "\n\n".join(paragraphs)
    else:
        sample_text = "\n\n".join(paragraphs[:4])
    print(f"Извлечено абзацаов из текста: {len(paragraphs)}.")

    print("\n" + "="*40)
    print("КОДИРОВАНИЕ И ДЕКОДИРОВАНИЕ ТЕКСТА")
    print("="*40)
    print(f"ИСХОДНЫЙ ТЕКСТ:\n{sample_text}\n")

    methods = [
        ("Шеннон-Фано", analyzer.build_shannon_fano),
        ("Хаффман", analyzer.build_huffman)
    ]

    for name, build_func in methods:
        build_func() # Строим коды
        encoded = analyzer.encode(sample_text)
        decoded = analyzer.decode(encoded)
        l_cp, k_cc, k_oe = analyzer.get_efficiency()

        print(f"--- МЕТОД: {name} ---")
        print(f"Средняя длина символа кодового алфавита (Lcp): {l_cp:.4f} бит/симв")
        print(f"Коэффициент статического сжатия (Kcc): {k_cc:.4f}")
        print(f"Коэффициент относительной эффективности (Koe): {k_oe:.4f}")
        print(f"Закодированная последовательность (первые 100 бит):\n{encoded[:100]}...")
        print(f"Результат декодирования:\n{decoded}")
        print(f"Проверка целостности: {'УСПЕШНО' if decoded == sample_text else 'ОШИБКА'}")
        print("-" * 30)

def main():
    analyzer = TextAnalyzer()

    while True:
        print("\n--- ЛАБОРАТОРНАЯ РАБОТА № 3 ---")
        print("1. Загрузить текст из файла")
        print("2. Задание 1: Расчет избыточности (D)")
        print("3. Задания 2-4: Кодирование/декодирование текста")
        print("0. Выход")
        
        choice = input("Выбор: ")
        
        if choice == "1":
            fname = input("Введите имя файла (по умолчанию 'input.txt'): ") or "input.txt"
            analyzer.preprocess_text(analyzer.load_file(fname))
            print(f"Текст загружен ({analyzer.text_length} символов)")
            
        elif choice == "2":
            if not analyzer.processed_text:
                print("Текст не загружен! Сначала выберите пункт 1.")
                continue
            
            dp, ds, d = analyzer.analyze_redundancy(analyzer.processed_text)
            print(f"Избыточность, вызванная неравномерностью распределения символов (Dp): {dp:.4f}")
            print(f"Избыточность, вызванная статистической связью между соседними символами (Ds): {ds:.4f}")
            print(f"Полная избыточность (D): {d:.4f}")

        elif choice == "3":
            demonsrate_text_processing(analyzer)
            
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()