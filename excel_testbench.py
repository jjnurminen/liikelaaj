# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""


from xlrd import open_workbook
from xlutils.copy import copy


def _getOutCell(outSheet, colIndex, rowIndex):
    """ HACK: Extract the internal xlwt cell representation. """
    row = outSheet._Worksheet__rows.get(rowIndex)
    if not row: return None

    cell = row._Row__cells.get(colIndex)
    return cell

def setOutCell(outSheet, col, row, value):
    """ Change cell value without changing formatting. """
    # HACK to retain cell style.
    previousCell = _getOutCell(outSheet, col, row)
    # END HACK, PART I

    outSheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx
    # END HACK
            
def get_field(s):
    """ If cell value is a field (variable name), return the name """
    if s and s[0] == '{' and s[-1] == '}':
        return s[1:-1]
    else:
        return None

fname_template = "C:/Users/HUS20664877/Desktop/Ubuntu_share/ROM-muuttujat.xls"
fname_save = "C:/Users/HUS20664877/Desktop/Ubuntu_share/output_test.xls"

rb = open_workbook(fname_template, formatting_info=True)
wb = copy(rb)
r_sheet = rb.sheet_by_index(0)
w_sheet = wb.get_sheet(0)

for row in range(r_sheet.nrows-100):
    for col in range(r_sheet.ncols):
        cl = r_sheet.cell(row, col)
        varname = get_field(cl.value)
        if varname:
            setOutCell(w_sheet, col, row, data_loaded[varname])
            
wb.save(fname_save)
            
        
        
    