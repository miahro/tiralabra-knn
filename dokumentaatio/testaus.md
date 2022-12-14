# Testausdokumentti

## Yksikkötestaus
- yksikkötestit toteutuettu seuraaville luokille ja moduleille:
    - KNN-luokka
    - Mnistdata-luokka
    - DataHandler-luokka
    - utils-moduli
- yksikkötestauksesta on jätetty pois käyttöliittymä, sekä projekti/konfigurointi -modulit, jotka sisältävät lähinnä vakioita
- testikattavuus on 94%. Testaamatta jäävät tapaukset liittyvät lähinnä tiedostojen luontiin, mutta näien toimivuus on todettu manuaalisesti


### Testikattavuus
![Testikattavuusraportti](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/TestCoverageReport.png)

## Järjestelmätestaus
Järjestelmätestausta on suoritettu manuaalisesti, havaitut ongelmat on korjattu.

## Suorituskykytestaus
Ohjelman suorituskykyä on testattu erillisellä ohjelmalla (yksinkertainen python main-ohjelma, joka vain luuppaa datahandler oliota eri parametreillä). Suorituskyvyn testaamisessa on haettu parhaiten toimivia parametrejä:
- nopeuden suhteen
- tunnistamisen oikeellisuuden suhteen

Johtuen ohjelman hitaudesta, testaamiseen käytetyt data-joukot ovat pienehköjä. Oikeiden numeroiden tunnistamisessa on selvästi vaihtelua riippuen valitusta datajoukosta. 

### kerrosten optimointi
Kerrosten (eli kuin läheltä pistettä haetaan kuvan lähintä pistettä boolean matriisista) vaikutusta ajoaikaan on tutkittu muuttamalla "kerrokset" parametria välillä 1-8. Kerrosten määrä ei vaikuta tulosten oikeellisuuten, vain ajoaikaan. 
- ajoaika paranee merkittävästi 4:n kerrokseen asti, jonka jälkeen se on lähes vakio
- jonkinlainen optimi löytyy 7:llä kerroksella (tosin erot välillä 4-8 ovat olemattomia)
- ajossa käytetyt paramatrit:
    - testidatan indeksit 500 - 600
    - opetusdatan indeksit 0 - 500
    - k-arvo 2
    - suodatin 128

![Ajoaka](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/runtime_vs_layers.png)

### k-arvo
K-arvon optimia tutkittiin seuraavalla datalla:
- testidatan indeksit 500 - 550
- opetusdatan indeksit 0 - 500
- suodatin 128
- k-arvo välillä 1-100

![k-arvo](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/k_value_vs_wrong.png)

Tämän perusteella k-arvon optimi on 3 tai 4 (normaalisti knn:ssä käytetään parittomia k-arvoja, joten 3). Huomioitava tässäkin testissä, että sekä opetusjoukko että testijoukko olivat hyvin pieniä. Tulos saattaisi poiketa isommilla joukoilla. 


### Suodattimen arvo
Harmaasuodattimen arvon vaikutusta tutkittiin seuraavalla datalla:
    - testidatan indeksit 500-600
    - opetusdatan indeksit 0-1000
    - k-arvo 3
    - suodatin [50, 75, 100, 125, 150, 175]

Hieman yllättäen paras tulos tuli arvoilla 50, 75 ja 175, ja huonoin tulos arvolla 125 (lähellä 0-255 harmaasävykuvien puoliväliä, joka olisi intuitiivisesti looginen valinta). Tässäkin tietysti testi ja opetusdata on melko rajallinen joukko

![suodatin](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/filter_vs_wrong.png)

### Suoritusaika testi- ja opetusdatan suhteen
- suoritusaika määritettiin testijoukolla:
    - testidatan indeksit 0-500
    - opetusdatan inkdeksit 0 - [100, 500, 1000, 2000, 5000, 10000, 30000, 60000]
    - harmaasuodatin 75
    - k-arvo 3
    - kerrokset 7
- tulokset:
    - ajoaika on selvästi lineaarinen (kuten pitääkin) suhteessa testidatan määrä * opetusdatan määrä (eli O(MN))
    - yksi testinumero vs yksi opetusnumero kestää 0,8 millisekuntia
    - näin ollen koko 10k * 60k datajoukko kestäisi 134 tuntia

![ajoaika2](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/runtime_vs_train.png)


