import numpy as np 

pie=[1,0,2,3,5,4,6,7]
H=[6,5,2,7,4,1,3,0]

class algo:

    def algo_generation_k(K, H):
        l = len(K)
        if l%2 == 0:
            K = K
        else:
            K = '0' + K
        K=list(K)
        H = H
        b = []
        combinaison = zip(H, K)
        tri = sorted(combinaison, key=lambda x: x[0])
        b = [item for _, item in tri]
        moy = len(b) // 2
        K11 = b[:moy]
        K22 = b[moy:]
        K1 =[x or y for x, y in zip(K11, K22)]
        K2 = [x or y for x, y in zip(K22, K11)]

        return K11, K22, K1, K2
        

    def configuration_cle(N, pie):
        t=len(N)
        if t%2 == 0:
            N = N
        else:
            N = '0' + N
        N=list(N)
        pie=pie
        a = []
        combinaison = zip(pie, N)
        tri = sorted(combinaison, key=lambda x: x[0])
        a = [item for _, item in tri]
        
        mid = len(a) // 2
        G0 = a[:mid]
        D0 = a[mid:]
        return G0, D0

        

    print(algo_generation_k("01101101", H))
    #print(configuration_cle("1111110", pie))
