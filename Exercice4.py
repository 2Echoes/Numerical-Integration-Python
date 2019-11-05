import numpy as np

def derivee_centrale(f,x,step=10E-5):
    res = (f(x+step/2)-f(x-step/2))/step
    return res

def f(x):
        return 1+1/2*np.tanh(2*x)

def f2(x):
    return 1/(np.cosh(2*x))**2

X = np.linspace(-2,2,500)
Y = f(X)
Y2 = f2(X)
Y21 = derivee_centrale(f,X,10E-5)
Y22 = derivee_centrale(f,X,10E-6)
Y23 = derivee_centrale(f,X,10E-4)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(X,Y,'k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 1+0.5tanh(2x)')

plt.figure()
plt.subplot(121)
plt.plot(X,Y2,'r',label='Derivée analytique')
plt.plot(X,Y21,'k',label='Derivée centrale')
plt.xlabel('x')
plt.ylabel('y')
plt.title("y=(1+0.5tanh(2x))'")
plt.legend()
plt.subplot(122)
plt.plot(X,Y2-Y21,'b')
plt.plot(X,Y2-Y22,'r')
plt.plot(X,Y2-Y23,'g')

plt.show()