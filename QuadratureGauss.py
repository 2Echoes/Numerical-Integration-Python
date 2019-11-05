from gaussxw import gaussxw #Permet de calculer les noeuds de la quadrature de Gauss sur l'intervalle [-1,1]

def quadratureGauss_setter(min,max,Nodenumber):
    pos,weight = gaussxw(Nodenumber)
    newpos = 0.5*(max-min)*pos +0.5*(max + min)
    newweight = 0.5*(max-min)*weight
    return newpos,newweight

def quadratureGauss(f,min,max,Nodenumber):
    nodes,weight = quadratureGauss_setter(min,max,Nodenumber)
    res = 0
    for nod,wei in zip(nodes,weight):
        res += wei*f(nod)
    return res

