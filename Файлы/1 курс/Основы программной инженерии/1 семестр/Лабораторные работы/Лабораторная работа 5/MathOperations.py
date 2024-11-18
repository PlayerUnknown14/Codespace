import time
from random import randint
import random
from tkinter import *
from tkinter import ttk
from random import *
import tkinter as tk

root = tk.Tk()
root.title('MathOperations')
root.geometry('500x500')

mass = []

def clicked():
    text = Combobox.get()   
    if text == 'Сложение':
        вычисления.summa()
class вычисления:
    def summa():
        global mass
        amount = amount_entry.get()
        range = range_entry.get().split(' ')
        rangemin = int(range[0])
        rangemax = int(range[1])
        mass = [randint(rangemin, rangemax) for i in range(int(amount))]
        start_time = time.time()
        summass = sum(mass)
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        mass_label.configure(text=f'Сумма массива: {summass}')
        print(f'Сумма массива: {summass}')
        print(f"Время выполнения программы: {execution_time} секунд")



Operations = ['Сложение', 'Вычитание', 'Умножение', 'Деление', 'Корни']
Operations_var = StringVar(value=Operations[0])

Combobox = ttk.Combobox(textvariable=Operations_var, values=Operations, state='readonly')
Combobox.pack(anchor=NW, padx=6, pady=6)

num = 30

amount_label = ttk.Label(text='Введите количество элементов массива')
amount_label.place(x=6,y=num)

amount_entry = ttk.Entry()
amount_entry.place(x=6, y=num+20)

range_label = ttk.Label(text='Введите через пробел диапазон генерируемых чисел')
range_label.place(x=6, y =num*2+20)

range_entry = ttk.Entry()
range_entry.place(x=6, y=num*3+20)

start_button = ttk.Button(text='Старт', command=clicked)
start_button.place(x=6, y=num*4+20)

time_label = ttk.Label(text='')
time_label.place(x=6, y=num*5+20)

mass_label = ttk.Label(text='')
mass_label.place(x=6, y=num*6+20)

root.mainloop()