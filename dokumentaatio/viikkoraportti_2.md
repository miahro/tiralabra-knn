# Viikkoraportti 2

## Viikon aikana tehty
- Toteutettu DirectedHausdorff luokka ja sen yksikköltestit
- Toteutettu Undirected Hausdorff luokka ja sen yksikkötestit
- Toteutettu Mnistrawdata -luokka (käyttää valmista python-mnist pakettia raakadataan) ja siihen mustavalkoiseksi sekä pistejoukoksi konvertointi, ja tälle yksikkötestit

## Edistyminen
- Työn edistyminen on jotakuinkin suunnitelman mukainen. Tosin tunteja meni paljon suunniteltua enemmän. Aikaa kului suhteettoman paljon teknisten yksityiskohtien säätämiseen (importtien toiminta poetry:ssä ja pytestissä vs normaalisti ajattavassa Python ohjelmassa oli ja on edelleen itselle hankala asia). Lisäksi paljon hukkaa tuli alustavassa ajatuksessa käyttää keras pakettia MNIST datan lukemiseen: tämä oli huono idea, koska toimii käytännössä ainoastaan conda ympäristössä, vaatii lisäpaketteja, jotka vaativat Python version downgreidausta, jne. 

## Opittua
- Hausdorffin etäisyyksien laskennan ymmärrän nähdäkseni tässä vaihessa hyvin. Erityisesti testien toteuttaminen pakotti laskemaan testitapaukset ulkoisesti ja ohjelmallisesti, ja tämä auttoi asian sisäistämisessä paljon enemmän kuin teorian opiskelu
- yksikkötestien tekemiseen (aikaisemmin tunsin periaatteen, mutta en käytännön, tasolla) tuli jo jonkinverran rutiinia

## Ongelmia
- Ei varsinaisia toteutukseen liittyviä ongelmia tässä vaiheessa. Epäilyksiä tehokkuudesta, mutta tässä vaiheessa kun on vasta toteutettu ja testattu yksittäisiä luokkia, eikä ajattu varsinaista tietokantadataa nämä ovat vasta epäilyksiä. 
- Ei kiireellinen kysymys: disabloin pylint tyylintarkastustyökalussa "invalid name" tarkistuksen. Tämä siksi, että sovelluksen matemaattisten muuttujien nimeäminen noudattaa lähdejulkaisun (ja yleisten matemaattisen konventioiden) merkintöjä, mutta nämä ovat kaikki snake_case tyylin vastaisia. Joutuu siis tekemään valinnan 1) keksin omat nimet, ja koodin vs kaavojen vertailu muuttuu lähes mahdottomaksi, tai 2) pitää koodin vs kaavat yhdenmukaisina, vaikka tämä on huonoa Python tyyliä. Lienee ok tehdä tyylillisesti huonoa, jotta selkeys säilyy?

## Suunnitelma seuraavalle viikolle
- Ainakin brute force kNN algoritmin toteutus. Brute force ei tule toimimaan lopullisena versiona, mutta tarvitsen tämän lähtö- ja vertailukohdaksi, jotta tulosten järkevyyttä pienellä joukolla voi jotenkin arvioida.
- Alustavia testejä oikealla MNIST datalla (luultavasti pienillä osajoukoilla), jotta saa jonkinlaisen käsityksen luokkien toimivuudesta
- Jonkinlainen alustava käyttöliittymä. Tähän asti ajurina on toiminut vain main.py, johon lisätty rivi kerrallaan kutsuja luokille ja funktioilla, joita on testaillut kehitysvaiheessa. Toiminut ok tähän asti, mutta laajemmissa testeissä ei tule enää toimimaan. 




