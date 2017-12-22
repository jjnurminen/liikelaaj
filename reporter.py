# -*- coding: utf-8 -*-
"""

Create reports for liikelaajuus

@author: Jussi (jnu@iki.fi)
"""


import string
from xlrd import open_workbook
from xlutils.copy import copy


""" Next 2 xlrd hacks copied from:
http://stackoverflow.com/questions/3723793/
preserving-styles-using-pythons-xlrd-xlwt-and-xlutils-copy?lq=1 """


def _getOutCell(outSheet, colIndex, rowIndex):
    """ HACK: Extract the internal xlwt cell representation. """
    row = outSheet._Worksheet__rows.get(rowIndex)
    if not row:
        return None
    cell = row._Row__cells.get(colIndex)
    return cell


def _setOutCell(outSheet, col, row, value):
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


class Report(object):
    """ A simple template engine. For example, a
    report text block may be "Name: {name} Age: {Age}" and the data may be
    {'Name': 'John', 'Age': 30}
    The fields in the text block are filled in using the data, resulting in
    the string "Name: John Age: 30"
    This is similar to Python text formatting, but it has a simple conditional
    formatting feature: if all the data for a given block are default, an
    empty block will be returned. The purpose is to easily generate reports
    where sections with missing data are not printed at all.
    """

    def __init__(self, data, fields_default):
        """ Init report with data dict."""
        # strings to replace in .xls cells (after filling the fields)
        self.cell_postprocess_dict = {u'(EI)': '', u'(Kyllä)': u'(kl.)'}
        self.text = ''
        self.data = data
        self.fields_default = fields_default
        self._item_separator = '. '

    def __add__(self, s):
        """ Format and add a text block to report """
        self.text += self._cond_format(s)
        return self

    def item_sep(self):
        """Insert item separator if it's not already at the end of text"""
        seplen = len(self._item_separator)
        if self.text[-seplen:] != self._item_separator:
            self.text += self._item_separator

    def __repr__(self):
        return self.text

    def _cond_format(self, s):
        """ Conditionally format string s. Fields given as {variable} are
        formatted using the data. If there is no data for any the fields, an
        empty string is returned. """
        flds = list(Report._get_field(s))
        if not flds or any([fld not in self.fields_default for fld in flds]):
            return s.format(**self.data)
        else:
            return ''

    @staticmethod
    def _get_field(s):
        """ Return list of fields in a format string, e.g.
        '{foo} is {bar}'  ->  ['foo', 'bar']  """
        fi = string.Formatter()
        pit = fi.parse(s)  # returns parser generator
        for items in pit:
            if items[1]:
                yield items[1]  # = the field

    def make_report(self, fn_template):
        """Create report using the template"""
        report = self
        execfile(fn_template)
        return self.text

    def make_excel(self, fn_save, fn_template):
        """ Export report to .xls file fn_save. Variables found in fn_template
        are filled in.
        fn_template should have Python-style format strings in cells that
        should be filled in, e.g. {TiedotNimi} would fill the cell using
        the corresponding key in self.data.
        fn_template must be in .xls (not xlsx) format, since formatting info
        cannot be read from xlsx (xlutils limitation).
        xlrd and friends are weird, so this code is also weird. """
        rb = open_workbook(fn_template, formatting_info=True)
        wb = copy(rb)
        r_sheet = rb.sheet_by_index(0)
        w_sheet = wb.get_sheet(0)
        # loop through cells, conditionally replace fields with variable names.
        # for unclear reasons, wb and rb are very different structures,
        # so we read from rb and write to corresponding cells of wb
        # (using the hacky methods above)
        for row in range(r_sheet.nrows):
            for col in range(r_sheet.ncols):
                cl = r_sheet.cell(row, col)
                varname = cl.value
                if varname:  # format non-empty cells
                    newval = self._cond_format(varname)
                    # apply replacement dict only if formatting actually did
                    # something. this is to avoid changing text-only cells.
                    if newval != varname:
                        for str, newstr in self.cell_postprocess_dict.iteritems():
                            if str in newval:
                                newval = newval.replace(str, newstr)
                    _setOutCell(w_sheet, col, row, newval)
        wb.save(fn_save)
