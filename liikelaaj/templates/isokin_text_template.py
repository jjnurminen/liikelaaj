# -*- coding: utf-8 -*-
"""
Template for text report (isokinetic data)

This is called by exec() and works by modifying an existing variable
called 'report' (instance of Report class)

The idea is to avoid putting the template code inside a function
call, which would lead to messy indentation.

@author: Jussi (jnu@iki.fi)
"""

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
ISOKINEETTINEN VOIMAMITTAUS
"""

report += u"""
Polven ekstensio, ROM: {IsokinPolviEkstensioOik} / {IsokinPolviEkstensioVas}
Polven fleksio, ROM: {IsokinPolviFleksioOik} / {IsokinPolviFleksioVas}
Polven ekstensiomomentti: {IsokinPolviEkstensioMomenttiOikNormUn} / {IsokinPolviEkstensioMomenttiVasNormUn}
Polven ekstensiomomentti (norm.): {IsokinPolviEkstensioMomenttiOikNorm} / {IsokinPolviEkstensioMomenttiVasNorm}
Polven liikenopeus, ekstensio: {IsokinPolviLiikenopeusEkstensioOik} / {IsokinPolviLiikenopeusEkstensioVas}
Polven fleksiomomentti: {IsokinPolviFleksioMomenttiOikNormUn} / {IsokinPolviFleksioMomenttiVasNormUn}
Polven fleksiomomentti (norm.): {IsokinPolviFleksioMomenttiOikNorm} / {IsokinPolviFleksioMomenttiVasNorm}
Polven liikenopeus, fleksio: {IsokinPolviLiikenopeusFleksioOik} / {IsokinPolviLiikenopeusFleksioVas}
"""

report += u"""
Nilkan plantaarifleksio, ROM: {IsokinNilkkaPlantaarifleksioOik} / {IsokinNilkkaPlantaarifleksioVas}
Nilkan dorsifleksio, ROM: {IsokinNilkkaDorsifleksioOik} / {IsokinNilkkaDorsifleksioVas}
Nilkan plantaarifleksiomomentti: {IsokinNilkkaPlantaarifleksioMomenttiOikNormUn} / {IsokinNilkkaPlantaarifleksioMomenttiVasNormUn}
Nilkan plantaarifleksiomomentti (norm.): {IsokinNilkkaPlantaarifleksioMomenttiOikNorm} / {IsokinNilkkaPlantaarifleksioMomenttiVasNorm}
Nilkan liikenopeus, plantaarifleksio: {IsokinNilkkaLiikenopeusPlantaarifleksioOik} / {IsokinNilkkaLiikenopeusPlantaarifleksioVas}
Nilkan dorsifleksiomomentti: {IsokinNilkkaDorsifleksioMomenttiOikNormUn} / {IsokinNilkkaDorsifleksioMomenttiVasNormUn}
Nilkan dorsifleksiomomentti: {IsokinNilkkaDorsifleksioMomenttiOikNorm} / {IsokinNilkkaDorsifleksioMomenttiVasNorm}
Nilkan liikenopeus, dorsifleksio: {IsokinNilkkaLiikenopeusDorsifleksioOik} / {IsokinNilkkaLiikenopeusDorsifleksioVas}
"""
