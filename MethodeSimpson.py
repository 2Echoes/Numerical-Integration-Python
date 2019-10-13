def Meth_Simpson(fonction,borne_min,borne_max,nb_intpoints):
    #f la fonction à intégrer, a la borne inf, b la borne sup et N le nb de pts d'integration
    step = (borne_max-borne_min)/nb_intpoints
    res = fonction(borne_min)+fonction(borne_max)
    for i in range(1,nb_intpoints,2):
        curr_point=borne_min+i*step
        res+= fonction(curr_point-step)+4*fonction(curr_point)+fonction(curr_point+step)
    res*=step/3
    return res

def Simpson_iteration(fonction,borne_min,borne_max,int_point):
    #Calcul la valeur de l'integral par la methode de Simpson pour un nbre de points = int_point, equivalent à Meth_Simpson sur le resultat
    Int = fonction(borne_min) + fonction(borne_max)
    step = (borne_max-borne_min)/int_point
    correction = 0
    for i in range(1,int_point,2):
        curr_point = borne_min+i*step
        Int +=2*fonction(curr_point+step)
        correction += fonction(curr_point)
    Int*=1/3
    correction*=2/3
    compvalue= step*(Int+2*correction)
    return compvalue


def Meth_Simpson_adapt(fonction,borne_min,borne_max,delta): 
    #Intégration avec la méthode de Simpson où delta est la marge d'erreur maximale
    int_point=1000
    error=1.0E38 # Initialisation à l'infini
    step=(borne_max-borne_min)/int_point
    compvalue1 = Simpson_iteration(fonction,borne_min,borne_max,int_point)
    while error>delta:
        int_point*=2
        step/=2
        compvalue2 = Simpson_iteration(fonction,borne_min,borne_max,int_point)
        error=abs((1/15)*(compvalue2-compvalue1))
        compvalue1=compvalue2
    return compvalue2