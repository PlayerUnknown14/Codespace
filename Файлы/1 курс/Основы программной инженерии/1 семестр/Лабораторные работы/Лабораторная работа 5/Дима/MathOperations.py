import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
import sys
from math import sqrt, log10
import numpy as np

sys.set_int_max_str_digits(1121241)
root = tk.Tk()
root.title('MathOperations')
root.geometry('500x500')

clipboardmemory = ''
typeofgen = ''
timeofoperations = ''
timeofgen = ''
lengthofgen = ''
totalvalue = 0
rangeofgen = ''

def clicked():
    match Comboboxtype.get().split():
        case ["Int"]:
            match Comboboxop.get().split():
                case ["Сложение"]:
                    IntOperations.slozhenie()
                case ["Вычитание"]:
                    IntOperations.raznost()
                case ["Умножение"]:
                    IntOperations.umnozh()
                case ["Деление"]:
                    IntOperations.delenie()
                case ["Корни"]:
                    IntOperations.korni()
                case ["Логарифмы"]:
                    IntOperations.log()
        case ["Float"]:
            match Comboboxop.get().split():
                case ["Сложение"]:
                    FloatOperations.slozhenie()
                case ["Вычитание"]:
                    FloatOperations.raznost()
                case ["Умножение"]:
                    FloatOperations.umnozh()
                case ["Деление"]:
                    FloatOperations.delenie()
                case ["Корни"]:
                    FloatOperations.korni()
                case ["Логарифмы"]:
                    FloatOperations.log()
            
        
class Gen:
    def integer():
        global timeofgen
        start_time = time.time()
        
        amount = amount_entry.get()
        rangeran = range_entry.get().split(' ')
        rangemin = int(rangeran[0])
        rangemax = int(rangeran[1])
        massgen = np.random.randint(rangemin, rangemax, int(amount))
        
        end_time = time.time()
        timeofgen = end_time - start_time
        return massgen
    def float():
        global timeofgen
        start_time = time.time()
        
        amount = amount_entry.get()
        rangeran = range_entry.get().split(' ')
        rangemin = float(rangeran[0])
        rangemax = float(rangeran[1])
        massgen = np.random.uniform(rangemin, rangemax, int(amount))
        
        end_time = time.time()
        timeofgen = end_time - start_time
        return massgen
