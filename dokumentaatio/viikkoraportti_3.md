# Viikkoraportti 3

## Viikon aikana tehty
- hylätty aikaisemmin kirjoitetut luokat DirectedHausdorff, Undirected Hausdorff, Mnistrawdata -luokka 
- kirjoitettu uusi Mnistdata luokka, joka lukee datan suoraan http://yann.lecun.com/exdb/mnist/ sivulta ja tallettaa datan järkevämpään tietorakenteeseen
- kirjoitettu uusi KNN luokka, joka sisältää:
    - alustavan KNN algoritmin
    - Hausdorff etäisyyden laskennan (tällä hetkellä d6b ja f4)
- kirjoitettu moduuli utils, joka sisältää apufunktioita (euklidinen etäisyys ja euklidisten etäisyyksien taulukointi) 
- kirjoitettu yksikkötestejä toteutetuilla luokille sekä moduleille
- testattu KNN:n toimivuutta hyvin pienillä datajoukoilla (muutamia kymmeniä testidatoja, n 1000 opetusdataa). Testaus oli hyvin alustavaa, eikä kovin järjestelmällistä. Lähinnä tarkoituksena oli nähdä, että KNN antaa ainakin jossain määrin järkeviä tuloksia (hyvin pienilläkin joukoilla kuitenkin yli 50% oikein, kun arvaamalla tulisi n 10%). 
- Hausdorffin etäisyyden laskentaa alustavasti optimoitu. Tämä on kaukana valmiista, mutta suunta on oikea (ensimmäinen yritys pienistä testeistä ekstrapoloiden olisi kestänyt n 1 vuosi 10k/60k datalla, nyt ollan 6 päivässä, mutta sekunteihinn pitäisi toki päästä)

## Edistyminen
- Työ edistyi tällä viikolla hitaammi kuin suunnniteltu. Tämä johtui osittain, siitä että päädyin hylkäämään aiemmat luokat, ja kirjoittamaan uudet. Osittain oman ajankäytön ongelmista ja hölmöihin ratkaisuyrityksiin ajan tuhlaamisesta. 
- Aikataulu on kiinniotettavissa

## Opittua
- Ymmärrän KNN:n paremmin
- Myös Hausdorffin etäisyyksien laskennan kokonaisuus alkaa hahmottua paremmin

## Ongelmia
- ei varsinaisia

## Suunnitelma seuraavalle viikolle
- Hausdorffin etäisyyksien laskennan optimointi, tämä on edellytys KNN:n järkevellä testaamiselle 
    - ainakin selvästi dist_point_set_all (eli pisteen ja pistejoukon kaikkien pisteiden läpikäynti) on hyvin huono, kymmenkertaistaa laskenta-ajan. Tätä en vielä ehtinyt edes yrittää järkevöittää, joten varmasti tästä tipahtaa helposti jotain
    - ja koko algoritmi on tällä hetkellä vain hyvin heikosti optimoitu, pitäisi löytyä helposti lisää tehoa
- järjestelmällisempiä testejä oikealla MNIST datalla
- testikattavuuden parantaminen
- Jonkinlainen alustava käyttöliittymä. Tähän asti ajurina on toiminut vain main.py, johon lisätty rivi kerrallaan kutsuja luokille ja funktioilla, joita on testaillut kehitysvaiheessa. Toiminut ok tähän asti, mutta laajemmissa testeissä ei tule enää toimimaan. 




