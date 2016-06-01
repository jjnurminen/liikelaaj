# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 12:37:26 2016

Template for liikelaajuus report.

Report text is delimited into sections. If a section has fields (variables), 
at least one of them must have corresponding data, otherwise the section 
will not be printed. Sections without variables are always printed.

@author: jussi (jnu@iki.fi)
"""


# section delimiter
delimiter = '#' 

# raw report text
report_ = u"""

LIIKELAAJUUDET JA VOIMAT

#Patient code: {TiedotID}
Patient name: {TiedotNimi}
Social security number: {TiedotHetu}
Diagnosis: {TiedotDiag}
Date of gait analysis: {TiedotPvm} 
#Kommentit: {cmtTiedot}#

ANTROPOMETRISET MITAT:
Alaraajat: {AntropAlaraajaOik} / {AntropAlaraajaVas}
Nilkat: {AntropNilkkaOik} / {AntropNilkkaVas}
Polvet: {AntropPolviOik} / {AntropPolviVas}
Paino: {AntropPaino}
Pituus: {AntropPituus}
SIAS: {AntropSIAS}
#Kommentit: {cmtAntrop}#

#MITTAAJAT:
{TiedotMittaajat}#


TULOSYY:


PÄÄTULOKSET KÄVELYANALYYSIN POHJALTA:


TESTAUS- JA ARVIOINTITULOKSET:



OHEISMITTAUSTEN TULOKSET:

Nivelten passiiviset liikelaajuudet (oikea/vasen), NR = normaalin rajoissa:
Lonkka: #Thomasin testi (vapaasti) {LonkkaEkstensioVapOik}/{LonkkaEkstensioVapVas}. #Thomasin testi (avustettuna) {LonkkaEkstensioAvOik}/{LonkkaEkstensioAvVas}. #Thomasin testi (polvi 90°) {LonkkaEkstensioPolvi90Oik}/{LonkkaEkstensioPolvi90Vas}.#
#Koukistus {LonkkaFleksioOik}/{LonkkaFleksioVas}. #Loitonnus (lonkka 0°, polvi 90°) {LonkkaAbduktioLonkka0Polvi90Oik}/{LonkkaAbduktioLonkka0Polvi90Vas}. #Loitonnus (lonkka 0°, polvi 0°) {LonkkaAbduktioLonkka0Oik}/{LonkkaAbduktioLonkka0Vas}. #
#Loitonnus (lonkka 90°) {LonkkaAbduktioLonkkaFleksOik}/{LonkkaAbduktioLonkkaFleksVas}. #Lähennys {LonkkaAdduktioOik}/{LonkkaAdduktioVas}. #Sisäkierto {LonkkaSisakiertoOik}/{LonkkaSisakiertoVas}. #Ulkokierto {LonkkaUlkokiertoOik}/{LonkkaUlkokiertoVas}. # 
#Kommentit: {cmtLonkkaPROM}#
Polvi: #Ojennus (vapaasti) {PolviEkstensioVapOik}/{PolviEkstensioVapVas}. #Ojennus (avustettuna) {PolviEkstensioAvOik}/{PolviEkstensioAvVas}. #Koukistus (vatsamakuu) {PolviFleksioVatsamakuuOik}/{PolviFleksioVatsamakuuVas}. #
#Koukistus (selinmakuu) {PolviFleksioSelinmakuuOik}/{PolviFleksioSelinmakuuVas}. #Popliteakulma {PolviPopliteaVastakkLonkka0Oik}/{PolviPopliteaVastakkLonkka0Vas}, popliteakulma (true) {PolviPopliteaVastakkLonkka90Oik}/{PolviPopliteaVastakkLonkka90Vas}. # 
#Kommentit: {cmtPolviPROM}#
Nilkka: #Koukistus (polvi 90°) {NilkkaDorsifPolvi90PROMOik}/{NilkkaDorsifPolvi90PROMVas}. #Koukistus (polvi 0°) {NilkkaDorsifPolvi0PROMOik}/{NilkkaDorsifPolvi0PROMVas}. #Ojennus {NilkkaPlantaarifleksioPROMOik}/{NilkkaPlantaarifleksioPROMVas}. #
#Kommentit: {cmtNilkkaPROM}#

