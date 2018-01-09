# -*- coding: utf-8 -*-
"""
Template for text report.

This is called by execfile() and works by modifying an existing variable
called 'report' (which needs to exist in function locals as an instance of
Report class)
The idea is to avoid putting the template code inside a function
call, which would lead to messy indentation.

@author: Jussi (jnu@iki.fi)
"""

import liikelaajuus

checkbox_yes = liikelaajuus.Config.checkbox_yestext


def cond_add_text(report, var, text):
    """Return text if yes/no var (checkbox) has the yes value, False
    otherwise"""
    global checkbox_yes
    return text if report.data[var] == checkbox_yes else u''


report += u"""

LIIKELAAJUUDET JA VOIMAT

Patient code: {TiedotID}
Patient name: {TiedotNimi}
Social security number: {TiedotHetu}
Diagnosis: {TiedotDiag}
Date of gait analysis: {TiedotPvm}
"""
report += u'Kommentit: {cmtTiedot}\n'

report += u"""
ANTROPOMETRISET MITAT:
Alaraajat: {AntropAlaraajaOik} / {AntropAlaraajaVas}
Nilkat: {AntropNilkkaOik} / {AntropNilkkaVas}
Polvet: {AntropPolviOik} / {AntropPolviVas}
Paino: {AntropPaino}
Pituus: {AntropPituus}
SIAS: {AntropSIAS}
"""
report += u'Kommentit: {cmtAntrop}\n'

report += u"""
MITTAAJAT:
{TiedotMittaajat}
"""

report += u"""
TULOSYY:


PÄÄTULOKSET KÄVELYANALYYSIN POHJALTA:


TESTAUS- JA ARVIOINTITULOKSET:


OHEISMITTAUSTEN TULOKSET:

"""

report += u"""
Nivelten passiiviset liikelaajuudet (oikea/vasen), NR = normaalin rajoissa:
"""
report += u'Lonkka: '
report += u'Thomasin testi (vapaasti) {LonkkaEkstensioVapOik}/{LonkkaEkstensioVapVas}. '
report += u'Thomasin testi (avustettuna) {LonkkaEkstensioAvOik}/{LonkkaEkstensioAvVas}. '
report += u'Thomasin testi (polvi 90°) {LonkkaEkstensioPolvi90Oik}/{LonkkaEkstensioPolvi90Vas}. ' 
report += u'Koukistus {LonkkaFleksioOik}/{LonkkaFleksioVas}. '
report += u'Loitonnus (lonkka 0°, polvi 90°) {LonkkaAbduktioLonkka0Polvi90Oik}/{LonkkaAbduktioLonkka0Polvi90Vas}. '
report += u'Loitonnus (lonkka 0°, polvi 0°) {LonkkaAbduktioLonkka0Oik}/{LonkkaAbduktioLonkka0Vas}. '
report += u'Loitonnus (lonkka 90°) {LonkkaAbduktioLonkkaFleksOik}/{LonkkaAbduktioLonkkaFleksVas}. '
report += u'Lähennys {LonkkaAdduktioOik}/{LonkkaAdduktioVas}. '
report += u'Sisäkierto {LonkkaSisakiertoOik}/{LonkkaSisakiertoVas}. '
report += u'Ulkokierto {LonkkaUlkokiertoOik}/{LonkkaUlkokiertoVas}. '
report += '\n'
report += u'Kommentit: {cmtLonkkaPROM}\n'
report += '\n'
report += u'Polvi: '
report += u'Ojennus (vapaasti) {PolviEkstensioVapOik}/{PolviEkstensioVapVas}. '
report += u'Ojennus (avustettuna) {PolviEkstensioAvOik}/{PolviEkstensioAvVas}. '
report += u'Koukistus (vatsamakuu) {PolviFleksioVatsamakuuOik}/{PolviFleksioVatsamakuuVas}. '
report += u'Koukistus (selinmakuu) {PolviFleksioSelinmakuuOik}/{PolviFleksioSelinmakuuVas}. '
report += u'Popliteakulma {PolviPopliteaVastakkLonkka0Oik}/{PolviPopliteaVastakkLonkka0Vas}, popliteakulma (true) {PolviPopliteaVastakkLonkka90Oik}/{PolviPopliteaVastakkLonkka90Vas}.'
report += '\n'
report += u'Kommentit: {cmtPolviPROM}\n'
report += '\n'
report += u'Nilkka: '
report += u'Koukistus (polvi 90°) {NilkkaDorsifPolvi90PROMOik}/{NilkkaDorsifPolvi90PROMVas}. '
report += u'Koukistus (polvi 0°) {NilkkaDorsifPolvi0PROMOik}/{NilkkaDorsifPolvi0PROMVas}. '
report += u'Ojennus {NilkkaPlantaarifleksioPROMOik}/{NilkkaPlantaarifleksioPROMVas}.'
report += '\n'
report += u'Kommentit: {cmtNilkkaPROM}\n'

