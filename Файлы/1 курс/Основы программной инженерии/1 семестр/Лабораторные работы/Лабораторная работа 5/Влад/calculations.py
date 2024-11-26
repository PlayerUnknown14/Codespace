import time
import sys
import numpy as np
from random import *
from math import *

sys.set_int_max_str_digits(1000000000)

class Functions():
    def get_data():
        size = int(input("Укажите размер массива: "))
        left_border = int(input("Укажите наименьшее допустимое число в массиве: "))
        right_border = int(input("Укажите наибольшее допустимое число в массиве: "))
        
        return size, left_border, right_border
        
    def generation(size, left_border, right_border):
        global gen_time, massive, operation_type
        
        if operation_type == "Умножение" or operation_type == "Деление":
            time_start = time.time()
            for i in range(int(size)//2):
                massive.append(randint(left_border, right_border))
                massive.append(1/randint(left_border, right_border))
            time_end = time.time()
            gen_time = float(time_end - time_start)
        else:
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
        value_total = "X"
        for i in range(0, len(massive)-1):
            massive[i] ** 0.5
        time_end = time.time()
        operation_time = float(time_end - time_start)
    
    def square():
        global operation_time, value_total, massive
        
        time_start = time.time()
        value_total = "X"
        for i in range(0, len(massive)-1):
            massive[i] ** 2
        time_end = time.time()
        operation_time = float(time_end - time_start)
        
while True:
    operation_type = ''
    operation_time = 0
    gen_time = 0
    list_size = 0
    value_total = 0
    massive = []
    opt1 = input("Выберите опцию: \n1 - Начать работу\n2 - Выход\nВвод: ")
    match opt1.split():
        case ["1"]:
            list_size, left_border, right_border = Functions.get_data()
            
            opt2 = input("Выберите операцию: \n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Квадратный корень\n6 - Возведение во вторую степень\nВвод: ")
            match opt2.split():
                case ["1"]:
                    operation_type = "Сложение"
                    Functions.generation(list_size, left_border, right_border)
                    Operations.addition()
                case ["2"]:
                    operation_type = "Вычитание"
                    Functions.generation(list_size, left_border, right_border)
                    Operations.subtraction()
                case ["3"]:
                    operation_type = "Умножение"
                    Functions.generation(list_size, left_border, right_border)
                    Operations.multiplication()
                case ["4"]:
                    operation_type = "Деление"
                    Functions.generation(list_size, left_border, right_border)
                    Operations.division()
                case ["5"]:
                    operation_type = "Квадратный корень числа"
                    Functions.generation(list_size, left_border, right_border)
                    Operations.square_root()
                case ["6"]:
                    operation_type = "Квадрат числа"
                    Functions.generation(list_size, left_border, right_border)
                    Operations.square()
                                                      
            print(f"\nТип операции - {operation_type}\nРазмер массива - {list_size}\nДиапазон - [{left_border}, {right_border}]\nВремя генерации - {gen_time}\nВремя проведения операции - {operation_time}\nПолученное значение - {value_total}\n")                                                    
        case ["2"]:
            print("\nПрограмма закрыта")
            break