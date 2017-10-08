#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__data__ = '2017/8/28'

from Func import *


# ---[Example]---
P1 = str2polynomial('p_1+p_2-p_1*p_2')
P2 = str2polynomial('p_4+p_5-p_4*p_5')
P3 = str2polynomial('p_3')
P4 = str2polynomial('p_1*p_4+p_2*p_5-p_1*p_2*p_4*p_5')
P5 = str2polynomial('1-p_3')
print((P1*P2*P3+P4*P5).latex())
