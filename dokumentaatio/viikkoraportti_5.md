# Viikkoraportti 5

## Viikon aikana tehty
- käyttöliittymää parannettu
    - asetetut parametrit säilyvät muistissa, jolloin toistoja on helpompi tehdä
    - tulokset esitetään järkevämmässä muodossa
    - testinumero voidaan plotata
    - tulokset voidaan tallentaa .csv-tiedostoon
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
- tämä on toisto viime viikolta, koska suorituskyvyn pullonkaulaa ei löytynyt
- suuria ongelmia suoritusajan kanssa. Tällä hetkellä yhdelle testipisteelle koko opetusdatan (eli 1 X 60k) kestää edelleen n. 50 sekuntia. Eli koko 10k x 60k kestäisi n 6 päivää. 
- en ymmärrä / löydä vikaa, nähdäkseni katkaisen loopit ensimmäisessä mahdollisessa kohdassa
- seuraavia asioita olen testannut / yrittänyt optimoida, mutta näiden vaikutus on vain luokkaa plus-miinus muutama sekunti / 50 sekunnin kokonaisuus:
    - euklidisesta etäisyydestä siirrytty neliölliseen etäisyyteen
    - funktiokutsuja vähennetty (ts laskenta integroitu yhteen isoon funktioon), tämänkin vaikutus on pieni
    - pisteen ja pistejoukon minimietäisyyden laskemiseksi yritetty listakoostetta, josta minimi, pelkän minimin ylläpitoa (tämä marginaalisesti paras, joten jätetty näin)
    - "kerrosten määrää" (eli montako pistettä haetaan boolean matriisista) säädetty; tämänkin vaikutus on melko marginaalinen, on kerroksia mitä vain 3-7
    - knn toteutettu listana ja minimikekona; tämänkin vaikutus on hyvin pieni, kuitenkin keko marginaalisesti parempi, ja se jätetty ratkaisuksi
    - numpy arrayt vaihdettu tavallisiksi listoiksi, paransi aikaa jonkin verran
- tiedän, että ongelma ei johdu seuraavista:
    - Datahandler ylätason luokasta (testattu käyttämällä KNN luokkaa ilman tätä, ja ajoaika on sama)
    - käyttöliittymästä (käli ei sisällä mitään laskentaa, ja testattu manuaalisesti, että ajoaika on sama ilman käliä)

## Suunnitelma seuraavalle viikolle
- nopeusongelman syyn löytäminen







