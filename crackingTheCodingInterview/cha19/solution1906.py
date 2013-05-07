#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Given an integer between 0 and 999,999, print an English phrase that
describes the integer (eg, “One Thousand, Two Hundred and Thirty
Four”).
"""

def __eng_seg_phrase(strn):
    # map 0-9 to phrase
    m1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
          'Eight', 'Nine']
    m2 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
          'Seventy', 'Eighty', 'Ninety']
    m3 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
          'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    s = ''
    if len(strn) == 3:
        s += m1[int(strn[0])] + ' Hundred'
        strn = strn[1:].lstrip('0')
        if not strn:
            return s
        s += ' and '
    if len(strn) == 2:
        if strn[0] == '1':
            return s + m3[int(strn)-10]
        else:
            s += m2[int(strn[0])]
            strn = strn[1:].lstrip('0')
            if strn:
                s += ' '
    if len(strn) == 1:
        return s + m1[int(strn)]
    return s


def eng_phrase(n):
    """Return English phrase for number n."""
    if n < 0 or n > 999999:
        return ''
    if n == 0:
        return 'Zero'

    strn = str(n)
    s = ''
    if len(strn) > 3:
        s += __eng_seg_phrase(strn[:-3]) + ' Thousand'
        strn = strn[-3:].lstrip('0')
        if not strn:
            return s
        s += ', '
    s += __eng_seg_phrase(strn[-3:])
    return s
