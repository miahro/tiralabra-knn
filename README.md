# Numeroiden tunnistus 

- Kurssin tietorakenteet ja algoritmit harjoitustyö, periodi 2/2022 projekti
- MNIST käsinkirjoitettujen numeroiden tunnistus kNN algoritmilla, käyttäen Hausdorffin etäisyyksiä

## Asennus
 - riippuvuuksien hallintaan on käytetetty poetrya
 - kloonaa repositorio
 - asenna riippuvuudet poetryn virtuaaliympäristöön komennolla
 ```bash
 poetry install
 ``` 
 - aja ohjelma komennolla
  ```bash
 poetry run invoke start
```
 - tarkemmat ohjeet, ks [manuaali](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/manuaali.md)


## Muut komentorivitoiminnot
- yksikkötestit voi ajaa komenolla
 ```bash
 poetry run invoke test
```
- testikattavuusraportin voi luoda komennolla (ajaa myös yksikkötestit):
 ```bash
 poetry run invoke coverage-report
```
- koodin laadun voi tarkastaa *pylint*-työkalulla komennolla:
 ```bash
 poetry run invoke lint
```



## Dokumentaatiolinkit
- [tuntikirjanpito](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/tuntikirjanpito.md#ty%C3%B6aikakirjanpito)
- [viikkoraportti 1](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/viikkoraportti_1.md)
- [viikkoraportti 2](dokumentaatio/viikkoraportti_2.md)
- [viikkoraportti 3](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/viikkoraportti_3.md)
- [viikkoraportti 4](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/viikkoraportti_4.md)
- [viikkoraportti 5](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/viikkoraportti_5.md)
- [viikkoraportti 6](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/viikkoraportti_6.md)
- [viikkoraportti 7](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/viikkoraportti_7.md)
- [määrittelydokumentti](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/Maarittely.pdf)
- [testausdokumentti](dokumentaatio/testaus.md)
- [toteutusdokumentti](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/toteutus.md)
- [manuaali](https://github.com/miahro/tiralabra-knn/blob/main/dokumentaatio/manuaali.md)
- [loppupalautus release](https://github.com/miahro/tiralabra-knn/releases/tag/loppupalautus)

