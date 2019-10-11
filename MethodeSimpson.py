import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi

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

def g(x):
    return x**2*sin(x)

""" N=1000
res=Meth_Simpson(g,0,pi,N)
print('I2 = ',res)    #il faut trouver 5.86
print('I = ',pi**2-4)
print('erreur estimée ',error_Simpson(g,0,pi,N))
print('erreur réelle ', pi**2-4-res) """

""" X=[]
estim=[]
reelle=[]

for n in range(100,101,1):
    X+=[n]
    res=Meth_Simpson(g,0,pi,n)
    estim+=[error_Simpson(g,0,pi,n)]
    reelle+=[pi**2-4-res]

plt.figure('figsize=(8,8)')
# erreur_estimee=plt.plot(X,estim,'--g')
# plt.legend('erreur estimée')
erreur_reelle=plt.plot(X,reelle,'--r')
plt.legend('erreur reelle')
plt.xlabel("Nombre de points d'intégration (N)")
plt.ylabel("Erreur")
plt.title('Intégrale x²sin(x) de 0 à pi')
plt.show() """