Nivelten aktiiviset liikelaajuudet: 
Nilkka: #Koukistus (polvi 90°) {NilkkaDorsifPolvi90AROMOik}/{NilkkaDorsifPolvi90AROMVas}. #\b\b (eversio {NilkkaDorsifPolvi90AROMEversioOik}/{NilkkaDorsifPolvi90AROMEversioVas}). #Koukistus (polvi 0°) {NilkkaDorsifPolvi0AROMOik}/{NilkkaDorsifPolvi0AROMVas}. #\b\b (eversio {NilkkaDorsifPolvi0AROMEversioOik}/{NilkkaDorsifPolvi0AROMEversioVas}). #Ojennus {NilkkaPlantaarifleksioAROMOik}/{NilkkaPlantaarifleksioAROMVas}. #
#Kommentit: {cmtNilkkaAROM}#

Luiset virheasennot: 
#Lonkan anteversio {VirheasAnteversioOik}/{VirheasAnteversioVas}. #Jalkaterä-reisi -kulma {VirheasJalkaReisiOik}/{VirheasJalkaReisiVas}. #Jalkaterän etu- takaosan kulma {VirheasJalkateraEtuTakaOik}/{VirheasJalkateraEtuTakaVas}. #
#Bimalleoli -akseli {VirheasBimalleoliOik}/{VirheasBimalleoliVas}. #2nd toe test {Virheas2ndtoeOik}/{Virheas2ndtoeVas}. #Patella alta {VirheasPatellaAltaOik}/{VirheasPatellaAltaVas}. #Polven valgus {PolvenValgusOik}/{PolvenValgusVas}. #Q-kulma {QkulmaOik}/{QkulmaVas}. #
#Kommentit: {cmtVirheas}#

Muita mittauksia:
#Extensor lag {LonkkaExtLagOik}/{LonkkaExtLagVas}. #Confusion test: {NilkkaConfusionOik}/{NilkkaConfusionVas}. #Ober test {LonkkaOberOik}/{LonkkaOberVas}. #Tasapaino: yhdellä jalalla seisominen {TasapOik}/{TasapVas}. #
#Kommentit (lonkka): {cmtLonkkaMuut}
#Kommentit (tasapaino): {cmtTasap}#

Jalkaterä kuormittamattomana (+ = lievä, ++ = kohtalainen, +++ = voimakas): 
#Subtalar neutraali-asento: {JalkatSubtalarOik}/{JalkatSubtalarVas}. #Takaosan asento {JalkatTakaosanAsentoOik}/{JalkatTakaosanAsentoVas}. #Takaosan liike eversioon {JalkatTakaosanLiikeEversioOik}/{JalkatTakaosanLiikeEversioVas}. #
#Takaosan liike inversioon {JalkatTakaosanLiikeInversioOik}/{JalkatTakaosanLiikeInversioVas}. #Med. holvikaari {JalkatHolvikaariOik}/{JalkatHolvikaariVas}. #Keskiosan liike {JalkatKeskiosanliikeOik}/{JalkatKeskiosanliikeVas}. #Etuosan asento 1: {JalkatEtuosanAsento1Oik}/{JalkatEtuosanAsento1Vas}. #  
#Etuosan asento 2: {JalkatEtuosanAsento2Oik}/{JalkatEtuosanAsento2Vas}. #1. säde: {Jalkat1sadeOik}/{Jalkat1sadeVas}. #1 MTP dorsifleksio {Jalkat1MTPojennusOik}/{Jalkat1MTPojennusVas}. #Vaivaisenluu {JalkatVaivaisenluuOik}/{JalkatVaivaisenluuVas}. #
#Kovettumat: {JalkatKovettumatOik}/{JalkatKovettumatVas}. #
#Kommentit (jalkaterä): {cmtJalkateraKuormittamattomana}#

