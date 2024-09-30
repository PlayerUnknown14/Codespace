from prettytable import *
table = PrettyTable()
table.field_names = ['Mark', 'Model', 'Colour', 'HP']
print(table)
r1 = ''
r2 = ''
r3 = ''
r4 = ''

a = ["".join(i) for i in open(r'C:\Users\luvid\OneDrive\Desktop\python\random\Работа над гаражом\garage.txt')]
print(a)
def dobavl():
    r1 = input('Введите марку:')
    r2 = input('Введите модель:')
    r3 = input('Введите цвет:')
    r4 = input('Введите лошадиные силы:')
    return r1,r2,r3,r4

def clear():
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    return r1,r2,r3,r4


r1,r2,r3,r4 = dobavl()

table.add_row([r1,r2,r3,r4])

print(table)
print('Значения до чистки',r1,r2,r3,r4)
r1,r2,r3,r4 = clear()
print('Значения после чистки',r1,r2,r3,r4)