# Testausdokumentti

## Yksikkötestaus
- modulille utils toteutettu yksikkötestit
- luokalle KNN toteutettu yksikköstestit
    - testikattavuus 91% , manuaalisesti laskettu testitapaus ei kata kaikkia tapauksia, laajennetaan myöhemmin
    - huomioitava, että yksikkötesti ei ainakaan tässä vaiheessa testaa KNN:n oikeellisuutta, lähinnä vain, että palautettu arvo on oikeaa tyyppiä
- luokalle Mnistdata on toteutettu yksikkötestit:
    - testikattavuus 88%, koska testitapaus testaa vain jo ladatun tiedoston tapauksen. Korjataan ja laajennetaan seuraaviin palautuksiin.
- luokalle DataHandler on toteutettu yksikkötestit:
    - testikattavuus on vain 59%, koska tulostenkäsittelyfunktioiden testaus edellyttäisi oikein tuloksen tietämistä, ja tätä ei voi helposti KNN:n tapauksessa toteuttaa

## Testikattavuus
![Testikattavuusraportti](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/TestCoverageReport.png)

## Suorituskykytestaus
Ohjelman suorituskykyä on testattu manuaalisesti, eikä tässä vaiheessa kovin järjestelmällisesti. 
- laskenta on edelleen liian hidas. KNN:n ajaminen yhdellä testinumerolla ja 60 000 opetusdatapisteellä kestään noin 50 sekuntia. Tämä tarkoittaisi, että koko 10 000 testidatan ajaminen kestäisi 6 päivää. 
- KNN:n parametreja (johtuen osittain hitaasta laskennasta) eikä eri vaihtoehtoja etäisyysmitoiksi ei ole vielä järjestelmällisesti testattu. Kuitenkin jo alustavien testien perusteella on selvää, että numeroiden tunnistus toimii vähintään tyydyttävästi jopa kohtalaisen pienillä opetusdatajoukoilla. Esimerkiksi:
    - MNIST testi datat 0-99
    - MNIST opetusdata 0-999
    - k-arvolla 6
    - etäisyysmittana neliöllisten etäisyyksien summa
    - tunnistetaan oikein 95% numeroista
    - ajoaika 82 sekuntia

## Koodin laadunseuranta
- koodin pylint arvo on pudonnot 7.82/10.00 
- osa tästä on johtuu tehokkuusvaatimuksesta, mutta osa siitä, että aika ei riittänyt siistiä koodia riittävästi tämän viikon palautukseen
- parannetaan seuraavaan palautukseen