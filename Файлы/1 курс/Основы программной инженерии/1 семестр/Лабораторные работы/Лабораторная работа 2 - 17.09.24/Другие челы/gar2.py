def search(b):
    f=open('garage.txt','r+')
    x=f.read()
    f.close()
    j=0
    m=0
    while b == 'нет':
        c=0
        while c == 0:
            stop=''
            v1=')'
            v2=')'
            v3=')'
            v4=')'
            v5=')'
            while stop != 'стоп':
                v=input('введите параметры до 6 штук по ним будет выведем список машин удовлетворяющих этим параметрам\n')
                stop=input('Напишите <стоп> если парметров достаточно\n')
                if v1 == ')':
                    v1=v
                elif v2 == ')':
                    v2=v
                elif v3 == ')':
                    v3=v
                elif v4 == ')':
                    v4=v
                elif v5 == ')':
                    v5=v 
            k=0
            n=0
            for i in range(0,len(x)):
                if x[i]==':' and x[i+1] == '!':
                    k=k+1
            for i in range(0,k):
                n=n+1
                num=n
                num1=n+1
                num=str(num)+':'
                num1=str(num1)+':'
                for i in range (1, len(x)):
                    if x[i:i+2] == num:
                        j=i
                    if x[i:i+2] == num1 or i == len(x)-1:
                        m=i-1
                        break
                if v in x[j:m] and v1 in x[j:m] and v2 in x[j:m] and v3 in x[j:m] and v4 in x[j:m] and v5 in x[j:m]:
                    print(x[j:m])
                    c=1
            if c == 0:
                print('Машины с такими парметрами нет')
        b1=input('В данном списке есть нужная машина (да или нет)\n')
        if b1 == 'да' or b1 == 'Да':
            b = 'да'
def izm(m,j,par1,s,num,count,n,v,b):
    for i in range (0, len(s)):
        v=v+[s[i]]
    v[m:j] = par1
    if int(num)!=count:
        num1=int(num)+1
        for i in range(0,len(n)): 
            if n[i]==str(num) and n[i+1] == ':':
                t=i+1
            if n[i]==str(num1) and n[i+1] == ':':
                y=i
        i=len(v)
        n[t:y] = v[1:i]
    if int(num) == count:
        for i in range(0,len(n)):
            if n[i]==str(num) and n[i+1] == ':':
                t=i+1
        i1=len(v)
        i2=len(n)
        n[t:i2]=v[1:i1]
    for i in range(0, len(n)):
        b=b+n[i]
    print('машина успешно изменена\n',b)
    f=open('garage.txt','r+')
    f.write(b)
    f.close()
