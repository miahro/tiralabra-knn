# Käyttöohje


## Asennus
 - riippuvuuksien hallintaan on käytetetty poetrya
 - kloonaa repositorio
 - asenna riippuvuudet poetryn virtuaaliympäristöön komennolla "poetry install"
 - aja ohjelma komennolla "poetry run invoke start"


## Käyttöliittymä
Ohjelma sisältää hyvin yksinkertaisen käyttöliittymän. Näkymissä voi liikkua yhden eteen tai taaksepäin

### MNIST datan lataus
- tässä näkymässä voidaan asettaa harmaasuodattimen arvo (oletus 128)
- merkitys: MNIST data on harmaasävydataa (0-255), ja KNN/Hausdorff laskentaa varten data tulee muuntaa mustavalkoiseksi. Suodattimen arvoa pienemmät arvot tulkitaan nollaksi (valkoinen) ja yhtäsuuret ja suuremmat ykkösiksi (musta)
- kun suodatin on asetettu (tai oletus jätetty voimaan) "Lataa MNIST data" lataa MNIST datan ohjelman muistiin
    - huom! tämä kestää jonkin aikaa, luokkaa 10-30 sekuntia

![load](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/mnist_load_view.png)

### Parametrien asetus näkymä
- tässä näkymässä asetetaan parametrit KNN:ää varten (tai jätetään oletukset voimaan)
- testidatan alku ja loppuindeksi
- opetusdatan alku ja loppuindeksi
- HUOM!! ohjelma on vielä hyvin hidas. 10 000 datapistettä (testidata x opetusdata) kestää noin 80 sekuntia, joten älä aja äärimmäisen suurilla testi ja opetusjoukoilla
- k-arvon (eli kuika monta lähintä naapuria KNN etsii luokittelua varten)
- "kerrosten" määrän: tämä on sisäisen toteutuksen optimointiin vaikuttava parametri. Ei vaikuta tulokseen, vaikuttaa marginaalisesti nopeuteen. Kannattaa pitäää välillä 4-6. 

![parameters](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/parameters_view.png)


### Tulosnäkymä
- näyttää tulokset
 - oikein tunnisttettujen määrän
 - väärin tunnistettujen määrän
 - suoritusajan
 - väärin tunnistettujen indeksit
 - väärin tunnistettujen indeksit alkuperäisessä MNIST tietokannassa
 - väärin tunnistetut numerot
 - ennustetut numerot
 - oikeat numerot

![results](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/kuvat/result_view.png)