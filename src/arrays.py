""" neliölliset etäisyysmatriisit sekä pistelistat Hausdorff laskentafunktion 'kerrosten' 
mukaan laskettu valmiiksi tämän. Tämä on luultavasti tarpeetonta, mutta tälle varmistettu, 
ettei tule vahingossa toistuvia funktiokutsuja """

SDM1 = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]

PL1 = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

SDM2 = [[8, 5, 4, 5, 8], 
       [5, 2, 1, 2, 5], 
       [4, 1, 0, 1, 4], 
       [5, 2, 1, 2, 5], 
       [8, 5, 4, 5, 8]]

PL2 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1), (0, 2), 
       (0, -2), (2, 0), (-2, 0),(-1, 2), (2, 1), (-1, -2), (1, -2), (-2, 1), (-2, -1),
       (1, 2), (2, -1), (-2, -2), (-2, 2), (2, -2), (2, 2)]

SDM3 = [[18, 13, 10, 9, 10, 13, 18], 
       [13, 8, 5, 4, 5, 8, 13], 
       [10, 5, 2, 1, 2, 5, 10], 
       [9, 4, 1, 0, 1, 4, 9], 
       [10, 5, 2, 1, 2, 5, 10], 
       [13, 8, 5, 4, 5, 8, 13], 
       [18, 13, 10, 9, 10, 13, 18]]

PL3 = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), 
       (0, 2), (0, -2), (-2, 0), (-2, 1), (-1, -2), (-2, -1), (-1, 2), (2, 1), 
       (1, -2), (2, -1), (1, 2), (-2, 2), (2, 2), (-2, -2), (2, -2), (0, 3), (0, -3), 
       (3, 0), (-3, 0), (1, 3), (-3, -1), (1, -3), (3, 1), (-1, 3), (-1, -3), 
       (-3, 1), (3, -1), (-3, 2), (3, 2), (2, -3), (-2, -3), (3, -2), (-3, -2), 
       (2, 3), (-2, 3), (-3, -3), (-3, 3), (3, -3), (3, 3)]

SDM4 = [[32, 25, 20, 17, 16, 17, 20, 25, 32], 
       [25, 18, 13, 10, 9, 10, 13, 18, 25], 
       [20, 13, 8, 5, 4, 5, 8, 13, 20], 
       [17, 10, 5, 2, 1, 2, 5, 10, 17], 
       [16, 9, 4, 1, 0, 1, 4, 9, 16], 
       [17, 10, 5, 2, 1, 2, 5, 10, 17], 
       [20, 13, 8, 5, 4, 5, 8, 13, 20], 
       [25, 18, 13, 10, 9, 10, 13, 18, 25], 
       [32, 25, 20, 17, 16, 17, 20, 25, 32]]

PL4 = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0),
       (0, 2), (-2, 0), (0, -2), (-1, -2), (1, -2), (1, 2), (2, -1), (-2, -1), (-1, 2), 
       (-2, 1), (2, 1), (2, -2), (-2, -2), (-2, 2), (2, 2), (0, 3), (0, -3), (-3, 0), 
       (3, 0), (-3, 1), (1, 3), (3, 1), (-1, 3), (-1, -3), (3, -1), (-3, -1), (1, -3), 
       (-2, 3), (-2, -3), (3, -2), (2, -3), (2, 3), (3, 2), (-3, 2), (-3, -2), (-4, 0), 
       (0, 4), (4, 0), (0, -4), (4, 1), (-1, -4), (1, -4), (-1, 4), (4, -1), (-4, 1), 
       (1, 4), (-4, -1), (-3, -3), (3, 3), (-3, 3), (3, -3), (4, -2), (-4, 2), (-2, -4), 
       (2, -4), (-2, 4), (2, 4), (-4, -2), (4, 2), (-4, 3), (-3, 4), (-3, -4), (3, 4), 
       (4, -3), (-4, -3), (3, -4), (4, 3), (-4, -4), (-4, 4), (4, -4), (4, 4)]

SDM5 = [[50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50], 
       [41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41], 
       [34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34], 
       [29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29], 
       [26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26], 
       [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25], 
       [26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26], 
       [29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29], 
       [34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34], 
       [41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41], 
       [50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50]]