### Tunnistuksen tarkkuus
Tunnistuksen tarkkuutta testattiin seuraavalla datalla:
- testidatan indeksit 0-500
- opetusdatan inkdeksit 0 - [100, 500, 1000, 2000, 5000, 10000, 30000, 60000]
- harmaasuodatin 75
- k-arvo 3
- kerrokset 7
- tulokset:
    - tunnistuksen tarkkuus parani, eli virheprosentti pieneni opetusdatan kasvaessa. Tämä toimii kuten pitääkin
    - täydellä 60k opetusdatalla päästiin 2,6% virheeseen, eli 97,4% tunnistustarkkuuteen, jota voidaan pitää kohtalaisen hyvänä

![virheprosentti](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/error_vs_train.png)

Täydellä opetusjoukolla virheellisiä tunnistuksia oli 13 kpl (500 kappaleesta). Väärin tunnistetut numerot olivat:
- [4, 4, 9, 4, 4, 8, 2, 4, 3, 6, 4, 9, 8]

| numero | vääriä |
| :---: | :----:|
| 0 | 0  | 
| 1 | 0  | 
| 2 | 1  | 
| 3 | 1  | 
| 4 | 6  | 
| 5 | 0  | 
| 6 | 1  | 
| 7 | 0  | 
| 8 | 2  | 
| 9 | 2  | 

Numero 4 oli siis selkeästi vaikein tunnistaa.

### Tunnistuksen tarkkuus toisella testijoukolla
Kohtalaisen pienillä testijoukoilla testijoukon valinta vaikuttaa jonkin verran tunnistustarkkuuteen. Tämän tutkimiseksi ajettiin tunnistuksen tarkkuus testi myös seuraavilla parametreilla:
- testidatan indeksit 1000-2000
- opetusdatana koko opetusjoukko (indeksit 0-60000)
- harmaasuodatin 75
- k-arvo 3
- kerrokset 7

Tästä tuloksina:
| parametri | tulos | yksikkö |
| :---: | :----:| :----:|
| virheellisesti tunnistettuja | 36  | kpl |
| virheprosentti | 3,6  | %|
| tunnistustarkkuus  | 96,4  | % |
| ajoaika | 13,1  | h |

Väärien frekvenssit
| numero | vääriä |
| :---: | :----:|
| 0 | 0  | 
| 1 | 0  | 
| 2 | 2  | 
| 3 | 2  | 
| 4 | 5  | 
| 5 | 5  | 
| 6 | 2  | 
| 7 | 7  | 
| 8 | 5  | 
| 9 | 8  | 

Tämä tulos poikkesi jossain määrin edellisestä joukosta, nyt vaikemmat tunnistettavat olivatkin numerot 9 ja 7. 

### Muiden Hausdorff-etäisyyksien testaus
Vaihtoehtoita testattiin myös muita etäisyysmittoja verrattuna muussa testauksessa käytettyyn f3:n:
- f1 = min(d(A,B), d(B,A))
- f2 = max(d(A,B), d(B,A))
- f4 = N_a * d(A,B) + N_b * d(B,A) ; tämä siis ilman jakajaan (N_a+N_b), koska tämä ei vaikuta järjestykseen

Testi ajettiin seuraavilla parametreilla:
- testidatan indeksit 0-500
    - opetusdatan inkdeksit 0 - 1000
    - harmaasuodatin 75
    - k-arvo 3
    - kerrokset 7

Tulokset
| f | vääriä |
| :---: | :----:|
| f1 | 138  | 
| f2| 61  | 
| f3 | 51  | 
| f4 | 56  | 



Vaikka testijoukko on pieni ja opetusjoukko myös hyvin pieni, tulos näyttää kuitenkin melko selvästi, että f3 eli d(A,B)+ d(B,A) antaa parhaan tuloksen. Näin ollen muita suuntaamattomia etäisyyksiä ei ole testattu tämän enempää. 

## Koodin staattisen laadun seuranta
- koodin pylint arvo on 9.76/10
- pylintin havaitsemat virheet ovat lähinnä "too many attributes", "too many branches" ja "too many arguments" virheitä. Nämä johtuvat pitkälti siitä, että knn/Haudorff -laskenta on tehokkuusyistä toteutettu yhdessä luokassa ja yhdessä funktiossa. Koodista saisi helposti tyylillisesti parempaa jakamalla toiminnallisuutta eri luokkiin ja funktioihin, mutta tämä toisaalta aiheuttaisi usein toistuvia funktiokutsuja ja suoritusnopeuden hidastumista
- käyttöliittymä ja testit eivät ole mukana pylint arviossa
