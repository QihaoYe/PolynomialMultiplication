#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/8/29'

from Element import *
# Indeterminate, Term, Polynomial, ftoi, dtos, stos


def advanced_split(string, *symbols, contain=False, linked='right'):
    """
    Split a string by symbols
    If contain is True, the result will contain symbols
    The choice of linked decides symbols link to which adjacent part of the result
    """
    if not isinstance(string, str):
        raise Exception('String must be str!')
    for each in symbols:
        if not isinstance(each, str):
            raise Exception('Symbol must be str!')
    linked = linked.lower()
    if linked not in ['left', 'right']:
        raise Exception('Linked must be left or right!')

    if not len(symbols):
        return [string]
    result = []
    symbols_len = tuple([len(each) for each in symbols])
    if contain:
        tail = ''
    while 1:
        index = len(string)
        num = -1
        for _num, each in enumerate(symbols):
            _index = string.find(each)
            if _index < index and _index + 1:
                index = _index
                num = _num
        if num == -1:
            temp = tail + string if contain and linked == 'right' and tail else string
            if temp:
                result.append(temp)
            break
        temp = string[:index]
        if contain and linked == 'left':
            tail = symbols[num]
        if contain:
            if tail:
                if linked == 'left':
                    temp = temp + tail
                if linked == 'right':
                    temp = tail + temp
        if contain and linked == 'right':
            tail = symbols[num]
        string = string[index+symbols_len[num]:]
        if temp:
            result.append(temp)

    return result


def str2term(string):
    """ Get a string, return a Term """
    # Ignore the spaces
    string = string.replace(' ', '')

    # Get the coefficient
    try:
        i = 2 if string[0] in ['+', '-'] else 1
        _coefficient = 1
        while 1:
            _coefficient = float(string[0:i])
            i += 1
            if i > len(string):
                break
    except:
        if string[0] == '-' and _coefficient == 1:
            _coefficient = -1

    # Get the indeterminates
    string = string[i-1:]
    indeterminates = []
    try:
        parts = string.split('*')
        for each in parts:
            underline = each.find('_')
            caret = each.find('^')
            if underline + 1 and caret + 1:
                _unknown = each[:underline]
                _subscript = each[underline+1:caret]
                _degree = each[caret+1:]
                if '_' in _subscript or '_' in _degree:
                    raise Exception
                if '^' in _degree:
                    raise Exception
                indeterminates.append(Indeterminate(_unknown, subscript=_subscript, degree=stos(_degree)))
            elif underline + 1:
                _unknown = each[:underline]
                _subscript = each[underline+1:]
                if '_' in _subscript:
                    raise Exception
                indeterminates.append(Indeterminate(_unknown, subscript=_subscript))
            elif caret + 1:
                _unknown = each[:caret]
                _degree = each[caret+1:]
                if '^' in _degree:
                    raise Exception
                indeterminates.append(Indeterminate(_unknown, degree=stos(_degree)))
            else:
                indeterminates.append(Indeterminate(each, degree=int(bool(each))))
    except:
        raise Exception('Example input: -4x_1^2*y_2^3')

    return Term(*indeterminates, coefficient=dtos(_coefficient))


def str2polynomial(string):
    """ Get a string, return a polynomial """
    try:
        parts = advanced_split(string, '+', '-', contain=True)
        terms = [str2term(each) for each in parts]
        return Polynomial(*terms)
    except:
        raise Exception('Example input: -5x_1^2*y_1^3+6x_2^2*y_2^4-x_3^1*y_3^1')
    

# ---[test zone]---
# print(advanced_split('-4x_1^2*y_2^3','^',contain=True,linked='left'))
# print(str2term('-4x_1^2*y_2^3').tolist())
print(str2polynomial('-5x_1^2 * y_3 + 6x_2^2 * y^ 4 - x*y +7').tolist())