PL5 = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), 
       (0, 2), (-2, 0), (0, -2), (1, 2), (-2, -1), (-1, -2), (-2, 1), (2, 1), (2, -1),
       (-1, 2), (1, -2), (2, -2), (-2, 2), (-2, -2), (2, 2), (0, -3), (-3, 0), (3, 0), 
       (0, 3), (3, -1), (1, 3), (-1, -3), (3, 1), (-3, 1), (-3, -1), (1, -3), (-1, 3), 
       (3, -2), (-2, -3), (-3, -2), (2, 3), (2, -3), (-2, 3), (3, 2), (-3, 2), (0, -4), 
       (0, 4), (4, 0), (-4, 0), (1, 4), (-4, -1), (1, -4), (-4, 1), (-1, 4), (4, 1), 
       (-1, -4), (4, -1), (3, 3), (3, -3), (-3, 3), (-3, -3), (2, 4), (4, 2), (-4, 2), 
       (4, -2), (2, -4), (-4, -2), (-2, -4), (-2, 4), (3, -4), (4, 3), (4, -3), (3, 4), 
       (-4, -3), (0, -5), (-3, 4), (5, 0), (-3, -4), (0, 5), (-4, 3), (-5, 0), (5, 1), 
       (-5, 1), (-1, -5), (1, -5), (5, -1), (1, 5), (-5, -1), (-1, 5), (5, -2), (-2, -5), 
       (5, 2), (-5, -2), (-2, 5), (2, -5), (-5, 2), (2, 5), (-4, -4), (4, 4), (-4, 4), 
       (4, -4), (5, -3), (5, 3), (3, 5), (3, -5), (-5, -3), (-5, 3), (-3, 5), (-3, -5), 
       (4, -5), (-5, 4), (-4, 5), (5, 4), (4, 5), (-5, -4), (5, -4), (-4, -5), (-5, -5), 
       (-5, 5), (5, -5), (5, 5)]

SDM6 = [[72, 61, 52, 45, 40, 37, 36, 37, 40, 45, 52, 61, 72], 
       [61, 50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50, 61], 
       [52, 41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41, 52], 
       [45, 34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34, 45], 
       [40, 29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29, 40], 
       [37, 26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26, 37], 
       [36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36], 
       [37, 26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26, 37], 
       [40, 29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29, 40], 
       [45, 34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34, 45], 
       [52, 41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41, 52], 
       [61, 50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50, 61], 
       [72, 61, 52, 45, 40, 37, 36, 37, 40, 45, 52, 61, 72]]

PL6 = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (0, 2), 
       (-2, 0), (0, -2), (-1, 2), (-1, -2), (1, -2), (1, 2), (2, 1), (-2, -1), (2, -1), (-2, 1), 
       (-2, 2), (2, -2), (2, 2), (-2, -2), (3, 0), (0, 3), (-3, 0), (0, -3), (-1, -3), (-3, -1), 
       (-3, 1), (1, -3), (1, 3), (3, 1), (3, -1), (-1, 3), (-2, 3), (3, 2), (2, -3), (2, 3), 
       (-2, -3), (-3, 2), (-3, -2), (3, -2), (0, -4), (4, 0), (0, 4), (-4, 0), (-1, -4), (1, 4), 
       (1, -4), (-1, 4), (-4, -1), (4, -1), (-4, 1), (4, 1), (3, 3), (-3, -3), (3, -3), (-3, 3), 
       (-2, 4), (2, -4), (4, 2), (-4, 2), (2, 4), (4, -2), (-2, -4), (-4, -2), (4, -3), (5, 0), 
       (-3, 4), (0, 5), (4, 3), (-5, 0), (-4, -3), (0, -5), (3, 4), (-3, -4), (3, -4), (-4, 3), 
       (5, 1), (1, -5), (5, -1), (1, 5), (-1, -5), (-5, -1), (-5, 1), (-1, 5), (-5, -2), (2, 5), 
       (5, -2), (-2, -5), (5, 2), (-2, 5), (-5, 2), (2, -5), (-4, 4), (4, 4), (4, -4), (-4, -4), 
       (-3, 5), (5, -3), (3, 5), (-5, 3), (-5, -3), (-3, -5), (5, 3), (3, -5), (-6, 0), (0, 6),
       (0, -6), (6, 0), (-1, -6), (6, -1), (-6, 1), (6, 1), (-6, -1), (1, 6), (-1, 6), (1, -6), 
       (6, -2), (6, 2), (2, 6), (-2, 6), (-6, 2), (-6, -2), (-2, -6), (2, -6), (-5, 4), (5, -4), 
       (4, 5), (-4, 5), (-4, -5), (5, 4), (4, -5), (-5, -4), (-6, 3), (6, -3), (-3, 6), (-6, -3), 
       (3, -6), (3, 6), (-3, -6), (6, 3), (-5, 5), (-5, -5), (5, 5), (5, -5), (-4, -6), (-6, -4), 
       (6, -4), (-6, 4), (6, 4), (4, -6), (-4, 6), (4, 6), (5, -6), (5, 6), (-5, 6), (-6, 5), 
       (6, 5), (-6, -5), (6, -5), (-5, -6), (-6, -6), (-6, 6), (6, -6), (6, 6)]

