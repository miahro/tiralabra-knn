# Testausdokumentti

## Yksikkötestaus
- modulille utils toteutettu yksikkötestit
- luokalle KNN toteutettu yksikköstestit
    - testikattavuus 91% , manuaalisesti laskettu testitapaus ei kata kaikkia tapauksia, laajennetaan myöhemmin
    - huomioitava, että yksikkötesti ei ainakaan tässä vaiheessa testaa KNN:n oikeellisuutta, lähinnä vain, että palautettu arvo on oikeaa tyyppiä
- luokalle Mnistdata on toteutettu yksikkötestit:
    - testikattavuus 88%, koska testitapaus testaa vain jo ladatun tiedoston tapauksen. Korjataan ja laajennetaan seuraaviin palautuksiin.

## Testikattavuus
![Testikattavuusraportti](dokumentaatio/TestCoverageReport.png)

## Koodin laadunseuranta
- toteutuille luokille ja moduleille pylint arvot 9.20-10.00
- .pylintrc :ssä disabloitu virhe C0103 "invalid name", snake_case konvention noudattaminen johtaisi siihen, että matemaattiset muuttujat pitäisi nimetä lähdejulkaisusta poikkeavalla tavalla, ja tämä tekisi koodisti vaikeasti ymmärrettävää. 