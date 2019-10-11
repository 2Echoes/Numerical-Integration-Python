def Meth_Simpson(f,a,b,N): #f la fonction à intégrer, a la borne inf, b la borne sup et N le nb de pts d'integration
    h = (b-a)/N
    res = f(a)+f(b)
    for i in range(1,N,2):
        xk=a+i*h
        res+= f(xk-h)+4*f(xk)+f(xk+h)
    res*=h/3
    return res

def error_Simpson(f,a,b,N): # Renvoie l'erreur commise pour la Meth_Simpson avec N points, f la fction, a et b les bornes inf et sup
    return (1/15)*(Meth_Simpson(f,a,b,N)-Meth_Simpson(f,a,b,int(N/2))) #préférable d'avoir N pair

def Meth_Simpson_adapt(f,a,b,delta): #Intégration avec la méthode de Simpson où delta est la marge d'erreur maximale
    N=1000
    error=1.0E38 # Initialisation à l'infini
    I1 = Meth_Simpson(f,a,b,N)
    while error>delta:
        N*=2
        h=(b-a)/N
        I2=(I1/2)*(3/h)
        for i in range(1,N,2):
            I2+=f(a+i*h)
        I2*=h/3
        error=abs((1/15)*(I2-I1))
        print(error)
        I1=I2
    return I2

from math import sin,pi
def g(c):
    return c**2*sin(c)

print(Meth_Simpson(g,0,pi,1000),'\n',pi**2-4)