Jalkaterä kuormitettuna: (+ = lievä, ++ = kohtalainen, +++ = voimakas):
#Takaosan (kantaluun) asento {JalkatTakaosanAsentoKuormOik}/{JalkatTakaosanAsentoKuormVas}. #Keskiosan asento {JalkatKeskiosanAsentoKuormOik}/{JalkatKeskiosanAsentoKuormVas}. #Etuosan asento 1: {JalkatEtuosanAsento1KuormOik}/{JalkatEtuosanAsento1KuormVas}, etuosan asento 2: {JalkatEtuosanAsento2KuormOik}/{JalkatEtuosanAsento2KuormVas}. #
#Takaosan kierto {JalkatTakaosanKiertoKuormOik}/{JalkatTakaosanKiertoKuormVas}. #Coleman's block test: {JalkatColemanOik}/{JalkatColemanVas}. #Feissin linja: {JalkatFeissinLinjaOik} / {JalkatFeissinLinjaVas}. #
#Painelevy mitattu: {Painelevy}#
#Kommentit (jalkaterä): {cmtJalkateraKuormitettuna}#

Alaraajojen spastisuus:
Catch: #Lonkan adduktorit {LonkkaAdduktoritCatchOik}/{LonkkaAdduktoritCatchVas}. #Hamstringit {PolviHamstringCatchOik}/{PolviHamstringCatchVas}. #Rectus femorikset {PolviRectusCatchOik}/{PolviRectusCatchVas}. #Soleukset {NilkkaSoleusCatchOik}/{NilkkaSoleusCatchVas}. #\b\b (klonus {NilkkaSoleusKlonusOik}/{NilkkaSoleusKlonusVas}). #
#Gastrocnemiukset {NilkkaGastroCatchOik}/{NilkkaGastroCatchVas}. #\b\b (klonus {NilkkaGastroKlonusOik}/{NilkkaGastroKlonusVas}). #
#Kommentit (lonkka): {cmtLonkkaSpast}#
#Kommentit (nilkka): {cmtNilkkaSpast}#
#Kommentit (polvi): {cmtPolviSpast}#

Modified Ashworth: #Lonkan koukistajat {LonkkaFleksioModAOik}/{LonkkaFleksioModAVas}. #Lonkan ojentajat {LonkkaEkstensioModAOik}/{LonkkaEkstensioModAVas}. #Lonkan lähentäjät {LonkkaAdduktoritModAOik}/{LonkkaAdduktoritModAVas}. #Hamstringit {PolviHamstringModAOik}/{PolviHamstringModAVas}. #
#Rectus femoris {PolviRectusModAOik}/{PolviRectusModAVas}. #Lonkan sisäkierto {LonkkaSisakiertoModAOik}/{LonkkaSisakiertoModAVas}. #Lonkan ulkokierto {LonkkaUlkokiertoModAOik}/{LonkkaUlkokiertoModAVas}. #Soleus {NilkkaSoleusModAOik}/{NilkkaSoleusModAVas}. #Gastrocnemius {NilkkaGastroModAOik}/{NilkkaGastroModAVas}. #
Kommentit:

