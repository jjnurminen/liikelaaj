# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:37:51 2016

@author: jussi
"""

def set_taborder(self):
    """ Set tab focus order. This is set also by the ui file loaded
    above, but needs to be redone because Qt does not handle focus correctly
    for custom (compound) widgets (QTBUG-10907). For custom widgets, the focus proxy
    needs to be explicitly inserted into focus chain. The below code can
    be generated by running:
    pyuic4 tabbed_design.ui | grep TabOrder | sed "s/csb[a-zA-Z0-9]*/&.focusProxy()/g" | sed "s/    MainWindow/self/g" >>fix_taborder.py
    (replaces csb* widget names with csb*.focusProxy() )
    """

    self.setTabOrder(self.lnTiedotNimi, self.lnTiedotPvm)
    self.setTabOrder(self.lnTiedotPvm, self.lnTiedotDiag)
    self.setTabOrder(self.lnTiedotDiag, self.lnTiedotID)
    self.setTabOrder(self.lnTiedotID, self.lnTiedotHetu)
    self.setTabOrder(self.lnTiedotHetu, self.lnTiedotMittaajat)
    self.setTabOrder(self.lnTiedotMittaajat, self.spAntropAlaraajaOik)
    self.setTabOrder(self.spAntropAlaraajaOik, self.spAntropAlaraajaVas)
    self.setTabOrder(self.spAntropAlaraajaVas, self.spAntropPolviOik)
    self.setTabOrder(self.spAntropPolviOik, self.spAntropPolviVas)
    self.setTabOrder(self.spAntropPolviVas, self.spAntropNilkkaOik)
    self.setTabOrder(self.spAntropNilkkaOik, self.spAntropNilkkaVas)
    self.setTabOrder(self.spAntropNilkkaVas, self.spAntropSIAS)
    self.setTabOrder(self.spAntropSIAS, self.spAntropPituus)
    self.setTabOrder(self.spAntropPituus, self.spAntropPaino)
    self.setTabOrder(self.spAntropPaino, self.csbLonkkaFleksioOik.focusProxy())
    self.setTabOrder(self.csbLonkkaFleksioOik.focusProxy(), self.csbLonkkaFleksioVas.focusProxy())
    self.setTabOrder(self.csbLonkkaFleksioVas.focusProxy(), self.cbLonkkaFleksioModAOik)
    self.setTabOrder(self.cbLonkkaFleksioModAOik, self.cbLonkkaFleksioModAVas)
    self.setTabOrder(self.cbLonkkaFleksioModAVas, self.csbLonkkaEkstensioVapOik.focusProxy())
    self.setTabOrder(self.csbLonkkaEkstensioVapOik.focusProxy(), self.csbLonkkaEkstensioAvOik.focusProxy())
    self.setTabOrder(self.csbLonkkaEkstensioAvOik.focusProxy(), self.csbLonkkaEkstensioPolvi90Oik.focusProxy())
    self.setTabOrder(self.csbLonkkaEkstensioPolvi90Oik.focusProxy(), self.csbLonkkaEkstensioVapVas.focusProxy())
    self.setTabOrder(self.csbLonkkaEkstensioVapVas.focusProxy(), self.csbLonkkaEkstensioAvVas.focusProxy())
    self.setTabOrder(self.csbLonkkaEkstensioAvVas.focusProxy(), self.csbLonkkaEkstensioPolvi90Vas.focusProxy())
    self.setTabOrder(self.csbLonkkaEkstensioPolvi90Vas.focusProxy(), self.cbLonkkaEkstensioModAOik)
    self.setTabOrder(self.cbLonkkaEkstensioModAOik, self.cbLonkkaEkstensioModAVas)
    self.setTabOrder(self.cbLonkkaEkstensioModAVas, self.csbLonkkaExtLagOik.focusProxy())
    self.setTabOrder(self.csbLonkkaExtLagOik.focusProxy(), self.csbLonkkaExtLagVas.focusProxy())
    self.setTabOrder(self.csbLonkkaExtLagVas.focusProxy(), self.csbLonkkaAbduktioLonkka0Polvi90Oik.focusProxy())
    self.setTabOrder(self.csbLonkkaAbduktioLonkka0Polvi90Oik.focusProxy(), self.csbLonkkaAbduktioLonkka0Polvi90Vas.focusProxy())
    self.setTabOrder(self.csbLonkkaAbduktioLonkka0Polvi90Vas.focusProxy(), self.csbLonkkaAdduktoritCatchOik.focusProxy())
    self.setTabOrder(self.csbLonkkaAdduktoritCatchOik.focusProxy(), self.csbLonkkaAdduktoritCatchVas.focusProxy())
    self.setTabOrder(self.csbLonkkaAdduktoritCatchVas.focusProxy(), self.csbLonkkaAbduktioLonkka0Oik.focusProxy())
    self.setTabOrder(self.csbLonkkaAbduktioLonkka0Oik.focusProxy(), self.csbLonkkaAbduktioLonkka0Vas.focusProxy())
    self.setTabOrder(self.csbLonkkaAbduktioLonkka0Vas.focusProxy(), self.cbLonkkaAdduktoritModAOik)
    self.setTabOrder(self.cbLonkkaAdduktoritModAOik, self.cbLonkkaAdduktoritModAVas)
    self.setTabOrder(self.cbLonkkaAdduktoritModAVas, self.csbLonkkaAbduktioLonkkaFleksOik.focusProxy())
    self.setTabOrder(self.csbLonkkaAbduktioLonkkaFleksOik.focusProxy(), self.csbLonkkaAbduktioLonkkaFleksVas.focusProxy())
    self.setTabOrder(self.csbLonkkaAbduktioLonkkaFleksVas.focusProxy(), self.csbLonkkaAdduktioOik.focusProxy())
    self.setTabOrder(self.csbLonkkaAdduktioOik.focusProxy(), self.csbLonkkaAdduktioVas.focusProxy())
    self.setTabOrder(self.csbLonkkaAdduktioVas.focusProxy(), self.lnLonkkaOberOik)
    self.setTabOrder(self.lnLonkkaOberOik, self.lnLonkkaOberVas)
    self.setTabOrder(self.lnLonkkaOberVas, self.csbLonkkaSisakiertoOik.focusProxy())
    self.setTabOrder(self.csbLonkkaSisakiertoOik.focusProxy(), self.csbLonkkaSisakiertoVas.focusProxy())
    self.setTabOrder(self.csbLonkkaSisakiertoVas.focusProxy(), self.cbLonkkaSisakiertoModAOik)
    self.setTabOrder(self.cbLonkkaSisakiertoModAOik, self.cbLonkkaSisakiertoModAVas)
    self.setTabOrder(self.cbLonkkaSisakiertoModAVas, self.csbLonkkaUlkokiertoOik.focusProxy())
    self.setTabOrder(self.csbLonkkaUlkokiertoOik.focusProxy(), self.csbLonkkaUlkokiertoVas.focusProxy())
    self.setTabOrder(self.csbLonkkaUlkokiertoVas.focusProxy(), self.cbLonkkaUlkokiertoModAOik)
    self.setTabOrder(self.cbLonkkaUlkokiertoModAOik, self.cbLonkkaUlkokiertoModAVas)
    self.setTabOrder(self.cbLonkkaUlkokiertoModAVas, self.csbPolviEkstensioVapOik.focusProxy())
    self.setTabOrder(self.csbPolviEkstensioVapOik.focusProxy(), self.csbPolviEkstensioAvOik.focusProxy())
    self.setTabOrder(self.csbPolviEkstensioAvOik.focusProxy(), self.csbPolviEkstensioVapVas.focusProxy())
    self.setTabOrder(self.csbPolviEkstensioVapVas.focusProxy(), self.csbPolviEkstensioAvVas.focusProxy())
    self.setTabOrder(self.csbPolviEkstensioAvVas.focusProxy(), self.csbPolviFleksioSelinmakuuOik.focusProxy())
    self.setTabOrder(self.csbPolviFleksioSelinmakuuOik.focusProxy(), self.csbPolviFleksioSelinmakuuVas.focusProxy())
    self.setTabOrder(self.csbPolviFleksioSelinmakuuVas.focusProxy(), self.csbPolviFleksioVatsamakuuOik.focusProxy())
    self.setTabOrder(self.csbPolviFleksioVatsamakuuOik.focusProxy(), self.csbPolviFleksioVatsamakuuVas.focusProxy())
    self.setTabOrder(self.csbPolviFleksioVatsamakuuVas.focusProxy(), self.csbPolviRectusCatchOik.focusProxy())
    self.setTabOrder(self.csbPolviRectusCatchOik.focusProxy(), self.csbPolviRectusCatchVas.focusProxy())
    self.setTabOrder(self.csbPolviRectusCatchVas.focusProxy(), self.cbPolviRectusModAOik)
    self.setTabOrder(self.cbPolviRectusModAOik, self.cbPolviRectusModAVas)
    self.setTabOrder(self.cbPolviRectusModAVas, self.csbPolviHamstringCatchOik.focusProxy())
    self.setTabOrder(self.csbPolviHamstringCatchOik.focusProxy(), self.csbPolviPopliteaVastakkLonkka0Oik.focusProxy())
    self.setTabOrder(self.csbPolviPopliteaVastakkLonkka0Oik.focusProxy(), self.csbPolviPopliteaVastakkLonkka90Oik.focusProxy())
    self.setTabOrder(self.csbPolviPopliteaVastakkLonkka90Oik.focusProxy(), self.csbPolviHamstringCatchVas.focusProxy())
    self.setTabOrder(self.csbPolviHamstringCatchVas.focusProxy(), self.csbPolviPopliteaVastakkLonkka0Vas.focusProxy())
    self.setTabOrder(self.csbPolviPopliteaVastakkLonkka0Vas.focusProxy(), self.csbPolviPopliteaVastakkLonkka90Vas.focusProxy())
    self.setTabOrder(self.csbPolviPopliteaVastakkLonkka90Vas.focusProxy(), self.cbPolviHamstringModAOik)
    self.setTabOrder(self.cbPolviHamstringModAOik, self.cbPolviHamstringModAVas)
    self.setTabOrder(self.cbPolviHamstringModAVas, self.csbNilkkaSoleusCatchOik.focusProxy())
    self.setTabOrder(self.csbNilkkaSoleusCatchOik.focusProxy(), self.xbNilkkaSoleusKlonusOik)
    self.setTabOrder(self.xbNilkkaSoleusKlonusOik, self.csbNilkkaDorsifPolvi90PROMOik.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi90PROMOik.focusProxy(), self.csbNilkkaDorsifPolvi90AROMOik.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi90AROMOik.focusProxy(), self.xbNilkkaDorsifPolvi90AROMEversioOik)
    self.setTabOrder(self.xbNilkkaDorsifPolvi90AROMEversioOik, self.cbNilkkaSoleusModAOik)
    self.setTabOrder(self.cbNilkkaSoleusModAOik, self.csbNilkkaGastroCatchOik.focusProxy())
    self.setTabOrder(self.csbNilkkaGastroCatchOik.focusProxy(), self.xbNilkkaGastroKlonusOik)
    self.setTabOrder(self.xbNilkkaGastroKlonusOik, self.csbNilkkaDorsifPolvi0PROMOik.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi0PROMOik.focusProxy(), self.csbNilkkaDorsifPolvi0AROMOik.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi0AROMOik.focusProxy(), self.xbNilkkaDorsifPolvi0AROMEversioOik)
    self.setTabOrder(self.xbNilkkaDorsifPolvi0AROMEversioOik, self.cbNilkkaGastroModAOik)
    self.setTabOrder(self.cbNilkkaGastroModAOik, self.csbNilkkaPlantaarifleksioPROMOik.focusProxy())
    self.setTabOrder(self.csbNilkkaPlantaarifleksioPROMOik.focusProxy(), self.csbNilkkaPlantaarifleksioAROMOik.focusProxy())
    self.setTabOrder(self.csbNilkkaPlantaarifleksioAROMOik.focusProxy(), self.csbNilkkaSoleusCatchVas.focusProxy())
    self.setTabOrder(self.csbNilkkaSoleusCatchVas.focusProxy(), self.xbNilkkaSoleusKlonusVas)
    self.setTabOrder(self.xbNilkkaSoleusKlonusVas, self.csbNilkkaDorsifPolvi90PROMVas.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi90PROMVas.focusProxy(), self.csbNilkkaDorsifPolvi90AROMVas.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi90AROMVas.focusProxy(), self.xbNilkkaDorsifPolvi90AROMEversioVas)
    self.setTabOrder(self.xbNilkkaDorsifPolvi90AROMEversioVas, self.cbNilkkaSoleusModAVas)
    self.setTabOrder(self.cbNilkkaSoleusModAVas, self.csbNilkkaGastroCatchVas.focusProxy())
    self.setTabOrder(self.csbNilkkaGastroCatchVas.focusProxy(), self.xbNilkkaGastroKlonusVas)
    self.setTabOrder(self.xbNilkkaGastroKlonusVas, self.csbNilkkaDorsifPolvi0PROMVas.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi0PROMVas.focusProxy(), self.csbNilkkaDorsifPolvi0AROMVas.focusProxy())
    self.setTabOrder(self.csbNilkkaDorsifPolvi0AROMVas.focusProxy(), self.xbNilkkaDorsifPolvi0AROMEversioVas)
    self.setTabOrder(self.xbNilkkaDorsifPolvi0AROMEversioVas, self.cbNilkkaGastroModAVas)
    self.setTabOrder(self.cbNilkkaGastroModAVas, self.csbNilkkaPlantaarifleksioPROMVas.focusProxy())
    self.setTabOrder(self.csbNilkkaPlantaarifleksioPROMVas.focusProxy(), self.csbNilkkaPlantaarifleksioAROMVas.focusProxy())
    self.setTabOrder(self.csbNilkkaPlantaarifleksioAROMVas.focusProxy(), self.lnNilkkaConfusionOik)
    self.setTabOrder(self.lnNilkkaConfusionOik, self.lnNilkkaConfusionVas)
    self.setTabOrder(self.lnNilkkaConfusionVas, self.cbJalkatSubtalarOik)
    self.setTabOrder(self.cbJalkatSubtalarOik, self.cbJalkatTakaosanAsentoOik)
    self.setTabOrder(self.cbJalkatTakaosanAsentoOik, self.cbJalkatTakaosanLiikeEversioOik)
    self.setTabOrder(self.cbJalkatTakaosanLiikeEversioOik, self.cbJalkatTakaosanLiikeInversioOik)
    self.setTabOrder(self.cbJalkatTakaosanLiikeInversioOik, self.cbJalkatHolvikaariOik)
    self.setTabOrder(self.cbJalkatHolvikaariOik, self.cbJalkatKeskiosanliikeOik)
    self.setTabOrder(self.cbJalkatKeskiosanliikeOik, self.cbJalkatEtuosanAsento1Oik)
    self.setTabOrder(self.cbJalkatEtuosanAsento1Oik, self.cbJalkatEtuosanAsento2Oik)
    self.setTabOrder(self.cbJalkatEtuosanAsento2Oik, self.cbJalkat1sadeOik)
    self.setTabOrder(self.cbJalkat1sadeOik, self.csbJalkat1MTPojennusOik)
    self.setTabOrder(self.csbJalkat1MTPojennusOik, self.cbJalkatVaivaisenluuOik)
    self.setTabOrder(self.cbJalkatVaivaisenluuOik, self.lnJalkatKovettumatOik)
    self.setTabOrder(self.lnJalkatKovettumatOik, self.cbJalkatSubtalarVas)
    self.setTabOrder(self.cbJalkatSubtalarVas, self.cbJalkatTakaosanAsentoVas)
    self.setTabOrder(self.cbJalkatTakaosanAsentoVas, self.cbJalkatTakaosanLiikeEversioVas)
    self.setTabOrder(self.cbJalkatTakaosanLiikeEversioVas, self.cbJalkatTakaosanLiikeInversioVas)
    self.setTabOrder(self.cbJalkatTakaosanLiikeInversioVas, self.cbJalkatHolvikaariVas)
    self.setTabOrder(self.cbJalkatHolvikaariVas, self.cbJalkatKeskiosanliikeVas)
    self.setTabOrder(self.cbJalkatKeskiosanliikeVas, self.cbJalkatEtuosanAsento1Vas)
    self.setTabOrder(self.cbJalkatEtuosanAsento1Vas, self.cbJalkatEtuosanAsento2Vas)
    self.setTabOrder(self.cbJalkatEtuosanAsento2Vas, self.cbJalkat1sadeVas)
    self.setTabOrder(self.cbJalkat1sadeVas, self.csbJalkat1MTPojennusVas)
    self.setTabOrder(self.csbJalkat1MTPojennusVas, self.cbJalkatVaivaisenluuVas)
    self.setTabOrder(self.cbJalkatVaivaisenluuVas, self.lnJalkatKovettumatVas)
    self.setTabOrder(self.lnJalkatKovettumatVas, self.cbJalkatTakaosanAsentoKuormOik)
    self.setTabOrder(self.cbJalkatTakaosanAsentoKuormOik, self.cbJalkatTakaosanKiertoKuormOik)
    self.setTabOrder(self.cbJalkatTakaosanKiertoKuormOik, self.cbJalkatKeskiosanAsentoKuormOik)
    self.setTabOrder(self.cbJalkatKeskiosanAsentoKuormOik, self.cbJalkatEtuosanAsento1KuormOik)
    self.setTabOrder(self.cbJalkatEtuosanAsento1KuormOik, self.cbJalkatEtuosanAsento2KuormOik)
    self.setTabOrder(self.cbJalkatEtuosanAsento2KuormOik, self.cbJalkatFeissinLinjaOik)
    self.setTabOrder(self.cbJalkatFeissinLinjaOik, self.lnJalkatColemanOik)
    self.setTabOrder(self.lnJalkatColemanOik, self.xbPainelevy)
    self.setTabOrder(self.xbPainelevy, self.cbJalkatTakaosanAsentoKuormVas)
    self.setTabOrder(self.cbJalkatTakaosanAsentoKuormVas, self.cbJalkatTakaosanKiertoKuormVas)
    self.setTabOrder(self.cbJalkatTakaosanKiertoKuormVas, self.cbJalkatKeskiosanAsentoKuormVas)
    self.setTabOrder(self.cbJalkatKeskiosanAsentoKuormVas, self.cbJalkatEtuosanAsento1KuormVas)
    self.setTabOrder(self.cbJalkatEtuosanAsento1KuormVas, self.cbJalkatEtuosanAsento2KuormVas)
    self.setTabOrder(self.cbJalkatEtuosanAsento2KuormVas, self.cbJalkatFeissinLinjaVas)
    self.setTabOrder(self.cbJalkatFeissinLinjaVas, self.lnJalkatColemanVas)
    self.setTabOrder(self.lnJalkatColemanVas, self.cbVoimaLonkkaEkstensioPolvi0Oik)
    self.setTabOrder(self.cbVoimaLonkkaEkstensioPolvi0Oik, self.cbVoimaLonkkaEkstensioPolvi0Vas)
    self.setTabOrder(self.cbVoimaLonkkaEkstensioPolvi0Vas, self.cbSelLonkkaEkstensioPolvi0Oik)
    self.setTabOrder(self.cbSelLonkkaEkstensioPolvi0Oik, self.cbSelLonkkaEkstensioPolvi0Vas)
    self.setTabOrder(self.cbSelLonkkaEkstensioPolvi0Vas, self.cbVoimaLonkkaEkstensioPolvi90Oik)
    self.setTabOrder(self.cbVoimaLonkkaEkstensioPolvi90Oik, self.cbVoimaLonkkaEkstensioPolvi90Vas)
    self.setTabOrder(self.cbVoimaLonkkaEkstensioPolvi90Vas, self.cbSelLonkkaEkstensioPolvi90Oik)
    self.setTabOrder(self.cbSelLonkkaEkstensioPolvi90Oik, self.cbSelLonkkaEkstensioPolvi90Vas)
    self.setTabOrder(self.cbSelLonkkaEkstensioPolvi90Vas, self.cbVoimaPolviFleksioOik)
    self.setTabOrder(self.cbVoimaPolviFleksioOik, self.cbVoimaPolviFleksioVas)
    self.setTabOrder(self.cbVoimaPolviFleksioVas, self.cbSelPolviFleksioOik)
    self.setTabOrder(self.cbSelPolviFleksioOik, self.cbSelPolviFleksioVas)
    self.setTabOrder(self.cbSelPolviFleksioVas, self.cbVoimaLonkkaAbduktioLonkka0Oik)
    self.setTabOrder(self.cbVoimaLonkkaAbduktioLonkka0Oik, self.cbVoimaLonkkaAbduktioLonkka0Vas)
    self.setTabOrder(self.cbVoimaLonkkaAbduktioLonkka0Vas, self.cbSelLonkkaAbduktioLonkka0Oik)
    self.setTabOrder(self.cbSelLonkkaAbduktioLonkka0Oik, self.cbSelLonkkaAbduktioLonkka0Vas)
    self.setTabOrder(self.cbSelLonkkaAbduktioLonkka0Vas, self.cbVoimaLonkkaAbduktioLonkkaFleksOik)
    self.setTabOrder(self.cbVoimaLonkkaAbduktioLonkkaFleksOik, self.cbVoimaLonkkaAbduktioLonkkaFleksVas)
    self.setTabOrder(self.cbVoimaLonkkaAbduktioLonkkaFleksVas, self.cbVoimaLonkkaAdduktioOik)
    self.setTabOrder(self.cbVoimaLonkkaAdduktioOik, self.cbVoimaLonkkaAdduktioVas)
    self.setTabOrder(self.cbVoimaLonkkaAdduktioVas, self.cbSelLonkkaAdduktioOik)
    self.setTabOrder(self.cbSelLonkkaAdduktioOik, self.cbSelLonkkaAdduktioVas)
    self.setTabOrder(self.cbSelLonkkaAdduktioVas, self.cbVoimaSelka)
    self.setTabOrder(self.cbVoimaSelka, self.cbVoimaVatsaSuorat)
    self.setTabOrder(self.cbVoimaVatsaSuorat, self.cbVoimaVatsaVinotOik)
    self.setTabOrder(self.cbVoimaVatsaVinotOik, self.cbVoimaVatsaVinotVas)
    self.setTabOrder(self.cbVoimaVatsaVinotVas, self.cbVoimaLonkkaFleksioOik)
    self.setTabOrder(self.cbVoimaLonkkaFleksioOik, self.cbVoimaLonkkaFleksioVas)
    self.setTabOrder(self.cbVoimaLonkkaFleksioVas, self.cbSelLonkkaFleksioOik)
    self.setTabOrder(self.cbSelLonkkaFleksioOik, self.cbSelLonkkaFleksioVas)
    self.setTabOrder(self.cbSelLonkkaFleksioVas, self.cbVoimaPolviEkstensioOik)
    self.setTabOrder(self.cbVoimaPolviEkstensioOik, self.cbVoimaPolviEkstensioVas)
    self.setTabOrder(self.cbVoimaPolviEkstensioVas, self.cbSelPolviEkstensioOik)
    self.setTabOrder(self.cbSelPolviEkstensioOik, self.cbSelPolviEkstensioVas)
    self.setTabOrder(self.cbSelPolviEkstensioVas, self.cbVoimaLonkkaUlkokiertoOik)
    self.setTabOrder(self.cbVoimaLonkkaUlkokiertoOik, self.cbVoimaLonkkaUlkokiertoVas)
    self.setTabOrder(self.cbVoimaLonkkaUlkokiertoVas, self.cbSelLonkkaUlkokiertoOik)
    self.setTabOrder(self.cbSelLonkkaUlkokiertoOik, self.cbSelLonkkaUlkokiertoVas)
    self.setTabOrder(self.cbSelLonkkaUlkokiertoVas, self.cbVoimaLonkkaSisakiertoOik)
    self.setTabOrder(self.cbVoimaLonkkaSisakiertoOik, self.cbVoimaLonkkaSisakiertoVas)
    self.setTabOrder(self.cbVoimaLonkkaSisakiertoVas, self.cbSelLonkkaSisakiertoOik)
    self.setTabOrder(self.cbSelLonkkaSisakiertoOik, self.cbSelLonkkaSisakiertoVas)
    self.setTabOrder(self.cbSelLonkkaSisakiertoVas, self.cbVoimaTibialisAnteriorOik)
    self.setTabOrder(self.cbVoimaTibialisAnteriorOik, self.cbVoimaTibialisAnteriorVas)
    self.setTabOrder(self.cbVoimaTibialisAnteriorVas, self.cbSelTibialisAnteriorOik)
    self.setTabOrder(self.cbSelTibialisAnteriorOik, self.cbSelTibialisAnteriorVas)
    self.setTabOrder(self.cbSelTibialisAnteriorVas, self.cbVoimaTibialisPosteriorOik)
    self.setTabOrder(self.cbVoimaTibialisPosteriorOik, self.cbVoimaTibialisPosteriorVas)
    self.setTabOrder(self.cbVoimaTibialisPosteriorVas, self.cbSelTibialisPosteriorOik)
    self.setTabOrder(self.cbSelTibialisPosteriorOik, self.cbSelTibialisPosteriorVas)
    self.setTabOrder(self.cbSelTibialisPosteriorVas, self.cbVoimaPeroneusOik)
    self.setTabOrder(self.cbVoimaPeroneusOik, self.cbVoimaPeroneusVas)
    self.setTabOrder(self.cbVoimaPeroneusVas, self.cbSelPeroneusOik)
    self.setTabOrder(self.cbSelPeroneusOik, self.cbSelPeroneusVas)
    self.setTabOrder(self.cbSelPeroneusVas, self.cbVoimaExtHallucisLongusOik)
    self.setTabOrder(self.cbVoimaExtHallucisLongusOik, self.cbVoimaExtHallucisLongusVas)
    self.setTabOrder(self.cbVoimaExtHallucisLongusVas, self.cbSelExtHallucisLongusOik)
    self.setTabOrder(self.cbSelExtHallucisLongusOik, self.cbSelExtHallucisLongusVas)
    self.setTabOrder(self.cbSelExtHallucisLongusVas, self.cbVoimaFlexHallucisLongusOik)
    self.setTabOrder(self.cbVoimaFlexHallucisLongusOik, self.cbVoimaFlexHallucisLongusVas)
    self.setTabOrder(self.cbVoimaFlexHallucisLongusVas, self.cbSelFlexHallucisLongusOik)
    self.setTabOrder(self.cbSelFlexHallucisLongusOik, self.cbSelFlexHallucisLongusVas)
    self.setTabOrder(self.cbSelFlexHallucisLongusVas, self.cbVoima25OjennusOik)
    self.setTabOrder(self.cbVoima25OjennusOik, self.cbVoima25OjennusVas)
    self.setTabOrder(self.cbVoima25OjennusVas, self.cbSel25OjennusOik)
    self.setTabOrder(self.cbSel25OjennusOik, self.cbSel25OjennusVas)
    self.setTabOrder(self.cbSel25OjennusVas, self.cbVoima25KoukistusOik)
    self.setTabOrder(self.cbVoima25KoukistusOik, self.cbVoima25KoukistusVas)
    self.setTabOrder(self.cbVoima25KoukistusVas, self.cbSel25KoukistusOik)
    self.setTabOrder(self.cbSel25KoukistusOik, self.cbSel25KoukistusVas)
    self.setTabOrder(self.cbSel25KoukistusVas, self.cbVoimaGastroOik)
    self.setTabOrder(self.cbVoimaGastroOik, self.cbVoimaGastroVas)
    self.setTabOrder(self.cbVoimaGastroVas, self.cbSelGastroOik)
    self.setTabOrder(self.cbSelGastroOik, self.cbSelGastroVas)
    self.setTabOrder(self.cbSelGastroVas, self.cbVoimaSoleusOik)
    self.setTabOrder(self.cbVoimaSoleusOik, self.cbVoimaSoleusVas)
    self.setTabOrder(self.cbVoimaSoleusVas, self.cbSelSoleusOik)
    self.setTabOrder(self.cbSelSoleusOik, self.cbSelSoleusVas)
    self.setTabOrder(self.cbSelSoleusVas, self.spVirheasAnteversioOik)
    self.setTabOrder(self.spVirheasAnteversioOik, self.spVirheasAnteversioVas)
    self.setTabOrder(self.spVirheasAnteversioVas, self.spVirheasPatellaAltaOik)
    self.setTabOrder(self.spVirheasPatellaAltaOik, self.spVirheasPatellaAltaVas)
    self.setTabOrder(self.spVirheasPatellaAltaVas, self.lnPolvenValgusOik)
    self.setTabOrder(self.lnPolvenValgusOik, self.lnPolvenValgusVas)
    self.setTabOrder(self.lnPolvenValgusVas, self.spQkulmaOik)
    self.setTabOrder(self.spQkulmaOik, self.spQkulmaVas)
    self.setTabOrder(self.spQkulmaVas, self.spVirheasJalkaReisiOik)
    self.setTabOrder(self.spVirheasJalkaReisiOik, self.spVirheasJalkaReisiVas)
    self.setTabOrder(self.spVirheasJalkaReisiVas, self.spVirheasJalkateraEtuTakaOik)
    self.setTabOrder(self.spVirheasJalkateraEtuTakaOik, self.spVirheasJalkateraEtuTakaVas)
    self.setTabOrder(self.spVirheasJalkateraEtuTakaVas, self.spVirheasBimalleoliOik)
    self.setTabOrder(self.spVirheasBimalleoliOik, self.spVirheasBimalleoliVas)
    self.setTabOrder(self.spVirheasBimalleoliVas, self.spVirheas2ndtoeOik)
    self.setTabOrder(self.spVirheas2ndtoeOik, self.spVirheas2ndtoeVas)
    self.setTabOrder(self.spVirheas2ndtoeVas, self.spTasapOik)
    self.setTabOrder(self.spTasapOik, self.spTasapVas)
    self.setTabOrder(self.spTasapVas, self.maintab)
    self.setTabOrder(self.maintab, self.cmtTiedot)
    self.setTabOrder(self.cmtTiedot, self.cmtAntrop)
    self.setTabOrder(self.cmtAntrop, self.cmtLonkkaSpast)
    self.setTabOrder(self.cmtLonkkaSpast, self.cmtLonkkaPROM)
    self.setTabOrder(self.cmtLonkkaPROM, self.cmtLonkkaMuut)
    self.setTabOrder(self.cmtLonkkaMuut, self.cmtPolviSpast)
    self.setTabOrder(self.cmtPolviSpast, self.cmtPolviPROM)
    self.setTabOrder(self.cmtPolviPROM, self.cmtNilkkaSpast)
    self.setTabOrder(self.cmtNilkkaSpast, self.cmtNilkkaAROM)
    self.setTabOrder(self.cmtNilkkaAROM, self.cmtNilkkaPROM)
    self.setTabOrder(self.cmtNilkkaPROM, self.cmtJalkateraKuormittamattomana)
    self.setTabOrder(self.cmtJalkateraKuormittamattomana, self.cmtJalkateraKuormitettuna)
    self.setTabOrder(self.cmtJalkateraKuormitettuna, self.cmtVoima1)
    self.setTabOrder(self.cmtVoima1, self.cmtVoima2)
    self.setTabOrder(self.cmtVoima2, self.cmtVirheas)
    self.setTabOrder(self.cmtVirheas, self.cmtTasap)
    self.setTabOrder(self.cmtTasap, self.btnSave)
    self.setTabOrder(self.btnSave, self.btnLoad)
    self.setTabOrder(self.btnLoad, self.btnClear)
    self.setTabOrder(self.btnClear, self.btnReport)
    self.setTabOrder(self.btnReport, self.btnHelp)
    self.setTabOrder(self.btnHelp, self.btnQuit)
