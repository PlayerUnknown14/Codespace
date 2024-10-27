import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tabulate

columns = ["Номер", "Марка", "Модель", "Тип двигателя", "Цвет", "Мощность"]

def get_data():
    with open("cars_table2.txt", 'r+', encoding='utf-16-be') as file:
        data = file.readlines()
        r = []
        for line in data:
            S = line.strip().split('/')
            r.append(S)
        return r

def delete_car(number):
    data = get_data()
    with open("cars_table2.txt", 'r+', encoding='utf-16-be') as file:
        rdata = []
        for i, line in enumerate(data):
            if int(line[0]) != number:
                rdata.append(line)
        for i in range(len(rdata)):
            rdata[i][0] = str(i + 1)
        s = ["/".join(x) for x in rdata]
        file.write("\n".join(s))
        update_data()

def change_car(number):
    data = get_data()
    for i, line in enumerate(data):
        if int(line[0]) == number:
            r = [line]
            break
    else:
        messagebox.showinfo("Ошибка", "Машины с таким номером нет")
        return

    def change_value(column_index, new_value):
        data[number - 1][column_index] = new_value
        with open("cars_table2.txt", 'w+', encoding='utf-16-be') as file:
            s = ["/".join(x) for x in data]
            file.write("\n".join(s))
        update_data()

    change_window = tk.Toplevel(root)
    change_window.title(f"Редактирование машины №{number}")

    print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
    for i, column in enumerate(columns):
        label = tk.Label(change_window, text=f"{column}:")
        label.grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(change_window)
        entry.insert(0, r[0][i])
        entry.grid(row=i, column=1, padx=5, pady=5)
        entry.bind("<Return>", lambda event, index=i: change_value(index, entry.get()))
    update_data()

def add_car():
    def find_num():
        data = get_data()
        number = 0
        for line in data:
            num1 = int(line[0])
            if num1 > number:
                number = num1
        return number
    def add_car_to_file():
        brand = brand_entry.get()
        model = model_entry.get()
        engine_type = engine_type_entry.get()
        color = color_entry.get()
        power = power_entry.get()
        if any([x.count('/') > 0 for x in [brand, model, engine_type, color, power]]):
            messagebox.showinfo("Ошибка", "Введен запрещенный символ: /")
            return
        num = find_num() + 1
        car_string = f'{num}/{brand}/{model}/{engine_type}/{color}/{power}'
        with open("cars_table2.txt", 'a+', encoding='utf-16-be') as file:
            file.write(f"{car_string}\n")
        add_car_window.destroy()
        update_data()

    add_car_window = tk.Toplevel(root)
    add_car_window.title("Добавить машину")

    brand_label = tk.Label(add_car_window, text="Марка:")
    brand_label.grid(row=0, column=0, padx=5, pady=5)
    brand_entry = tk.Entry(add_car_window)
    brand_entry.grid(row=0, column=1, padx=5, pady=5)

    model_label = tk.Label(add_car_window, text="Модель:")
    model_label.grid(row=1, column=0, padx=5, pady=5)
    model_entry = tk.Entry(add_car_window)
    model_entry.grid(row=1, column=1, padx=5, pady=5)

    engine_type_label = tk.Label(add_car_window, text="Тип двигателя:")
    engine_type_label.grid(row=2, column=0, padx=5, pady=5)
    engine_type_entry = tk.Entry(add_car_window)
    engine_type_entry.grid(row=2, column=1, padx=5, pady=5)

    color_label = tk.Label(add_car_window, text="Цвет:")
    color_label.grid(row=3, column=0, padx=5, pady=5)
    color_entry = tk.Entry(add_car_window)
    color_entry.grid(row=3, column=1, padx=5, pady=5)

    power_label = tk.Label(add_car_window, text="Мощность:")
    power_label.grid(row=4, column=0, padx=5, pady=5)
    power_entry = tk.Entry(add_car_window)
    power_entry.grid(row=4, column=1, padx=5, pady=5)

    add_button = tk.Button(add_car_window, text="Добавить", command=add_car_to_file)
    add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

def find_car():
    def find_car_by_number():
        try:
            number_for_find = int(find_entry.get())
        except ValueError:
            messagebox.showinfo("Ошибка", "Введён некорректный номер автомобиля.")
            return
        data = get_data()
        for i, line in enumerate(data):
            if int(line[0]) == number_for_find:
                r = [line]
                break
        else:
            messagebox.showinfo("Ошибка", "Автомобиль с таким номером не найден.")
            return

        find_window = tk.Toplevel(root)
        find_window.title(f"Информация о машине №{number_for_find}")
        
        for i, column in enumerate(columns):
            label = tk.Label(find_window, text=f"{column}: {r[0][i]}")
            label.pack()

    find_window = tk.Toplevel(root)
    find_window.title("Поиск машины")

    find_label = tk.Label(find_window, text="Введите номер машины:")
    find_label.pack()
    find_entry = tk.Entry(find_window)
    find_entry.pack()

    find_button = tk.Button(find_window, text="Найти", command=find_car_by_number)
    find_button.pack()

def update_data():
    data = get_data()
    tree.delete(*tree.get_children())
    for i, line in enumerate(data):
        tree.insert("", "end", values=line)
        
root = tk.Tk()
root.title("База данных машин")

tree = ttk.Treeview(root, columns=columns, show='headings')
for column in columns:
    tree.column(column, width=100, anchor='center')
    tree.heading(column, text=column)

tree.pack()

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Выход", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Добавить автомобиль", command=add_car)
editmenu.add_command(label="Изменить автомобить", command=lambda: change_car(int(tree.item(tree.selection()[0])['values'][0])))
editmenu.add_command(label="Удалить автомобиль", command=lambda: delete_car(int(tree.item(tree.selection()[0])['values'][0])))
editmenu.add_separator()
editmenu.add_command(label="Найти машину", command=find_car)
menubar.add_cascade(label="Редактировать", menu=editmenu)

root.config(menu=menubar)

update_data()

root.mainloop()