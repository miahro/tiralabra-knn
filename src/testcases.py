"""
Tässä tiedostossa etukäteen määriteltyjä testitapauksia
vastaavat tapaukset laskettu manuaalisesti testin vertailukohdaksi
"""
import numpy as np

#snumpy.array suunnattujen Hausdorffin etäisyyksien laskentaa varten
A=np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [1,1],
        [0, 2],
        [2,0],
        [1,2],
        [2,1],
        [2,2],
        [0,3],
        [3,0],
        [3,1],
        [1,3],
        [3,2],
        [2,3],
        [3,3],
        [4,0],
        [0,4],
        [4,1],
        [1,4],
        [4,2],
        [2,4],
        [4,3],
        [3,4],
        [4,4]
    ])

#snumpy.array suunnattujen Hausdorffin etäisyyksien laskentaa varten
B=np.array([
        [27,27],
        [27,26],
        [26,27],
        [26,26],
        [27,25],
        [25,27],
        [26,25],
        [25,26],
        [25,25],
        [27,24],
        [24,27],
        [26,24],
        [24,26],
        [25,24],
        [24,25],
        [24,24]
    ])

A2=np.array([
        [4,4]
    ])

C2=np.array([
        [6,6],
    ])


C=np.array([
        [6,6],
        [27,26],
        [26,27],
        [26,26],
        [27,25],
        [25,27],
        [26,25],
        [25,26],
        [25,25],
        [27,24],
        [24,27],
        [26,24],
        [24,26],
        [25,24],
        [24,25],
        [24,24]
    ])


Am = np.full((28,28), False)
for a in A:
    Am[a[0]][a[1]]=True


Bm = np.full((28,28), False)
for b in B:
    Bm[b[0]][b[1]]=True

Cm = np.full((28,28), False)
for c in C:
    Cm[c[0]][c[1]]=True


A2m = np.full((28,28), False)
for a in A2:
    A2m[a[0]][a[1]]=True

C2m = np.full((28,28), False)
for c in C2:
    C2m[c[0]][c[1]]=True