# for 'eversio' extra info and similar things later:
# we have to add item separators in a 'smart' way since we do not know
# which items actually get printed
report += u"""
Nivelten aktiiviset liikelaajuudet: 
"""
report += u'Nilkka: '
report += u'Koukistus (polvi 90°) {NilkkaDorsifPolvi90AROMOik}'
report += cond_add_text(report, 'NilkkaDorsifPolvi90AROMEversioOik', ' (eversio)')
report += u'/{NilkkaDorsifPolvi90AROMVas}'
report += cond_add_text(report, 'NilkkaDorsifPolvi90AROMEversioVas', ' (eversio)')
report.item_sep()
report += u'Koukistus (polvi 0°) {NilkkaDorsifPolvi0AROMOik}/{NilkkaDorsifPolvi0AROMVas}'
report += u' (eversio {NilkkaDorsifPolvi0AROMEversioOik}/{NilkkaDorsifPolvi0AROMEversioVas})'
report.item_sep()
report += u'Ojennus {NilkkaPlantaarifleksioAROMOik}/{NilkkaPlantaarifleksioAROMVas}. '
report += '\n'
report += u'Kommentit: {cmtNilkkaAROM}\n'

report += u"""
Alaraajojen spastisuus:
"""
report += u'Catch: Lonkan adduktorit {LonkkaAdduktoritCatchOik}/{LonkkaAdduktoritCatchVas}. '
report += u'Hamstringit {PolviHamstringCatchOik}/{PolviHamstringCatchVas}. '
report += u'Rectus femorikset {PolviRectusCatchOik}/{PolviRectusCatchVas}. '
report += u'Soleukset {NilkkaSoleusCatchOik}/{NilkkaSoleusCatchVas}'
report += u' (klonus {NilkkaSoleusKlonusOik}/{NilkkaSoleusKlonusVas})'
report.item_sep()
report += u'Gastrocnemiukset {NilkkaGastroCatchOik}/{NilkkaGastroCatchVas}'
report += u' (klonus {NilkkaGastroKlonusOik}/{NilkkaGastroKlonusVas})'
report.item_sep()
report += '\n'
report += u'Kommentit (lonkka): {cmtLonkkaSpast}\n'
report += u'Kommentit (nilkka): {cmtNilkkaSpast}\n'
report += u'Kommentit (polvi): {cmtPolviSpast}\n'

report += u"""
Luiset virheasennot: 
"""
report += u'Lonkan anteversio {VirheasAnteversioOik}/{VirheasAnteversioVas}. '
report += u'Jalkaterä-reisi -kulma {VirheasJalkaReisiOik}/{VirheasJalkaReisiVas}. '
report += u'Jalkaterän etu- takaosan kulma {VirheasJalkateraEtuTakaOik}/{VirheasJalkateraEtuTakaVas}. '
report += u'Bimalleoli -akseli {VirheasBimalleoliOik}/{VirheasBimalleoliVas}. '
report += u'2nd toe test {Virheas2ndtoeOik}/{Virheas2ndtoeVas}. '
report += u'Patella alta {VirheasPatellaAltaOik}/{VirheasPatellaAltaVas}. '
report += u'Polven valgus {PolvenValgusOik}/{PolvenValgusVas}. '
report += u'Q-kulma {QkulmaOik}/{QkulmaVas}.'
report += '\n'
report += u'Kommentit: {cmtVirheas}\n'

