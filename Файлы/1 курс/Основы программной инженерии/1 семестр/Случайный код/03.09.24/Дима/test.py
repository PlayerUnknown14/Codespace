def check():
    while True:
        try:
            print("Введите коэффиценты")
            a, b, c, d = map(float, input().split())
            break
        except ValueError:
            print("Коэффиценты введены неверно")
    return a, b, c, d

a, b, c, d = check()

def sign(x):  
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
        
def dicho(f,a,b,eps=1.0e-14):    
    fa=f(a)                    
    fb=f(b)
    while True:
        c=0.5*(a+b)
        if abs(b-a)<eps:
            return c
        fc=f(c)
        if abs(fc)<=eps:
            return c
        if sign(fa)*sign(fc)<0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc
            
def div_poly(p,a):  
    r=[0,0,0]          
    r[2]=p[3]
    r[1]=p[2]+a*p[3]
    r[0]=(p[1]+a*(p[2]+a*p[3]))
    return tuple(r)
    
def solve_qube(p):  
    q=max(p)
    left=-abs(q)/abs(p[3])  
    right=-left
    x1=dicho(lambda x: p[3]*x**3+p[2]*x**2+p[1]*x+p[0],left,right)
    (c,b,a)=div_poly(p,x1)
    d=b**2-4*a*c
    x2=(-b+d**0.5)/(2*a)
    x3=(-b-d**0.5)/(2*a)
    return (x1,x2,x3)
    
print(solve_qube([a,b,c,d]))