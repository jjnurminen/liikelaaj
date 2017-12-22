# -*- coding: utf-8 -*-
"""

misc utility stuff for liikelaajuus application

@author: jussi (jnu@iki.fi)
"""

import io
import json


fn_emptyvals = "testdata/empty.json"
fn_out = "variable_list.txt"

# write out variable list as text
with io.open(fn_emptyvals, 'r', encoding='utf-8') as f:
    data_emptyvals = json.load(f)
with io.open(fn_out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(data_emptyvals.keys())))
