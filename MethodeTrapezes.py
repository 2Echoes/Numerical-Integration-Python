""" Dans la suite, f est la fonction à int
a et b les bornes respectivement inférieures et supérieures de l'intégrale
N est le nombre de pts d'intégration
delta l'erreur maximale acceptée """

def int_trapez(f,a,b,N):
    h=(b-a)/N
    res = (1/2)*(f(a)+f(b))
    for i in range(1,N):
        xk=a+i*h
        res+=f(xk)
    return h*res


def int_trapez_adapt(f,a,b,delta):
    N=1000
    error=1.0E38 #initialisée à la VMax de Python
    I1=int_trapez(f,a,b,N)
    while error>delta:
        N*=2
        h=(b-a)/N
        I2 = I1/(2*2*h)
        for i in range(1,N,2):
            xk=a+i*h
            I2+=f(xk)
        I2*=h   
        error = abs((1/3)*(I2-I1))
        print(error)
        I1=I2
    return I2