SDM7 =[[98, 85, 74, 65, 58, 53, 50, 49, 50, 53, 58, 65, 74, 85, 98], 
       [85, 72, 61, 52, 45, 40, 37, 36, 37, 40, 45, 52, 61, 72, 85], 
       [74, 61, 50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50, 61, 74], 
       [65, 52, 41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41, 52, 65], 
       [58, 45, 34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34, 45, 58], 
       [53, 40, 29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29, 40, 53], 
       [50, 37, 26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26, 37, 50], 
       [49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49], 
       [50, 37, 26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26, 37, 50], 
       [53, 40, 29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29, 40, 53], 
       [58, 45, 34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34, 45, 58], 
       [65, 52, 41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41, 52, 65], 
       [74, 61, 50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50, 61, 74], 
       [85, 72, 61, 52, 45, 40, 37, 36, 37, 40, 45, 52, 61, 72, 85], 
       [98, 85, 74, 65, 58, 53, 50, 49, 50, 53, 58, 65, 74, 85, 98]]
                                                                                                                                                                                                                                                                                                                                                                                                                            

PL7 = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (0, 2), 
       (-2, 0), (0, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (2, 1), (2, -1), (1, -2), 
       (1, 2), (-2, -2), (-2, 2), (2, 2), (2, -2), (-3, 0), (0, -3), (0, 3), (3, 0), (3, -1), 
       (1, -3), (-3, -1), (-3, 1), (-1, 3), (-1, -3), (1, 3), (3, 1), (-3, 2), (-2, -3), 
       (3, 2), (2, -3), (3, -2), (2, 3), (-3, -2), (-2, 3), (0, -4), (4, 0), (-4, 0), (0, 4), 
       (1, 4), (-4, -1), (-4, 1), (-1, -4), (1, -4), (-1, 4), (4, 1), (4, -1), (3, -3), 
       (-3, 3), (-3, -3), (3, 3), (-2, -4), (4, 2), (2, -4), (2, 4), (-4, 2), (-2, 4), 
       (-4, -2), (4, -2), (0, -5), (-5, 0), (3, -4), (5, 0), (0, 5), (-4, -3), (3, 4), (4, -3), 
       (-3, 4), (4, 3), (-4, 3), (-3, -4), (-1, -5), (5, 1), (1, 5), (-5, -1), (-1, 5), (-5, 1), 
       (5, -1), (1, -5), (2, -5), (2, 5), (5, 2), (-5, -2), (-2, -5), (-5, 2), (-2, 5), (5, -2), 
       (-4, -4), (4, 4), (4, -4), (-4, 4), (5, -3), (-3, -5), (3, 5), (3, -5), (-5, 3), (5, 3), 
       (-3, 5), (-5, -3), (-6, 0), (0, -6), (0, 6), (6, 0), (6, 1), (-6, 1), (1, -6), (-6, -1), 
       (1, 6), (-1, -6), (-1, 6), (6, -1), (-2, -6), (2, -6), (-6, -2), (-2, 6), (6, 2), 
       (-6, 2), (6, -2), (2, 6), (4, -5), (5, -4), (4, 5), (-5, 4), (-5, -4), (5, 4), (-4, 5), 
       (-4, -5), (6, 3), (6, -3), (-6, 3), (-3, -6), (-6, -3), (3, -6), (3, 6), (-3, 6), (0, -7), 
       (0, 7), (-7, 0), (7, 0), (7, -1), (7, 1), (5, -5), (5, 5), (-5, 5), (-7, -1), (-1, -7), 
       (1, 7),(-7, 1), (-1, 7), (-5, -5), (1, -7), (4, -6), (-6, -4), (6, 4), (-4, 6), (4, 6), 
       (-6, 4), (-4, -6), (6, -4), (2, -7), (-2, 7), (7, 2), (-7, 2), (-2, -7), (2, 7), (7, -2), 
       (-7, -2), (7, -3), (7, 3), (-3, 7), (3, 7), (3, -7), (-7, 3), (-7, -3), (-3, -7), (6, 5), 
       (5, 6), (-5, 6), (-5, -6), (6, -5), (-6, 5), (5, -6), (-6, -5), (7, -4), (-4, -7), (4, -7), 
       (7, 4), (4, 7), (-4, 7), (-7, 4), (-7, -4), (-6, 6), (6, 6), (6, -6), (-6, -6), (5, 7), 
       (-5, 7), (7, 5), (-5, -7), (-7, 5), (7, -5), (-7, -5), (5, -7), (6, -7), (-6, -7), (6, 7), 
       (7, -6), (-6, 7), (7, 6), (-7, -6), (-7, 6), (-7, -7), (-7, 7), (7, -7), (7, 7)]

