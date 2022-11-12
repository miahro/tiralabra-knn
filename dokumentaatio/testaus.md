# Testausdokumentti

## Yksikkötestaus
- luokalle DirectedHausdorff toteutettu yksikkötestit
    - testitapauksena käytetty modulissa testcases.py määriteltyä pistejoukkoa. Ko joukolle laskettu suunnatut Hausdorffin etäisyydet manuaalisesti taulukkolaskennassa, joita käytetään vertailuarvoina.
- luokalle UndirectedHausdorff toteutettu yksikkötestit
    - testitapauksena sama pistejoukko kuin luokalle DirectedHausdorff, ja vertailuarvoina myös manuaalisesti taulukkolaskennassa lasketut arvot
- luokalle Mnistrawdata toteutetty yksikkötestit
    - testataan lähinnä, että kaikki data luetaan (oikea määrä datapisteitä), ja että arvot ovat oikealla välillä

## Testikattavuus
- [Testikattavuusraportti](dokumentaatio/TestCoverageReport.png)

## Koodin laadunseuranta
- toteutuille luokille pylint arvio 10.00/10
- .pylintrc :ssä disabloitu virhe C0103 "invalid name", snake_case konvention noudattaminen johtaisi siihen, että matemaattiset muuttujat pitäisi nimetä lähdejulkaisusta poikkeavalla tavalla, ja tämä tekisi koodisti vaikeasti ymmärrettävää. 