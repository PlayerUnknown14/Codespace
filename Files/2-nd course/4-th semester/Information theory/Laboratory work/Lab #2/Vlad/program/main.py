from header import TextEntropyAnalyzer

def print_results(metrics):
    if not metrics: 
        return
    
    print("\n" + "="*40)
    print("РЕЗУЛЬТАТЫ РАСЧЕТОВ")
    print("="*40)
    print(f"H(X) [Энтропия источника]: {metrics['H(X)']:.4f} бит/симв")
    print(f"H(Y) [Энтропия приемника]: {metrics['H(Y)']:.4f} бит/симв")
    print(f"H(X, Y) [Энтропия объединения]: {metrics['H(X,Y)']:.4f} бит/симв")
    print(f"H(Y/X) [Потери при передаче]: {metrics['H(Y/X)']:.4f} бит/симв")
    print(f"H(X/Y) [Потери при приеме]: {metrics['H(X/Y)']:.4f} бит/симв")

    print("\nЧастные потери H(Y/xi):")
    len_xi = len(metrics['partial_Y_xi'])
    for i, val in enumerate(metrics['partial_Y_xi'][:len_xi]):
        print(f"  H(Y/x{i+1}): {val:.4f} бит/симв")
        
    print("\nЧастные потери H(X/yi):")
    len_yj = len(metrics['partial_X_yj'])
    for i, val in enumerate(metrics['partial_X_yj'][:len_yj]):
        print(f"  H(X/y{i+1}): {val:.4f} бит/симв")      

    print("="*40)

def main():
    analyzer = TextEntropyAnalyzer()
    
    while True:
        print("\n--- ЛАБОРАТОРНАЯ РАБОТА № 2 ---")
        print("1. Задание 1: Исследование канала (Матрица 10x10)")
        print("2. Задание 2: Анализ текста (Биграммы, 32 знака)")
        print("0. Выход")
        
        choice = input("Выберите пункт: ")

        if choice == "1":
            analyzer.build_random_matrix(size=10)
            metrics = analyzer.calculate_entropy()
            print("\nСгенерирована случайная матрица совместных вероятностей 10x10.")
            print_results(metrics)
            
        elif choice == "2":
            fname = input("Введите имя файла (по умолчанию 'input.txt'): ") or "input.txt"
            if not analyzer.build_from_text(fname):
                print(f"\nОшибка при обработке файла '{fname}'.")
                continue
            metrics = analyzer.calculate_entropy()
            print(f"\nТекст из файла '{fname}' обработан.")
            print_results(metrics)
                
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()