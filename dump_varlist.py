# -*- coding: utf-8 -*-
"""

Dump current variable list

@author: jussi (jnu@iki.fi)
"""

import sys
import io
from liikelaaj import liikelaajuus
from PyQt5 import QtWidgets

fn_out = "variable_list.txt"

app = QtWidgets.QApplication(sys.argv)  # needed for Qt stuff to function
eapp = liikelaajuus.EntryApp(check_temp_file=False)
with io.open(fn_out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(eapp.data.keys())))