Manuaalisesti mitatut lihasvoimat ja selektiivisyys (oikea lihasvoima/vasen lihasvoima, (oikea selekt./vasen selekt.)):
Asteikko: 0-5, missä 5 on vahvin ja 3 voittaa painovoiman. Selektiivisyys, missä 
0=kokonaisliikemalli, 1=osittain eriytynyt ja 2=eriytynyt koko liikelaajuudella:  
#Lonkan ojennus (polvi 0°) {VoimaLonkkaEkstensioPolvi0Oik}/{VoimaLonkkaEkstensioPolvi0Vas}. #\b\b ({SelLonkkaEkstensioPolvi0Oik}/{SelLonkkaEkstensioPolvi0Vas}). #Lonkan ojennus (polvi 90°) {VoimaLonkkaEkstensioPolvi90Oik}/{VoimaLonkkaEkstensioPolvi90Vas}. #\b\b ({SelLonkkaEkstensioPolvi90Oik}/{SelLonkkaEkstensioPolvi90Vas}). #Lonkan koukistus {VoimaLonkkaFleksioOik}/{VoimaLonkkaFleksioVas}. #\b\b ({SelLonkkaFleksioOik}/{SelLonkkaFleksioVas}). #Loitonnus (lonkka 0°) {VoimaLonkkaAbduktioLonkka0Oik}/{VoimaLonkkaAbduktioLonkka0Vas}. #\b\b ({SelLonkkaAbduktioLonkka0Oik}/{SelLonkkaAbduktioLonkka0Vas}).#
#Loitonnus, lonkka fleksiossa {VoimaLonkkaAbduktioLonkkaFleksOik}/{VoimaLonkkaAbduktioLonkkaFleksVas}. #Lähennys {VoimaLonkkaAdduktioOik}/{VoimaLonkkaAdduktioVas}. #\b\b ({SelLonkkaAdduktioOik}/{SelLonkkaAdduktioVas}). #Lonkan ulkokierto {VoimaLonkkaUlkokiertoOik}/{VoimaLonkkaUlkokiertoVas}. #\b\b ({SelLonkkaUlkokiertoOik}/{SelLonkkaUlkokiertoVas}).#
#Lonkan sisäkierto {VoimaLonkkaSisakiertoOik}/{VoimaLonkkaSisakiertoVas}. #\b\b ({SelLonkkaSisakiertoOik}/{SelLonkkaSisakiertoVas}). #Polven ojennus {VoimaPolviEkstensioOik}/{VoimaPolviEkstensioVas}. #\b\b ({SelPolviEkstensioOik}/{SelPolviEkstensioVas}). #Polven koukistus {VoimaPolviFleksioOik}/{VoimaPolviFleksioVas}. #\b\b ({SelPolviFleksioOik}/{SelPolviFleksioVas}). #Nilkan koukistus {VoimaTibialisAnteriorOik}/{VoimaTibialisAnteriorVas}. #\b\b ({SelTibialisAnteriorOik}/{SelTibialisAnteriorVas}).#
#Nilkan ojennus (gastrocnemius) {VoimaGastroOik}/{VoimaGastroVas}. #\b\b ({SelGastroOik}/{SelGastroVas}). #Nilkan ojennus (soleus) {VoimaSoleusOik}/{VoimaSoleusVas}. #\b\b ({SelSoleusOik}/{SelSoleusVas}).#
#Inversio {VoimaTibialisPosteriorOik}/{VoimaTibialisPosteriorVas}. #\b\b ({SelTibialisPosteriorOik}/{SelTibialisPosteriorVas}). #Eversio {VoimaPeroneusOik}/{VoimaPeroneusVas}. #\b\b({SelPeroneusOik}/{SelPeroneusVas}). #Isovarpaan ojennus {VoimaExtHallucisLongusOik}/{VoimaExtHallucisLongusVas}. #\b\b ({SelExtHallucisLongusOik}/{SelExtHallucisLongusVas}).#
#Isovarpaan koukistus {VoimaFlexHallucisLongusOik}/{VoimaFlexHallucisLongusVas}. #\b\b ({SelFlexHallucisLongusOik}/{SelFlexHallucisLongusVas}). #Varpaiden (2-5) ojennus {Voima25OjennusOik}/{Voima25OjennusVas}. #\b\b ({Sel25OjennusOik}{Sel25OjennusVas}).#
#Varpaiden (2-5) koukistus {Voima25KoukistusOik}/{Voima25KoukistusVas}. #\b\b ({Sel25KoukistusOik}/{Sel25KoukistusVas}). #Suorat vatsalihakset {VoimaVatsaSuorat}. #Vinot vatsalihakset {VoimaVatsaVinotOik}/{VoimaVatsaVinotVas}. #Selkälihakset {VoimaSelka}.# 
#Kommentit (voimat): {cmtVoima1}
{cmtVoima2}#

Dynaaminen EMG:
Alaraajojen lihasaktivaatio mitattiin pintaelektrodeilla seuraavista lihaksista: soleus, gastrocnemius, peroneus, tibialis anterior, rectus, med hamstring, vastus, gluteus.
Kommentit:


SUUNNITELMA/POHDINTA:





, fysioterapeutti
Liikelaboratorio
HYKS, Lastenlinna

Jakelu:

Kotiin 2kpl, joista toinen kuntouttavalle fysioterapeutille.
.LL14
"""


report = report_.split(delimiter)

