# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:37:47 2016

@author: jussi
"""

from pandas import DataFrame

class html():

    def __init__(self, data):
        self.data = data
        
    def multiline_to_html(self, str):
        """ Convert multiline string to html """
        html_output = []
        for li in str.splitlines():
            html_output.append('<p>'+li+'</p>')
        return ''.join(html_output)
        
    def comments(self, comments):
        """ Make comments field into HTML """
        if comments:
            return u'<h2>Kommentit</h2>'+'\n'+self.multiline_to_html(comments)
        else:
            return ''

    def html_table(self, data):
        """ Make a multicolumn html table. data is a list of rows
        (list of lists of str) """
        table = ['<table style="width:100%">']
        for row in data:
            table.append['<tr>']
            for item in row:
                table.append('<td>'+item+'</td>')
            table.append['</tr>']
        table.append['</table>']
        return ''.join(table)
        
    def doc_header(self):
        return u"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" /> 
</head>
<body>
<h1>Kävelyanalyysi</h1>
"""

    def doc_terminator(self):
        return u"""
</body>
</html>
"""

    def sec_tiedot(self):
        return u"""
<h2>Potilaan tiedot</h2>
<table style="width:100%">
  <tr>
    <td>Potilaan nimi</td>
    <td>{lnTiedotNimi}</td> 
  </tr>
  <tr>
    <td>Potilaskoodi</td>
    <td>{lnTiedotID}</td> 
  </tr>
  <tr>
    <td>Päivämäärä</td>
    <td>{lnTiedotPvm}</td> 
  </tr>
  <tr>
    <td>Diagnoosi</td>
    <td>{lnTiedotDiag}</td> 
  </tr>
  <tr>
    <td>Henkilötunnus</td>
    <td>{lnTiedotHetu}</td> 
  </tr>
  <tr>
    <td>Mittaajat</td>
    <td>{lnTiedotMittaajat}</td> 
  </tr>
</table>""".format(**self.data) + self.comments(self.data['cmtTiedot'])

    def sec_liikelaajuudet(self):
        return u"""
<h2>Nivelten passiiviset liikelaajuudet</h2>
<h3>Lonkka</h3>
<table style="width:100%">
  <tr>
    <td>Potilaan nimi</td>
    <td>{lnTiedotNimi}</td> 
  </tr>
  <tr>"""
    
        
        
        

    def make(self):
        return self.doc_header() + self.sec_tiedot() + self.doc_terminator()

    def excel(self, fn):
        """ Export report to Excel (filename fn) TODO"""
        # example (two columns:)
        # df = DataFrame( {'Item': list_items, 'Value': list_values} )
        # df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
        
        
        
           
    

     
     
     
 


