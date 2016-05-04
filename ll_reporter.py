# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:37:47 2016

Create liikelaajuus report.

@author: jussi
"""

#from pandas import DataFrame

import html_templates
import text_templates
import liikelaajuus
import string        
        

class Text():
    
    def __init__(self, data, units):
        # some special conversion for reporting purposes
        # add units as suffixes to data values
        self.data = {}
        # if value is in not_measured_vals, it's counted as not measured and the corresponding variable is ignored (not reported)
        self.not_measured_vals = [u'Ei mitattu', u'', u'EI']  # 'EI' is the checkbox (QtCheckBox) 'No' value
        # special values that don't take units as suffix
        self.nounits_vals = [u'NR', u'Ei']
        for fld in data:
            if data[fld] not in self.not_measured_vals+self.nounits_vals:
                self.data[fld] = unicode(data[fld])+units[fld]
            else:
                self.data[fld] = unicode(data[fld])


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
    def cond_format(s, di, emptyvals=[None]):
        """ Conditionally format string s using dict di: if all field values
        are in emptyvals list, return empty string. """
        flds = list(Text.get_field(s))
        if not flds or any([di[fld] not in emptyvals for fld in flds]):
            return s.format(**di)
        else:
            return ''
        
    def make_text_report(self):
        """ Generates the main text report. """
        # DEBUG: can edit template while running
        #reload(text_templates)
        ###
        postprocess_dict = {'EI': 'Ei'}  # after creating the report, strings can be replaced via this
        report = text_templates.report
        # check which fields are (not) present in report
        flds_report = set(Text.get_field(''.join(report)))
        flds_data = set(self.data.keys())
        flds_cmn = flds_data.intersection(flds_report)
        not_in_rep = flds_data - flds_cmn
        print('Fields in data but not used in report:')
        for fld in sorted(not_in_rep):
            print(fld)
        # format fields and join into string
        rep_text = ''.join([Text.cond_format(s, self.data, self.not_measured_vals) for s in report])
        # process backspaces
        rep_text = Text.backspace(rep_text)
        for it in postprocess_dict:
            rep_text = rep_text.replace(it, postprocess_dict[it])
        return rep_text
        

    def make_text_list(self):
        """ Make a simple list of all variables + values. """
        li = []
        for key in sorted(self.data):
            li.append(key+':'+unicode(self.data[key])+'\n')
        return u''.join(li)

    def excel(self, fn):
        """ Export report to Excel (filename fn) TODO"""
        # example (two columns:)
        # df = DataFrame( {'Item': list_items, 'Value': list_values} )
        # df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
        





class html():
    
    def __init__(self, data):
        self.data = data

    def multiline_to_html(self, str):
        """ Convert multiline string to html """
        html_output = []
        for li in str.splitlines():
            html_output.append('<p>'+li+'</p>')
        return ''.join(html_output)
        
    def format_comments(self, comments):
        """ Make given comments field (multiline string) into HTML """
        if comments:
            return u'<h2>Kommentit</h2>'+'\n'+self.multiline_to_html(comments)
        else:
            return ''

    def html_table(self, data):
        """ Make a multicolumn html table. data is a list of rows
        (list of lists of str). """
        table = ['<table style="width:100%">']
        for row in data:
            table.append['<tr>']
            for item in row:
                table.append('<td>'+item+'</td>')
            table.append['</tr>']
        table.append['</table>']
        return ''.join(table)
        
    def format_section(self, sec):
        # format html for given section & add comments field
        return html_templates.section[sec].format(**self.data)

    def make_html(self):
        # TODO: for key in html_templates.sections...
        return html_templates.header + self.sec_tiedot() + html_templates.footer

        
        
           
    

     
     
     
 


