mass = []


def f(n):
    global mass
    for i in range(1, abs(n)+1):
        if n%i == 0:
            mass.append(n/i)
            mass.append(-(n/i))
            mass.sort()


a = 1
b = -4
c = 5
d = -2
x1 = 0
a1 = 0
b1 = 0
c1 = 0
x2 = "x2 отсутствует"
x3 = "x3 отсутствует"
f(d)
print(mass)
for numb in mass:
    a_after = a
    b_after = numb*a+b
    c_after = b_after*numb+c
    if (((numb*a+b)*numb+c)*numb+d) == 0:
        x1 = numb
        a1 = a_after
        b1 = b_after
        c1 = c_after
print(x1)
d = b1+4*a1*c1
print(d)
if d<0:
    print('Дискриминант квадратного уравнения меньше нуля. Единственный корень уравнения: ',x1)
else:
    x2 = -b-d**0.5
    x3 = -b+d**0.5
print('Корни кубического уравнения:',x1,x2,x3)