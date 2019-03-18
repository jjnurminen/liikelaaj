# -*- coding: utf-8 -*-
""" Misc utility functions """

def _check_hetu(hetu):
    """ This checks validity of a Finnish social security number (hetu) """
    chrs = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if len(hetu) != 11:
        return False
    # check day and month
    pp, kk = int(hetu[:2]), int(hetu[2:4])
    if not (0 <= pp <= 31 and 1 <= kk <= 12):
        return False
    # check 'checksum'
    chk = chrs[(int(hetu[:6] + hetu[7:10])) % 31]
    if hetu[-1] != chk:
        return False
    return True

