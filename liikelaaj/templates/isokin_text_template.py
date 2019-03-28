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
Polven ekstensio, ROM: {IsokinPolviEkstensioOik} / {IsokinPolviEkstensioVas} °
Polven fleksio, ROM: {IsokinPolviFleksioOik} / {IsokinPolviFleksioVas} °
Polven ekstensiomomentti: {IsokinPolviEkstensioMomenttiOikNormUn} / {IsokinPolviEkstensioMomenttiVasNormUn} Nm
Polven ekstensiomomentti (norm.): {IsokinPolviEkstensioMomenttiOikNorm} / {IsokinPolviEkstensioMomenttiVasNorm} Nm/kg
Polven liikenopeus, ekstensio: {IsokinPolviLiikenopeusEkstensioOik} / {IsokinPolviLiikenopeusEkstensioVas} °/s
Polven fleksiomomentti: {IsokinPolviFleksioMomenttiOikNormUn} / {IsokinPolviFleksioMomenttiVasNormUn} Nm
Polven fleksiomomentti (norm.): {IsokinPolviFleksioMomenttiOikNorm} / {IsokinPolviFleksioMomenttiVasNorm} Nm/kg
Polven liikenopeus, fleksio: {IsokinPolviLiikenopeusFleksioOik} / {IsokinPolviLiikenopeusFleksioVas} °/s
"""

report += u"""
Nilkan plantaarifleksio, ROM: {IsokinNilkkaPlantaarifleksioOik} / {IsokinNilkkaPlantaarifleksioVas} °
Nilkan dorsifleksio, ROM: {IsokinNilkkaDorsifleksioOik} / {IsokinNilkkaDorsifleksioVas} °
Nilkan plantaarifleksiomomentti: {IsokinNilkkaPlantaarifleksioMomenttiOikNormUn} / {IsokinNilkkaPlantaarifleksioMomenttiVasNormUn} Nm 
Nilkan plantaarifleksiomomentti (norm.): {IsokinNilkkaPlantaarifleksioMomenttiOikNorm} / {IsokinNilkkaPlantaarifleksioMomenttiVasNorm} Nm/kg
Nilkan liikenopeus, plantaarifleksio: {IsokinNilkkaLiikenopeusPlantaarifleksioOik} / {IsokinNilkkaLiikenopeusPlantaarifleksioVas} °/s
Nilkan dorsifleksiomomentti: {IsokinNilkkaDorsifleksioMomenttiOikNormUn} / {IsokinNilkkaDorsifleksioMomenttiVasNormUn} Nm
Nilkan dorsifleksiomomentti (norm.): {IsokinNilkkaDorsifleksioMomenttiOikNorm} / {IsokinNilkkaDorsifleksioMomenttiVasNorm} Nm/kg
Nilkan liikenopeus, dorsifleksio: {IsokinNilkkaLiikenopeusDorsifleksioOik} / {IsokinNilkkaLiikenopeusDorsifleksioVas} °/s
"""
