from QuadratureGauss import quadratureGauss
import numpy as np

#PARAMETRES
kb = 1.38E-23 #JK-1 cte de Boltzmann
#Système Bloc aluminium
vol =1.0E-5 # m3 le volume
densnum = 6.022E28 #m-3 la densité numérique
Debyetemp = 428# K la température de Debye du matéria
nodenumber = 50

def thm_capacity_interger(x):
    return (x**4*np.exp(x))/(np.exp(x)-1)**2

def thm_capacity(T):
    integer = quadratureGauss(thm_capacity_interger,0,Debyetemp/T,nodenumber)
    return 9*densnum*vol*kb*(T/Debyetemp)**3*integer



T = np.linspace(5,500,100)
Cv = []
for i in T :
    Cv += [thm_capacity(i)]


import matplotlib.pyplot as plt
plt.figure()
plt.plot(T,Cv,'k')
plt.xlabel('Température(K)')
plt.ylabel('Cv(J.K-1)')
plt.show()

