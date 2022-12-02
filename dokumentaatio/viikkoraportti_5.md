# Viikkoraportti 5

## Viikon aikana tehty
- käyttöliittymää parannettu
    - asetetut parametrit säilyvät muistissa, jolloin toistoja on helpompi tehdä
    - tulokset esitetään järkevämmässä muodossa
    - testinumero voidaan plotata
    - tulokset voidaan tallentaa .csv-tiedostoon
- muutettu etäisyyslaskennassa toiseen potenssiin korutus kertolaskulla:
    - tämä parantaa laskennan nopeutta silloin kun läpikäytäviä kerroksia on vähän (eli suoraan etäisyyslaskentaan menee suuri osa)
    - kuitenkin, tälläkin muutoksella ajan minimi lötyy noin 7-kerroksesta, jolloin suoran etäisyyslaskennan nopetus ei auta merkittävästi
- yksikkötestien kattavuutta parannettu
- koodin staattista laatua parannettu
- dokumentaatiota päivitetty
- tehty paljon manuaalisia testejä

## Edistyminen
- työ edistyi muuten hyvin ja suunnitellusti, mutta suorituskykyongelman juurisyy ei löytynyt
- suorituskyvyn järjestmällisempi testaus pääsi parempaan vauhtiin

## Opittua
- varsinaisesti ei uutta oppia KNN:stä tai Hausdorffin etäisyyksistä
- toki koodaus/testaus/dokumentointi rutiini parantunut koko ajan

## Ongelmia
- suoritusaika on edelleen pullonkaula
- ohjaajalta saatu hyviä vinkkejä, näitä testattu, mutta silti edelleen ollaan luokassa noin 44 sekuntia, per testidata koko opetusjoukolla (eli 5 päivää kestäisi koko 10k x 60k data)
- alan olla vakuuttunut, ettei nykyisen toteutuksen laskennan optimointi johda merkittäviin parannuksiin
- jäjellä oleva parannusyritys on käyttää bittimatriisiesitystä, tämä on sen verran iso muutos, ettei onnistu tämän viikon palautukseen


## Suunnitelma seuraavalle viikolle
- ohjaajan vinkistä yritän nopeuttaa laskentaa käyttämällä bittimatriisiesitystä
    - tämä on suuri ja riskialtis muutos (riskit väärälle laskennalle, ei yhtä suoraviivainen tarkastaa ja testata kuin normaali laskenta)
    - yritetään kuitenkin
- riippumatta siitä, onnistuuko bittimatriisitoteutus vai ei, suorituskykysytestausta tunnistuksen ja parametrien optimoinnin suhteen jatketaan

