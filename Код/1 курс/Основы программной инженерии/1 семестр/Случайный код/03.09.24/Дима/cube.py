mass = []


def f(n):
    global mass
    for i in range(1, abs(n)+1):
        if n%i == 0:
            mass.append(n/i)
            mass.append(-1*(n/i))
            mass.sort()


a = 5
b = -1
c = -20
d = 4
x1 = 0
a1 = 0
b1 = 0
c1 = 0
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