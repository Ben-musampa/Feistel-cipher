""" Ce script est une implémentation de l'algorithme de feistel
Dans le cadre du cours de : TRANSMISSION DES DONNEES ET SECURITE INFORMATIQUE
Par : MUSAMPA KAMBAJA Ben
ce script est sans librairie externe et peut donc s'éxecuter sans installation préalable d'autres librairies
"""
#pie
pie=[4,6,0,2,7,3,1,1]
#pie exposant -1
pie_1 = [2,6,3,5,0,7,1,4]
#permutation
H=[4,6,0,2,7,3,1,5]
#P
P = [2,0,1,3]
#moitié
mi = len(H)//2

def ou(a,b): #implementation de la fonction ou
    temp=""
    for i in range(mi):
        if(a[i]=='1' or b[i]=='1'):
            temp += '1'
        else:
            temp += '0'

    return temp
def ouexlusif(a,b): #implementation de la fonction et ouexcusif X0R
	temp = ""
	for i in range(mi):
		if (a[i] == b[i]):
			temp += "0"	
		else:
			temp += "1"	
	return temp

def et(a,b): #implementation de la fonction et logique
    temp =""
    for i in range(mi):
        if (a[i] == "1" and b[i]== "1"):
            temp +="1"
        else:
             temp +="0"
    return temp

def permutation(a, b): #implementation de la fonction de permutation
    c = [0]*len(b)
    for i in range(len(a)):
        j = a[i]
        c[i]=b[a[i]]
        
    return c

def algo_generation_k(a, bb): #implementation de la fonction de l'algo de génération de clé
    l = len(a)
    if l%2 == 0:
        a = a
    else:
        a = '0' + a

    a=list(a)
    b = permutation(bb, a)
    b = list(b)
    moy = len(b) // 2
    K11 = b[:moy]
    K22 = b[moy:]
    #print (b)
    #print (K11, K22)
    K1 = ouexlusif(K11, K22)
    K1 = list(K1)

    K2 = et(K22, K11)
    K2 = list(K2)

    return K1, K2


def configuration_cle(aa, bb): #implementation de la fonction de l'agorithme de configuration de clé
    t=len(aa)
    if t%2 == 0:
        aa = aa
    else:
        aa = '0' + aa
    aa=list(aa)
    bb=bb
    a = []
    a = permutation(bb, aa)
    mid = len(a) // 2
    G0 = a[:mid]
    D0 = a[mid:]
    return G0, D0

def main(): #implementation de la fonction principale

    a=input(print('les 8 bits à crypté'))
    k1, k2 = (algo_generation_k(a, H))

    b=input(print('entrée le message N de taile 8 '))
    g0, d0 =  configuration_cle(b, pie)

    g0=list(g0)
    d0=list(d0)
    #print(g0, d0)
    # 1er round 
    pd1 = []
    pd1 = permutation(P, g0)

    d1 = ouexlusif(pd1,k1)
    gr = ou(g0, k1)

    g1 = ouexlusif(d0, gr)

    #2em round 
    pd2 = []
    pd2 = permutation(P, g1)

    d2 = ouexlusif(pd2, k2)

    g2r = ou(g1, k2)
    g2 = ouexlusif(d1, g2r)

    c = g2 + d2
    c= list(c)

    resultat = []
    resultat = permutation(pie_1, c)

    print(resultat)


if __name__ == "__main__":
     main()