SDM8 = [[128, 113, 100, 89, 80, 73, 68, 65, 64, 65, 68, 73, 80, 89, 100, 113, 128],
        [113, 98, 85, 74, 65, 58, 53, 50, 49, 50, 53, 58, 65, 74, 85, 98, 113],
        [100, 85, 72, 61, 52, 45, 40, 37, 36, 37, 40, 45, 52, 61, 72, 85, 100], 
        [89, 74, 61, 50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50, 61, 74, 89],
        [80, 65, 52, 41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41, 52, 65, 80],
        [73, 58, 45, 34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34, 45, 58, 73],
        [68, 53, 40, 29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29, 40, 53, 68], 
        [65, 50, 37, 26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26, 37, 50, 65], 
        [64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64], 
        [65, 50, 37, 26, 17, 10, 5, 2, 1, 2, 5, 10, 17, 26, 37, 50, 65], 
        [68, 53, 40, 29, 20, 13, 8, 5, 4, 5, 8, 13, 20, 29, 40, 53, 68], 
        [73, 58, 45, 34, 25, 18, 13, 10, 9, 10, 13, 18, 25, 34, 45, 58, 73], 
        [80, 65, 52, 41, 32, 25, 20, 17, 16, 17, 20, 25, 32, 41, 52, 65, 80], 
        [89, 74, 61, 50, 41, 34, 29, 26, 25, 26, 29, 34, 41, 50, 61, 74, 89], 
        [100, 85, 72, 61, 52, 45, 40, 37, 36, 37, 40, 45, 52, 61, 72, 85, 100], 
        [113, 98, 85, 74, 65, 58, 53, 50, 49, 50, 53, 58, 65, 74, 85, 98, 113], 
        [128, 113, 100, 89, 80, 73, 68, 65, 64, 65, 68, 73, 80, 89, 100, 113, 128]]

