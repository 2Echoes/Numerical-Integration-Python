from MethodeTrapezes import int_trapez

#Pas ok mais methode nulle

def int_Romberg(f,min,max,delta) :
    #delta est l'erreur maximale acceptée
    count=0
    P_numb = 10
    error = 1E36
    Romb_list = [int_trapez(f,min,max,P_numb)]
    while error > delta: 
        P_numb *=2
        step = (max-min)/P_numb
        new_Romb = Romb_list[count]/2*2*step
        for i in range(1,P_numb,2):
            xk = min + step*i
            new_Romb += f(xk)
        new_Romb *=step
        Old_list = Romb_list
        Romb_list +=[0.0]
        Romb_list[0] = new_Romb