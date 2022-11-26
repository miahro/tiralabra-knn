# Viikkoraportti 4

## Viikon aikana tehty
- Edellisen viikon KNN / Hausdorff laskennassa oli bugeja, nämä korjattu
- KNN toteutettu sekä listana (joka järjestetään), minimikekona, sekä minimikekoversiona, jossa ei ole ulkoisia funktiokutsuja. Viimeinen jätetty käyttöön. Eri versiot tarvittiin tulosten oikeellisuuden varmistamiseksi
- toteutettu Datahandler luokka (ylätason luokka, joka ei tee laskentaa, vaan hallinnoi millä datajoukoilla KNN:ää ajetaan, ja käsittelee tulokset)
- toteutettu käyttöliittymä
- testien kirjoitusta ja manuaalista testausta

## Edistyminen
- työ edistyi sinänsä suunnitellun aikataulun mukaan, ja ehkä jopa vähän paremmin
- toki suorituskyky ongelma (ks alla kohta ongelmia) ei varsinaisesti ratkennut

## Opittua
- yleinen ymmärrys KNN:n ja Hausdorffin etäisyyksien laskennasta parantunut

## Ongelmia
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
- nopeusongelman syyn löytäminen; tämä on aika lailla edellytys järjestelmällisemmälle suorituskykytestaukselle
- järjestelmällisempi suorituskyky testaus vs. parametrit, vs käytetty etäisyys
- käyttöliittymän parantaminen, jos aikaa jää. Voisi olla hyvä pystyä plottaamaan MNIST numeroit kälistä, erityisesti väärin tunnistettuja






