# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:37:47 2016

Create liikelaajuus (movement range) reports.

@author: jussi
"""

import text_templates
import string        
from xlrd import open_workbook
from xlutils.copy import copy

        

class Report():
    """ Make various reports based on the data. """    
    
    def __init__(self, data, vars_default, units):
        # convert values to Unicode and add corresponding units as suffices
        self.data = {key: unicode(data[key]) + units[key] for key in data}
        # list of variables which have default values (=no data was entered)
        self.vars_default = vars_default

    @staticmethod
    def get_field(s):
        """ Return all fields in a format string. """
        fi = string.Formatter()
        pit = fi.parse(s)  # returns parser generator
        for items in pit:
            if items[1]:
                yield items[1]  # = the field

    @staticmethod
    def backspace(s):
        """ Process \b chars in string, i.e. remove preceding char and the \b for each \b """
        sout = []
        for ch in s:
            if ch == '\b':
                if sout:
                    sout.pop()
            else:
                sout.append(ch)
        return ''.join(sout)
    
    @staticmethod
    def cond_format(s, di, fields_at_default):
        """ Conditionally format string s using dict di. If s has fields and
        they all are in the empty_fields list, an empty string is returned. 
        Otherwise all the fields are formatted, and any other (non-field) text 
        is returned as is. """
        flds = list(Report.get_field(s))
        if not flds or any([fld not in fields_at_default for fld in flds]):
            return s.format(**di)
        else:
            return ''
        
    def make_text_report(self):
        """ Generates the main text report. """
        # DEBUG: can edit template while running
        #reload(text_templates)
        ###
        # string replacements to do after formatting the whole report
        postprocess_dict = {'EI': 'Ei'}  
        report = text_templates.report
        # check which fields are (not) present in report
        flds_report = set(Report.get_field(''.join(report)))
        flds_data = set(self.data.keys())
        flds_cmn = flds_data.intersection(flds_report)
        not_in_rep = flds_data - flds_cmn
        if not_in_rep:
            print('Fields in data but not used in report:')
            for fld in sorted(not_in_rep):
                print(fld)
        # format fields and join into string
        rep_text = ''.join([Report.cond_format(s, self.data, self.vars_default) for s in report])
        # process backspaces
        rep_text = Report.backspace(rep_text)
        for it in postprocess_dict:
            rep_text = rep_text.replace(it, postprocess_dict[it])
        return rep_text

    def make_text_list(self):
        """ Return a simple list of all variables + values. """
        li = []
        for key in sorted(self.data):
            li.append(key+':'+unicode(self.data[key])+'\n')
        return u''.join(li)

    """ Next 2 xlrd hacks copied from: 
        http://stackoverflow.com/questions/3723793/
        preserving-styles-using-pythons-xlrd-xlwt-and-xlutils-copy?lq=1 """
    @staticmethod                    
    def _getOutCell(outSheet, colIndex, rowIndex):
        """ HACK: Extract the internal xlwt cell representation. """
        row = outSheet._Worksheet__rows.get(rowIndex)
        if not row:
            return None
        cell = row._Row__cells.get(colIndex)
        return cell

    @staticmethod                        
    def setOutCell(outSheet, col, row, value):
        """ Change cell value without changing formatting. """
        # HACK to retain cell style.
        previousCell = Report._getOutCell(outSheet, col, row)
        # END HACK, PART I
        outSheet.write(row, col, value)
        # HACK, PART II
        if previousCell:
            newCell = Report._getOutCell(outSheet, col, row)
            if newCell:
                newCell.xf_idx = previousCell.xf_idx
        # END HACK
                
    def make_excel(self, fn_save, fn_template):
        """ Export report to .xls file fn_save. Variables found in fn_template 
        are filled in. 
        fn_template should have Python-style format strings at cells that
        should be filled in, e.g. {TiedotNimi} would fill the cell using
        the corresponding key in self.data.
        fn_template must be in .xls (not xlsx) format, since formatting info
        cannot be read from xlsx (xlutils limitation). 
        xlrd and friends are weird, so this code is also weird. """
        # string replacements to do after a cell is formatted
        # WARNING: currently a bit hacky; watch out for unwanted changes
        postprocess_dict = {u'(EI)':'', u'(Kyllä)':u'(kl.)'}
        rb = open_workbook(fn_template, formatting_info=True)
        wb = copy(rb)
        r_sheet = rb.sheet_by_index(0)
        w_sheet = wb.get_sheet(0)
        # loop through cells, conditionally replace fields with variable names
        # for unknown reasons, wb and rb are very different structures,
        # so we read from rb and write to wb (using the hacky methods above)
        for row in range(r_sheet.nrows):
            for col in range(r_sheet.ncols):
                cl = r_sheet.cell(row, col)
                varname = cl.value
                if varname:
                    # conditionally format cell
                    newval = Report.cond_format(varname, self.data, 
                                                self.vars_default)
                    # apply replacement dict only if formatting actually did
                    # something. this is to avoid changing text-only cells.
                    if newval != varname:
                        for key in postprocess_dict:
                            if key in newval:
                                newval = newval.replace(key, postprocess_dict[key])
                    Report.setOutCell(w_sheet, col, row, newval)
        wb.save(fn_save)
        
        
        
        
        