while True:
    d=input('1.Добавить машину\n2.Удалить машину\n3.Изменить машину\n4.Вывести список машин\n5.Выйти из проги\nВведите номер действия:\n')
    if d != '1' and d!='2' and d!='3' and d!='4' and d!='5':
        print('такого действия нет')
    if d == '1' or d=='2' or d=='3' or d=='4' or d=='5':
        d=int(d)    
        if d == 1:
            v=''
            for i in range (0, 99):
                i=str(i)
                v=v+i
            k=0
            s=''
            car=input('Марка:\n')
            door=input('Модель:\n')
            light=input('Тонировка числовое среднее значение(без процентов):\n')
            while light not in v:
                if light in v:
                    break
                light=input('!!!Показатель тонировки  должен быть больше или равен 0 и не больше 100\n')
            light = light + '%'
            color=input('Цвет:\n')
            reg=input('Регистрационный номер:\n')
            f=open('garage.txt','r+')
            s=f.read()
            if reg in s:
                k=1
                print('Машина с таким номером уже есть')
                break
            if k==0:
                engine=input('Тип двигателя (Гибридный, электро, внутреннего сгорания):\n')
                if engine != 'Гибридный' or engine != 'Электро' or engine != 'Внутреннего сгорания' or engine != 'гибридный' or engine != 'электро' or engine != 'внутреннего сгорания':
                    while engine != 'Гибридный' or engine != 'Электро' or engine != 'Внутреннего сгорания' or engine != 'гибридный' or engine != 'электро' or engine != 'внутреннего сгорания':
                        if engine == 'Гибридный' or engine == 'Электро' or engine == 'Внутреннего сгорания' or engine == 'гибридный' or engine == 'электро' or engine == 'внутреннего сгорания':
                            break
                        engine=input('!!!Тип двигателя должен удовлетворять предложеному списку (Гибридный, электро, внутреннего сгорания):\n')
                c=1
                c=str(c)
                for i in range(0,len(s)):
                    if s[i] == c and s[i+1]==':':
                        c=int(c)
                        c=c+1
                        c=str(c)
                c=str(c)
                s =c+':!'+'\n'+'1)Номер:'+'\n'+reg+'\n'+'2)Марка:'+'\n'+car+'\n'+ '3)Модель:'+'\n'+door+'\n'+'4)Тонировка:'+'\n'+light+'\n'+'5)Цвет:'+'\n'+color+'\n'+'6)Тип двигателя:'+'\n'+engine+'\n'
                f.write(s)
                f.close()
                print(s) 
        if d == 2:
            f=open('garage.txt','r+')
            x = f.read()
            f.close()
            if len(x) == 0:
                print('Гараж пустой, нужно сачала добавить машину')
            if len(x)!= 0:
                d1 = input('Точно хотите удалить машину (да или нет)\n')
                if d1 == 'да' or d1 == 'Да':
                    f=open('garage.txt','r+')
                    print(f.read(),'\n')
                    f.close()
                    b=input('Нашли в этои списке нужную машину(да или нет)\n')
                    if b == 'нет' or b == 'Нет':
                        search(b)
                        b='да'
                    if b == 'да' or b == 'Да':
                        x=''
                        s=''
                        z=''
                        v=[]
                        b=''
                        count = 0
                        f=open('garage.txt','r+')
                        print(f.read(),'\n')
                        f.close()
                        num=input('Введите номер машины которую нужно удалить\n')
                        f=open('garage.txt','r+')
                        x = f.read()
                        for i in range (0, len(x)):
                            if x[i] == '\n':
                                count = count+1
                        count = count/13
                        count = int(count)
                        f.close()
                        if int(num)>count or int(num)<=0:
                            while int(num)>count or int(num)<=0:
                                print('Такой машины нет')
                                num=input('Введите номер машины которую нужно удалить\n')
                        if int(num) <= count and int(num) > 0:
                            if int(num) != count:
                                for i in range (0, len(x)):
                                    num1=int(num)+1
                                    num1=str(num1)
                                    if x[i] == num and x[i+1] == ':':
                                        j=i
                                    if x[i] == num1 and x[i+1]==':':
                                        m=i
                                if num != 1:        
                                    for i1 in range (0,j):
                                        s=s+x[i1]
                                    for i1 in range (m, len(x)):
                                        s=s+x[i1]
                                if num == 1:
                                    for i1 in range (j, len(x)):
                                        s=s+x[i1]
                                for i in range (0, len(s)):
                                    v=v+[s[i]]
                                for i in range(int(num), count):
                                    for i1 in range(0, len(v)):
                                        i2 = i+1
                                        i2 = str(i2)
                                        if v[i1] == i2:
                                            v[i1] = str(i)
                                for i in range(0, len(v)):
                                    b=b+v[i]
                                print('Машина успешно удалена\n',b)
                                f=open('garage.txt','w')
                                f.write(b)
                                f.close()
                            if int(num) == count:
                                for i in range (0, len(x)):
                                    if x[i] == num and x[i+1] == ':':
                                        j=i    
                                for i1 in range (0, j):
                                    s=s+x[i1]
                                print('Машина успешно удалена\n',s)
                                f=open('garage.txt','w')
                                f.write(s)
                                f.close()
        if d == 3:
            f=open('garage.txt','r+')
            x = f.read()
            f.close()
            if len(x) == 0:
                print('Гараж пустой, нужно сачала добавить машину')
            if len(x)!= 0:
                f=open('garage.txt','r+')
                print(f.read(),'\n')
                f.close()
                b=input('Нашли в этои списке нужную машину(да или нет)\n')
                if b == 'нет' or b == 'Нет':
                   search(b)
                   b='да'
                if b == 'да' or b == 'Да':
                    k=0
                    x=''
                    s=''
                    count=0
                    v=[]
                    b=''
                    n=[]
                    f=open('garage.txt','r+')
                    print(f.read(),'\n')
                    f.close()
                    num=input('Введите номер машины которую нужно изменить\n')
                    f=open('garage.txt','r+')
                    x = f.read()  
                    for i in range (0,len(x)):
                        n=n+[x[i]]
                    for i in range (0, len(x)):
                        if x[i] == '\n':
                            count = count+1
                    count = count/13
                    count = int(count)
                    f.close()
                    if int(num) != count:
                        for i in range (0, len(x)):
                            num1=int(num)+1
                            num1=str(num1)
                            if x[i] == num and x[i+1] == ':':
                                j=i
                            if x[i] == num1  and x[i+1] == ':':
                                m=i
                        if num != 1:        
                            for i1 in range (j,m):
                                s=s+x[i1]
                        if num == 1:
                            for i1 in range (0, j):
                                s=s+x[i1]
                    if int(num) == count:
                        for i in range (0, len(x)):
                            if x[i] == num and x[i+1] == ':':
                                j=i
                        for i1 in range (j, len(x)):
                            s=s+x[i1]
                    print(s)
                    par=input('Введите параметр который нужно изменить\n')
                    if par == 'Номер' or par == 'номер' or par == '1':
                        for i in range (0, len(s)):
                            if s[i] == '1' and s[i+1] == ')':
                                m = i+9
                            if s[i] == '2' and s[i+1] == ')':
                                j = i-1
                        z = s[m:j]
                        print(z,'\n')
                        par1=input('введите на какой номер заменить\n')
                        for i in range(0,len(x)):
                            t=i+len(par1)
                            if x[i:t] == par1:
                                k=k+1
                                print('Машина с таким номером уже есть')
                                break
                        if k==0:
                            izm(m,j,par1,s,num,count,n,v,b)
                    if par == 'Марка' or par == 'марка' or par == '2':
                        for i in range (0, len(s)):
                            if s[i] == '2' and s[i+1] == ')':
                                m = i+9
                            if s[i] == '3' and s[i+1] == ')':
                                j = i-1
                        z = s[m:j]
                        print(z,'\n')
                        par1=input('введите на какую марку заменить\n')
                        izm(m,j,par1,s,num,count,n,v,b)
                    if par == 'Модель' or par == 'модель' or par == '3':
                        for i in range (0, len(s)):
                            if s[i] == '3' and s[i+1] == ')':
                                m = i+10
                            if s[i] == '4' and s[i+1] == ')':
                                j = i-1
                        z = s[m:j]
                        print(z,'\n')
                        par1=input('введите на какую модель заменить\n')
                        izm(m,j,par1,s,num,count,n,v,b)
                    if par == 'Тонировка' or par == 'тонировка' or par == '4':
                        for i in range (0, len(s)):
                            if s[i] == '4' and s[i+1] == ')':
                                m = i+13
                            if s[i] == '5' and s[i+1] == ')':
                                j = i-1
                        z = s[m:j]
                        print(z,'\n')
                        par1=input('введите новое значение тонировки числовое значение\n')
                        if par1 not in range(0, 100):
                            while par1 not in range(0, 100):
                                if int(par1) in range(0, 100):
                                    break
                                par1=input('!!!Показатель тонировки  должен быть больше или равен 0 и не больше 100\n')
                        par1= par1+'%'
                        izm(m,j,par1,s,num,count,n,v,b)                    
                    if par == 'Цвет' or par == 'цвет' or par == '5':
                        for i in range (0, len(s)):
                            if s[i] == '5' and s[i+1] == ')':
                                m = i+8
                            if s[i] == '6' and s[i+1] == ')':
                                j = i-1
                        z = s[m:j]
                        print(z,'\n')
                        par1=input('введите новый цвет\n')
                        izm(m,j,par1,s,num,count,n,v,b)
                    if par == 'Тип двигателя' or par == 'двигатель' or par == 'тип' or par == '6':
                        for i in range (0, len(s)):
                            if s[i] == '6' and s[i+1] == ')':
                                m = i+17
                            j=len(s)
                        z = s[m:j]
                        print(z,'\n')
                        par1=input('введите на какой тип двигателя\n')
                        if par1 != 'Гибридный' or par1 != 'Электро' or par1 != 'Внутреннего сгорания' or par1 != 'гибридный' or par1 != 'электро' or par1 != 'внутреннего сгорания':
                            while par1 != 'Гибридный' or par1 != 'Электро' or par1 != 'Внутреннего сгорания' or par1 != 'гибридный' or par1 != 'электро' or par1 != 'внутреннего сгорания':
                                if par1 == 'Гибридный' or par1 == 'Электро' or par1 == 'Внутреннего сгорания' or par1 == 'гибридный' or par1 == 'электро' or par1 == 'внутреннего сгорания':
                                    break
                                par1=input('!!!Тип двигателя должен удовлетворять предложеному списку (Гибридный, электро, внутреннего сгорания):\n')
                        izm(m,j,par1,s,num,count,n,v,b)
                    else:
                        print('Такого параметра нет')
        if d == 4:
            s=''
            k=0
            f=open('garage.txt','r+')
            x = f.read()
            f.close()
            if len(x) == 0:
                print('Гараж пустой, нужно сачала добавить машину')
            if len(x)!= 0:
                print('1.Вывести весь список машин\n2.Вывести машины по одному параметру\n')
                b2=input('Введите номер действия\n')
                if b2 != '1' and b2 != '2':
                    print('Такого действия нет')
                if b2 == '1' or b2 == '2':
                    if b2 == '1':
                        f = open('garage.txt','r+')
                        print(f.read())
                        f.close()
                    if b2 =='2':
                        b='нет'
                        search(b)                
        if d == 5:
            print('Вы вышли')
            break