class Clipboard:
    def cl():
        root.clipboard_clear()
        root.clipboard_append(clipboardmemory)
        root.update()
        
    def generalcl():
        text = f'Тип вычислений: {typeofgen}\nВремя генерации массива: {timeofgen}\nВремя вычислений: {timeofoperations}\nКоличество элементов массива: {lengthofgen}\nПолучившееся значение: {totalvalue}\nДиапазон данных:{rangeofgen}'
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        
    def generalclclear():
        text = f'{typeofgen}\n{timeofgen}\n{timeofoperations}\n{lengthofgen}\n{totalvalue}\n{rangeofgen}'
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()      

        
class IntOperations:
    def slozhenie(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        
        massgen = Gen.integer()
        start_time = time.time()
        summass = sum(massgen)
        end_time = time.time()
        execution_time = float(end_time - start_time)
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Сумма массива: {summass}')
        
        typeofgen = 'Сложение'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = summass
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def raznost():
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.integer()
        itograzn = 0
        start_time = time.time()
        for i in massgen:
            itograzn-=i

        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Разность массива: {itograzn}')

        typeofgen = 'Вычитание'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = itograzn
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def umnozh(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.integer()
        itogumnozh = massgen[0]
        start_time = time.time()
        
        for i in massgen:
            itogumnozh = itogumnozh*i
        
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Произведение массива: {itogumnozh}')
        
        typeofgen = 'Умножение'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = itogumnozh
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def delenie(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.integer()
        itogdel = 1
        start_time = time.time()
        for i in massgen:
            itogdel = float(itogdel/i)
        
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Произведение массива: {itogdel}')
        
        typeofgen = 'Деление'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = itogdel
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'
        
    def korni(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.integer()
        start_time = time.time()
        for i in range(0, len(massgen)-1):
            bufer = sqrt(massgen[i])
            massgen[i] = bufer
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'')
        
        typeofgen = 'Корни'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = 'Процесс операции "Корни" не подразумевает итогового значения'
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def log(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.integer()
        start_time = time.time()
        for i in range(0, len(massgen)-1):
            bufer = log10(massgen[i])
            massgen[i] = bufer
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'')
        
        typeofgen = 'Логарифм'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = 'Процесс операции "Логарифм" не подразумевает итогового значения'
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'
        
class FloatOperations:
    def slozhenie(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        
        massgen = Gen.float()
        start_time = time.time()
        summass = sum(massgen)
        end_time = time.time()
        execution_time = float(end_time - start_time)
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Сумма массива: {summass}')
        
        typeofgen = 'Сложение'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = summass
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def raznost():
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.float()
        itograzn = 0
        start_time = time.time()
        for i in massgen:
            itograzn-=i

        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Разность массива: {itograzn}')

        typeofgen = 'Вычитание'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = itograzn
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def umnozh(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.float()
        itogumnozh = massgen[0]
        start_time = time.time()
        
        for i in massgen:
            itogumnozh = itogumnozh*i
        
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Произведение массива: {itogumnozh}')
        
        typeofgen = 'Умножение'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = itogumnozh
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def delenie(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.float()
        itogdel = 1
        start_time = time.time()
        for i in massgen:
            itogdel = float(itogdel/i)
        
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'Произведение массива: {itogdel}')
        
        typeofgen = 'Деление'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = itogdel
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'
        
    def korni(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.float()
        start_time = time.time()
        for i in range(0, len(massgen)-1):
            bufer = sqrt(massgen[i])
            massgen[i] = bufer
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'')
        
        typeofgen = 'Корни'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = 'Процесс операции "Корни" не подразумевает итогового значения'
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

    def log(): 
        global clipboardmemory, typeofgen, timeofgen, timeofoperations, lengthofgen, totalvalue, rangeofgen
        
        massgen = Gen.float()
        start_time = time.time()
        for i in range(0, len(massgen)-1):
            bufer = log10(massgen[i])
            massgen[i] = bufer
        end_time = time.time()
        execution_time = end_time - start_time
        time_label.configure(text=f'Время выполнения программы: {execution_time} секунд')
        timemass_label.configure(text=f'Время генерации массива: {timeofgen} секунд')
        mass_label.configure(text=f'')
        
        typeofgen = 'Логарифм'
        timeofoperations = execution_time
        lengthofgen = len(massgen)
        totalvalue = 'Процесс операции "Логарифм" не подразумевает итогового значения'
        rangeofgen = f'{min(massgen)};{max(massgen)}'
        clipboardmemory = f'Время выполнения программы: {execution_time} секунд'

Operationslist = ['Сложение', 'Вычитание', 'Умножение', 'Деление', 'Корни', 'Логарифм']
Operations_var = StringVar(value=Operationslist[0])

Comboboxop = ttk.Combobox(textvariable=Operations_var, values=Operationslist, state='readonly')
Comboboxop.place(x=6,y=6)

Typelist = ['Int', 'Float']
Typelist_var = StringVar(value=Typelist[0])

Comboboxtype = ttk.Combobox(textvariable=Typelist_var, values=Typelist, state='readonly')
Comboboxtype.place(x=156, y=6)


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

timemass_label = ttk.Label(text='')
timemass_label.place(x=6, y=num*6+20)

clipboardbtn = ttk.Button(text='Скопировать', command=Clipboard.cl)
clipboardbtn.place(x = 6, y=num*7+20)

mass_label = ttk.Label(text='')
mass_label.place(x=6, y=num*8+20)

generalinfobtn = ttk.Button(text='Скопировать\nобщую\nинформцию', command=Clipboard.generalcl)
generalinfobtn.place(x=6, y=num*14+20)

generalinfobtn = ttk.Button(text='Скопировать\nобщую\nинформцию без текста', command=Clipboard.generalclclear)
generalinfobtn.place(x=96, y=num*14+20)

root.mainloop()