report += u"""
Muita mittauksia:
"""
report += u'Alaraajat: {AntropAlaraajaOik} / {AntropAlaraajaVas}. '
report += u'Extensor lag {LonkkaExtLagOik}/{LonkkaExtLagVas}. '
report += u'Confusion test: {NilkkaConfusionOik}/{NilkkaConfusionVas}. '
report += u'Ober test {LonkkaOberOik}/{LonkkaOberVas}. '
report += u'Tasapaino: yhdellä jalalla seisominen {TasapOik}/{TasapVas}. '
report += '\n'
report += u'Kommentit (lonkka): {cmtLonkkaMuut}\n'
report += u'Kommentit (tasapaino): {cmtTasap}\n'

report += u"""
Jalkaterä kuormittamattomana (+ = lievä, ++ = kohtalainen, +++ = voimakas)
Lyhenteet: NEU=neutraali, TYYP=tyypillinen, RAJ=rajoittunut, VAR=varus, VALG=valgus:
"""
report += u'Subtalar neutraali-asento: {JalkatSubtalarOik}/{JalkatSubtalarVas}. '
report += u'Takaosan asento {JalkatTakaosanAsentoOik}/{JalkatTakaosanAsentoVas}. '
report += u'Takaosan liike eversioon {JalkatTakaosanLiikeEversioOik}/{JalkatTakaosanLiikeEversioVas}. '
report += u'Takaosan liike inversioon {JalkatTakaosanLiikeInversioOik}/{JalkatTakaosanLiikeInversioVas}. '
report += u'Med. holvikaari {JalkatHolvikaariOik}/{JalkatHolvikaariVas}. '
report += u'Keskiosan liike {JalkatKeskiosanliikeOik}/{JalkatKeskiosanliikeVas}. '
report += u'Etuosan asento 1: {JalkatEtuosanAsento1Oik}/{JalkatEtuosanAsento1Vas}. '
report += u'Etuosan asento 2: {JalkatEtuosanAsento2Oik}/{JalkatEtuosanAsento2Vas}. '
report += u'1. säde: {Jalkat1sadeOik}/{Jalkat1sadeVas}. '
report += u'1 MTP dorsifleksio {Jalkat1MTPojennusOik}/{Jalkat1MTPojennusVas}. '
report += u'Vaivaisenluu {JalkatVaivaisenluuOik}/{JalkatVaivaisenluuVas}. '
report += u'Kovettumat: {JalkatKovettumatOik}/{JalkatKovettumatVas}.'
report += '\n'
report += u'Kommentit (jalkaterä): {cmtJalkateraKuormittamattomana}\n'

report += u"""
Jalkaterä kuormitettuna: (+ = lievä, ++ = kohtalainen, +++ = voimakas):
"""
report += u'Takaosan (kantaluun) asento {JalkatTakaosanAsentoKuormOik}/{JalkatTakaosanAsentoKuormVas}. '
report += u'Keskiosan asento {JalkatKeskiosanAsentoKuormOik}/{JalkatKeskiosanAsentoKuormVas}. '
report += u'Etuosan asento 1: {JalkatEtuosanAsento1KuormOik}/{JalkatEtuosanAsento1KuormVas}, etuosan asento 2: {JalkatEtuosanAsento2KuormOik}/{JalkatEtuosanAsento2KuormVas}. '
report += u'Takaosan kierto: {JalkatTakaosanKiertoKuormOik}/{JalkatTakaosanKiertoKuormVas}. '
report += u"Coleman's block test: {JalkatColemanOik}/{JalkatColemanVas}. "
report += u'Feissin linja: {JalkatFeissinLinjaOik} / {JalkatFeissinLinjaVas}. '
report += u'Navicular drop, istuen: {JalkatNavDropIstuenOik} / {JalkatNavDropIstuenVas}. '
report += u'Navicular drop, seisten: {JalkatNavDropSeistenOik} / {JalkatNavDropSeistenVas}. '
report += '\n'
report += u'Painelevymittaus: {Painelevy}\n'
report += u'Painelevymittaus, lisätietoja: {JalkatPainelevyTiedot}\n'
report += u'Kommentit (jalkaterä): {cmtJalkateraKuormitettuna}\n'