PL8 =  [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), 
       (0, 2), (-2, 0), (0, -2), (-2, -1), (1, -2), (2, -1), (2, 1), (-1, -2), (-1, 2), 
       (-2, 1), (1, 2), (-2, 2), (2, -2), (-2, -2), (2, 2), (0, -3), (0, 3), (3, 0), 
       (-3, 0), (-3, -1), (-3, 1), (1, 3), (3, -1), (1, -3), (3, 1), (-1, 3), (-1, -3), 
       (3, -2), (-2, 3), (2, 3), (-3, -2), (2, -3), (3, 2), (-2, -3), (-3, 2), (4, 0), 
       (0, -4), (-4, 0), (0, 4), (-1, -4), (4, -1), (4, 1), (-1, 4), (-4, 1), (1, -4), 
       (-4, -1), (1, 4), (3, 3), (-3, 3), (3, -3), (-3, -3), (2, 4), (-4, 2), (4, -2), 
       (4, 2), (2, -4), (-4, -2), (-2, 4), (-2, -4), (0, 5), (-3, -4), (5, 0), (4, -3), 
       (3, -4), (-3, 4), (-4, 3), (-4, -3), (0, -5), (4, 3), (-5, 0), (3, 4), (-5, 1), 
       (5, -1), (-1, 5), (1, 5), (1, -5), (-1, -5), (-5, -1), (5, 1), (5, -2), (2, -5), 
       (-5, -2), (-5, 2), (2, 5), (5, 2), (-2, 5), (-2, -5), (4, -4), (4, 4), (-4, 4),
       (-4, -4), (3, 5), (5, -3), (5, 3), (-5, -3), (-5, 3), (3, -5), (-3, 5), (-3, -5), 
       (0, -6), (6, 0), (-6, 0), (0, 6), (-1, 6), (1, -6), (6, 1), (6, -1), (-1, -6), 
       (-6, 1), (-6, -1), (1, 6), (-2, 6), (2, 6), (-2, -6), (6, 2), (2, -6), (-6, -2), 
       (-6, 2), (6, -2), (-5, 4), (-5, -4), (5, 4), (-4, -5), (-4, 5), (4, -5), (4, 5), 
       (5, -4), (6, 3), (3, -6), (-3, 6), (3, 6), (-6, 3), (-3, -6), (-6, -3), (6, -3), 
       (-7, 0), (0, 7), (0, -7), (7, 0), (-7, 1), (5, -5), (1, 7), (-5, -5), (5, 5), 
       (7, -1), (-7, -1), (-5, 5), (7, 1), (1, -7), (-1, 7), (-1, -7), (4, -6), (4, 6), 
       (6, 4), (-4, -6), (-4, 6), (6, -4), (-6, 4), (-6, -4), (-2, 7), (-7, 2), (-7, -2), 
       (7, 2), (2, -7), (-2, -7), (2, 7), (7, -2), (-7, -3), (3, 7), (7, -3), (7, 3), 
       (-3, 7), (-3, -7), (-7, 3), (3, -7), (5, 6), (5, -6), (6, -5), (-6, -5), (6, 5), 
       (-5, 6), (-5, -6), (-6, 5), (8, 0), (0, 8), (-8, 0), (0, -8), (-4, -7), (4, 7), 
       (-4, 7), (7, 4), (-7, 4), (-7, -4), (8, -1), (8, 1), (7, -4), (-1, -8), (-8, 1), 
       (1, 8), (1, -8), (4, -7), (-8, -1), (-1, 8), (-2, 8), (8, 2), (2, -8), (8, -2), 
       (-8, -2), (-8, 2), (2, 8), (-2, -8), (-6, 6), (-6, -6), (6, -6), (6, 6), (-8, -3), 
       (-8, 3), (3, 8), (-3, 8), (-3, -8), (8, 3), (3, -8), (8, -3), (5, 7), (-5, -7), 
       (-7, 5), (7, 5), (-5, 7), (5, -7), (-7, -5), (7, -5), (8, -4), (8, 4), (-8, -4), 
       (-4, -8), (-8, 4), (4, -8), (-4, 8), (4, 8), (-6, -7), (-6, 7), (6, -7), (-7, 6), 
       (6, 7), (-7, -6), (7, 6), (7, -6), (8, -5), (-5, -8), (-5, 8), (-8, 5), (-8, -5), 
       (5, -8), (5, 8), (8, 5), (7, -7), (-7, -7), (-7, 7), (7, 7), (8, 6), (-8, 6), 
       (8, -6), (6, -8), (-6, -8), (6, 8), (-8, -6), (-6, 8), (8, -7), (-7, 8), (8, 7), 
       (7, -8), (-7, -8), (-8, 7), (-8, -7), (7, 8), (-8, -8), (-8, 8), (8, -8), (8, 8)]



SDM = [SDM1, SDM2, SDM3, SDM4, SDM5, SDM6, SDM7, SDM8]
PL = [PL1, PL2, PL3, PL4, PL5, PL6, PL7, PL8]
