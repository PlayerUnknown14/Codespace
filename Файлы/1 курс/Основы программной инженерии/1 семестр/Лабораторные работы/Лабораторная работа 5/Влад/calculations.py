'''
ТЕХНИЧЕСКОЕ ЗАДАНИЕ:
Консольное приложение с выбором опций
1) Выбор операции
2) Задание размера массива
3) Задание диапазона возможных чисел
4) Получение результатов операции (возможность копировани в буфер???)
'''

import time
import random
import sys
import numpy as np
from random import *
from math import *

sys.set_int_max_str_digits(1000000)

operation_type = ''
operation_time = ''
gen_range = ''
gen_time = ''
list_size = ''
value_total = ''
massive = []

class Functions():
    def get_data():
        size = input("Укажите размер массива: ")
        left_border = input("Укажите наименьшее допустимое число в массиве: ")
        right_border = input("Укажите наибольшее допустимое число в массиве: ")
        
        return size, left_border, right_border
        
    def generation(size, left_border, right_border):
        global gen_time, massive
        
        time_start = time.time()
        massive = np.random.randint(left_border, right_border, size)
        time_end = time.time()
        gen_time = float(time_end - time_start)
    
class Operations():
    def addition():
        global operation_time, value_total, massive
        
        time_start = time.time()
        for i in massive:
            value_total += i
        time_end = time.time()
        operation_time = float(time_end - time_start)
    
    def subtraction():
        global operation_time, value_total, massive
        
        time_start = time.time()
        for i in massive:
            value_total -= i
        time_end = time.time()
        operation_time = float(time_end - time_start)

    def multiplication():
        global operation_time, value_total, massive
        
        time_start = time.time()
        value_total = 1
        for i in massive:
            value_total *= i
        time_end = time.time()
        operation_time = float(time_end - time_start)
    
    def division():
        global operation_time, value_total, massive
        
        time_start = time.time()
        value_total = 1
        for i in massive:
            value_total /= i
        time_end = time.time()
        operation_time = float(time_end - time_start)
    
    def square_root():
        global operation_time, value_total, massive
        
        time_start = time.time()
        value_total = 1
        for i in range(0, len(massive)-1):
            massive[i] ** 0.5
        time_end = time.time()
        operation_time = float(time_end - time_start)
    
    def square():
        global operation_time, value_total, massive
        
        time_start = time.time()
        value_total = 1
        for i in range(0, len(massive)-1):
            massive[i] ** 2
        time_end = time.time()
        operation_time = float(time_end - time_start)
        
while True:
    opt1 = input("Выберите опцию: \n1 - Начать работу\n2 - Выход")
    match opt1.split():
        case ["1"]:
            size, left_border, right_border = Functions.get_data()
            Functions.generation(size, left_border, right_border)
            
            opt2 = input("Выберите операцию: \n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Квадратный корень\n6 - Возведение во вторую степень")
            match opt2.split():
                case ["1"]:
                    Operations.addition()
                    print(f"Размер массива - {size}")
        case ["2"]:
            print("\nПрограмма закрыта")
            break