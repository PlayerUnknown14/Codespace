import time
from random import randint
import random
from tkinter import *
from tkinter import ttk
from random import *
import tkinter as tk
import sys

sys.set_int_max_str_digits(1121241)

root = tk.Tk()
root.title('MathOperations')
root.geometry('500x500')


def clicked():
    text = Combobox.get()   
    if text == 'Сложение':
        Operations.slozhenie()
    if text == 'Вычитание':
        Operations.raznost()
    if text == 'Умножение':
        Operations.umnozh()
        
        
class Others:
    def simplegeneration():
        amount = amount_entry.get()
        rangeran = range_entry.get().split(' ')
        rangemin = int(rangeran[0])
        rangemax = int(rangeran[1])
        massgen = [randint(rangemin, rangemax) for i in range(int(amount))]
        return massgen
    def hardgeneration():
        amount = amount_entry.get()
        rangeran = range_entry.get().split(' ')
        rangemin = int(rangeran[0])
        rangemax = int(rangeran[1])
        massgen = []
        for i in range(int(amount)//2):
            massgen.append(randint(rangemin, rangemax))
            massgen.append(1/randint(rangemin, rangemax))
        return massgen
class Operations:
    def slozhenie():
        massgen = Others.simplegeneration()
        start_time = time.time()
        summass = sum(massgen)
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        mass_label.configure(text=f'Сумма массива: {summass}')

    def raznost():
        massgen = Others.simplegeneration()
        itograzn = 0
        start_time = time.time()
        for i in massgen:
            itograzn-=i

        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        mass_label.configure(text=f'Разность массива: {itograzn}')
        
    def umnozh():
        massgen = Others.hardgeneration()
        itogumnozh = 1
        start_time = time.time()
        for i in massgen:
            itogumnozh*=i
        
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        mass_label.configure(text=f'Произведение массива: {itogumnozh}')
        


Operationslist = ['Сложение', 'Вычитание', 'Умножение', 'Деление', 'Корни']
Operations_var = StringVar(value=Operationslist[0])

Combobox = ttk.Combobox(textvariable=Operations_var, values=Operationslist, state='readonly')
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