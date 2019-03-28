# -*- coding: utf-8 -*-
"""

Qt Designer plugin for CheckDegSpinBox

@author: Jussi (jnu@iki.fi)
"""

from liikelaaj.liikelaajuus import CheckDegSpinBox
from PyQt5 import QtDesigner


class CheckDegSpinBoxPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return CheckDegSpinBox(parent)

    def name(self):
        return "CheckDegSpinBox"

    def group(self):
        return "Liikelaajuus"

    def isContainer(self):
        return False

    def includeFile(self):
        return "liikelaaj.liikelaajuus"
