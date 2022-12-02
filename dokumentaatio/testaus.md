# Testausdokumentti

## Yksikkötestaus
- yksikkötestit toteutuettu seuraaville luokille ja moduleille:
    - KNN-luokka
    - Mnistdata-luokka
    - DataHandler-luokka
    - utils-moduli
- yksikkötestauksesta on jätetty pois käyttöliittymä, sekä projekti/konfigurointi -modulit, jotka sisältävät lähinnä vakioita
- testikattavuus on 94%. Testaamatta jäävät tapaukset liittyvät lähinnä tiedostojen luontiin, mutta näien toimivuus on todettu manuaalisesti


## Testikattavuus
Testikattavuusraportti](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/TestCoverageReport.png

## Suorituskykytestaus
Ohjelman suorituskykyä on testattu erillisellä ohjelmalla (yksinkertainen python main-ohjelma, joka vain luuppaa datahandler oliota eri parametreillä). Suorituskyvyn testaamisessa on haettu parhaiten toimivia parametrejä:
- nopeuden suhteen
- tunnistamisen oikeellisuuden suhteen

Johtuen ohjelman hitaudesta, testaamiseen käytetyt data-joukot ovat pienehköjä. Oikeiden numeroiden tunnistamisessa on selvästi satunnaisvaihtelua; X 

### kerrosten optimointi
Kerrosten (eli kuin läheltä pistettä haetaan kuvan lähintä pistettä boolean matriisista) vaikutusta ajoaikaan on tutkittu muuttamalla "kerrokset" parametria välillä 1-8. Kerrosten määrä ei vaikuta tulosten oikeellisuuten, vain ajoaikaan. 
- ajoaika paranee merkittävästi 4:n kerrokseen asti, jonka jälkeen se on lähes vakio
- jonkinlainen optimi löytyy 7:llä kerroksella (tosin erot välillä 4-8 ovat olemattomia)
- ajossa käytetyt paramatrit:
    - testidatan indeksit [500, 600]
    - opetusdatan indeksit [0, 500]
    - k-arvo 2
    - suodatin 128

![Ajoaka](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/runtime_vs_layers.png)

### k-arvo
K-arvon optimia tutkittiin seuraavalla datalla:
- testidatan indeksit [500, 550]
- opetusdatan indeksit [0, 500]
- suodatin 128
- k-arvo välillä 1-100

![k-arvo](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/k_value_vs_wrong.png)

Tämän perusteella k-arvon optimi on 3 tai 4 (normaalisti knn:ssä käytetään parittomia k-arvoja, joten 3). Huomioitava tässäkin testissä, että sekä opetusjoukko että testijoukko olivat hyvin pieniä. Tulos saattaisi poiketa isommilla joukoilla. 


### Suodattimen arvo
Harmaasuodattimen arvon vaikutusta tutkittiin seuraavalla datalla:
    - testidatan indeksit [500, 600]
    - opetusdatan indeksit [0, 1000]
    - k-arvo 3
    - suodatin [50, 75, 100, 125, 150, 175]

Hieman yllättäen paras tulos tuli arvoilla 50, 75 ja 175, ja huonoin tulos arvolla 125 (lähellä 0-255 harmaasävykuvien puoliväliä, joka olisi intuitiivisesti looginen valinta). Tässäkin tietysti testi ja opetusdata on melko rajallinen joukko

![suodatin](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/filter_vs_wrong.png)

### Tunnistuksen tarkkuus
lisättävä

## Koodin laadunseuranta
- koodin pylint arvo on pudonnot 9.68/10
- käyttöliittymä ja testit eivät ole mukana pylint arviossa