report += u"""
Modified Ashworth:
"""
report += u'Lonkan koukistajat {LonkkaFleksioModAOik}/{LonkkaFleksioModAVas}. '
report += u'Lonkan ojentajat {LonkkaEkstensioModAOik}/{LonkkaEkstensioModAVas}. '
report += u'Lonkan lähentäjät {LonkkaAdduktoritModAOik}/{LonkkaAdduktoritModAVas}. '
report += u'Hamstringit {PolviHamstringModAOik}/{PolviHamstringModAVas}. '
report += u'Rectus femoris {PolviRectusModAOik}/{PolviRectusModAVas}. '
report += u'Lonkan sisäkierto {LonkkaSisakiertoModAOik}/{LonkkaSisakiertoModAVas}. '
report += u'Lonkan ulkokierto {LonkkaUlkokiertoModAOik}/{LonkkaUlkokiertoModAVas}. '
report += u'Soleus {NilkkaSoleusModAOik}/{NilkkaSoleusModAVas}. '
report += u'Gastrocnemius {NilkkaGastroModAOik}/{NilkkaGastroModAVas}.'
report += '\n'
report += u'Kommentit (lonkka): {cmtLonkkaSpast}\n'

report += u"""
Manuaalisesti mitatut lihasvoimat ja selektiivisyys (oikea lihasvoima/vasen lihasvoima, (oikea selekt./vasen selekt.)):
Asteikko: 0-5, missä 5 on vahvin ja 3 voittaa painovoiman koko potilaan liikelaajuudella.
Selektiivisyys: 0-2, missä 0=kokonaisliikemalli, 1=osittain eriytynyt ja 2=eriytynyt koko liikelaajuudella:
"""
report += u'Lonkan ojennus (polvi 0°) {VoimaLonkkaEkstensioPolvi0Oik}/{VoimaLonkkaEkstensioPolvi0Vas}'
report += u' ({SelLonkkaEkstensioPolvi0Oik}/{SelLonkkaEkstensioPolvi0Vas})'
report.item_sep()
report += u'Lonkan ojennus (polvi 90°) {VoimaLonkkaEkstensioPolvi90Oik}/{VoimaLonkkaEkstensioPolvi90Vas}'
report += u' ({SelLonkkaEkstensioPolvi90Oik}/{SelLonkkaEkstensioPolvi90Vas})'
report.item_sep()
report += u'Lonkan koukistus {VoimaLonkkaFleksioOik}/{VoimaLonkkaFleksioVas}'
report += u' ({SelLonkkaFleksioOik}/{SelLonkkaFleksioVas})'
report.item_sep()
report += u'Loitonnus (lonkka 0°) {VoimaLonkkaAbduktioLonkka0Oik}/{VoimaLonkkaAbduktioLonkka0Vas}'
report += u' ({SelLonkkaAbduktioLonkka0Oik}/{SelLonkkaAbduktioLonkka0Vas})'
report.item_sep()
report += u'Loitonnus, lonkka fleksiossa {VoimaLonkkaAbduktioLonkkaFleksOik}/{VoimaLonkkaAbduktioLonkkaFleksVas}. '
report += u'Lähennys {VoimaLonkkaAdduktioOik}/{VoimaLonkkaAdduktioVas}'
report += u' ({SelLonkkaAdduktioOik}/{SelLonkkaAdduktioVas})'
report.item_sep()
report += u'Lonkan ulkokierto {VoimaLonkkaUlkokiertoOik}/{VoimaLonkkaUlkokiertoVas}'
report += u' ({SelLonkkaUlkokiertoOik}/{SelLonkkaUlkokiertoVas})'
report.item_sep()
report += u'Lonkan sisäkierto {VoimaLonkkaSisakiertoOik}/{VoimaLonkkaSisakiertoVas}'
report += u' ({SelLonkkaSisakiertoOik}/{SelLonkkaSisakiertoVas})'
report.item_sep()
report += u'Polven ojennus {VoimaPolviEkstensioOik}/{VoimaPolviEkstensioVas}'
report += u' ({SelPolviEkstensioOik}/{SelPolviEkstensioVas})'
report.item_sep()
report += u'Polven koukistus {VoimaPolviFleksioOik}/{VoimaPolviFleksioVas}'
report += u' ({SelPolviFleksioOik}/{SelPolviFleksioVas})'
report.item_sep()
report += u'Nilkan koukistus {VoimaTibialisAnteriorOik}/{VoimaTibialisAnteriorVas}'
report += u' ({SelTibialisAnteriorOik}/{SelTibialisAnteriorVas})'
report.item_sep()
report += u'Nilkan ojennus (gastrocnemius) {VoimaGastroOik}/{VoimaGastroVas}'
report += u' ({SelGastroOik}/{SelGastroVas})'
report.item_sep()
report += u'Nilkan ojennus (soleus) {VoimaSoleusOik}/{VoimaSoleusVas}'
report += u' ({SelSoleusOik}/{SelSoleusVas})'
report.item_sep()
report += u'Inversio {VoimaTibialisPosteriorOik}/{VoimaTibialisPosteriorVas}'
report += u' ({SelTibialisPosteriorOik}/{SelTibialisPosteriorVas})'
report.item_sep()
report += u'Eversio {VoimaPeroneusOik}/{VoimaPeroneusVas}'
report += u' ({SelPeroneusOik}/{SelPeroneusVas})'
report.item_sep()
report += u'Isovarpaan ojennus {VoimaExtHallucisLongusOik}/{VoimaExtHallucisLongusVas}'
report += u' ({SelExtHallucisLongusOik}/{SelExtHallucisLongusVas})'
report.item_sep()
report += u'Isovarpaan koukistus {VoimaFlexHallucisLongusOik}/{VoimaFlexHallucisLongusVas}'
report += u' ({SelFlexHallucisLongusOik}/{SelFlexHallucisLongusVas})'
report.item_sep()
report += 'Varpaiden (2-5) ojennus {Voima25OjennusOik}/{Voima25OjennusVas}'
report += u' ({Sel25OjennusOik}/{Sel25OjennusVas})'
report.item_sep()
report += 'Varpaiden (2-5) koukistus {Voima25KoukistusOik}/{Voima25KoukistusVas}'
report += u' ({Sel25KoukistusOik}/{Sel25KoukistusVas})'
report.item_sep()
report += u'Suorat vatsalihakset {VoimaVatsaSuorat}. '
report += u'Vinot vatsalihakset {VoimaVatsaVinotOik}/{VoimaVatsaVinotVas}. '
report += u'Selkälihakset {VoimaSelka}.'
report += '\n'
report += u'Kommentit (voimat): {cmtVoima1} {cmtVoima2} \n'

# some extra logic to add the names of EMG electrodes
emg_chs = {'EMGSol': 'soleus',
           'EMGGas': 'gastrocnemius',
           'EMGPer': 'peroneous',
           'EMGTibA': 'tibialis anterior',
           'EMGRec': 'rectus',
           'EMGHam': 'hamstring',
           'EMGVas': 'vastus',
           'EMGGlut': 'gluteus'}
emgs_in_use = [emg_chs[ch] for ch in emg_chs if
               report.data[ch] == checkbox_yes]
emgs_str = u', '.join(emgs_in_use)
if emgs_str:
    report += u"""
Dynaaminen EMG:
Alaraajojen lihasaktivaatio mitattiin pintaelektrodeilla seuraavista lihaksista:
"""
report += emgs_str
report += '\n'

report += u"""
SUUNNITELMA/POHDINTA:
"""
