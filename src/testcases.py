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
