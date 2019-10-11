def Meth_Simpson(fonction,borne_min,borne_max,nb_intpoints):
    #f la fonction à intégrer, a la borne inf, b la borne sup et N le nb de pts d'integration
    step = (borne_max-borne_min)/nb_intpoints
    res = fonction(borne_min)+fonction(borne_max)
    for i in range(1,nb_intpoints,2):
        curr_point=borne_min+i*step
        res+= fonction(curr_point-step)+4*fonction(curr_point)+fonction(curr_point+step)
    res*=step/3
    return res

def error_Simpson(f,a,b,N): 
    # Renvoie l'erreur commise pour la Meth_Simpson avec N points, f la fction, a et b les bornes inf et sup
    return (1/15)*(Meth_Simpson(f,a,b,N)-Meth_Simpson(f,a,b,int(N/2))) #préférable d'avoir N pair

def Meth_Simpson_adapt(f,a,b,delta): 
    #Intégration avec la méthode de Simpson où delta est la marge d'erreur maximale
    N=1000
    error=1.0E38 # Initialisation à l'infini
    I1 = Meth_Simpson(f,a,b,N)
    while error>delta:
        N*=2
        h=(b-a)/N
        I2=(I1/2)*3/(2*h)
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

print(Meth_Simpson_adapt(g,0,pi,1.0E-6),'\n',pi**2-4)