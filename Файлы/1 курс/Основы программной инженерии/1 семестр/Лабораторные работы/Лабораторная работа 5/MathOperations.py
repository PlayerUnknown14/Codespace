import time
from random import randint


mass = []
start_time = time.time()
for i in range(10_000_000):
    i = randint(1, 1252100)
    mass.append(i)
    end_time = time.time()
    execution_time = end_time - start_time
print(f'Сумма массива: {sum(mass)}')
print(f"Время выполнения программы: {execution_time} секунд")

