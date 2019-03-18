# -*- coding: utf-8 -*-
"""
Configuration for liikelaajuus
"""

import sys
from datetime import date

# XXX: these should eventually go into a proper config file
class Config(object):
    """ The 'not measured' value for spinboxes. For regular spinboxes, this
    is the value that gets written to data files, but it does not affect
    the value shown next to the spinbox (which is set in Qt Designer).
    For the CheckDegSpinBox class, this is also the value shown next to the
    widget in the user interface. """
    spinbox_novalue_text = u'Ei mitattu'
    # 'yes' and 'no' values for checkboxes. Written to data files.
    checkbox_yestext = u'Kyllä'
    # the (silly) idea here was that by case sensitivity, 'EI' could be
    # changed in the reports by search&replace operations without affecting
    # other 'Ei' strings
    checkbox_notext = u'EI'
    # Set dirs according to platform
    if sys.platform == 'win32':
        tmp_fldr = '/Temp'
        # data_root_fldr = 'C:/'
        data_root_fldr = ('Z:/Other Data_May2013/ROM/ROM_' +
                          str(date.today().year))
    else:  # Linux
        tmp_fldr = '/tmp'
        data_root_fldr = '/'
    text_report_fldr = data_root_fldr + '/Raportit'
    excel_report_fldr = data_root_fldr + '/Raportit_Excel'
    tmpfile = tmp_fldr + '/liikelaajuus_tmp.json'
    # start of default Excel filename
    excel_report_prefix = 'Excel_'
    # start of default .txt filename
    text_report_prefix = 'Raportti_'
    # exceptions that might be generated when parsing and loading/saving json
    # these should all be caught
    json_io_exceptions = (UnicodeDecodeError, EOFError, IOError, TypeError)
    json_filter = u'JSON files (*.json)'
    text_filter = u'Text files (*.txt)'
    excel_filter = u'Excel files (*.xls)'
    global_fontsize = 11
    traceback_file = 'traceback.txt'
    help_url = 'https://github.com/jjnurminen/liikelaaj/wiki'
    # template paths
    xls_template = 'templates/rom_excel_template.xls'
    text_template = 'templates/text_template.py'
    # allowing multiple instances is problematic since they share the same
    # backup file (tmpfile)
    allow_multiple_instances = False

