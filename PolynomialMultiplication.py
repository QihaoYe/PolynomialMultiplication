#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/8/28'

from Element import *
from Func import *

x = Indeterminate('x')
y = Indeterminate('y')
z = Indeterminate('z')
alpha1 = Indeterminate('α', subscript='1')
alpha2 = Indeterminate('α', subscript='2')
alpha3 = Indeterminate('α', subscript='3')
beta1 = Indeterminate('β', subscript='1')
beta2 = Indeterminate('β', subscript='2')
beta3 = Indeterminate('β', subscript='3')
gamma1 = Indeterminate('γ', subscript='1')
gamma2 = Indeterminate('γ', subscript='2')
gamma3 = Indeterminate('γ', subscript='3')

# Δ = (x^2+y^2+z^2)^(1/2)
Δcosα = str2polynomial('α_1*x+α_2*y+α_3*z')
Δcosβ = str2polynomial('β_1*x+β_2*y+β_3*z')
Δcosγ = str2polynomial('γ_1*x+γ_2*y+γ_3*z')
cosαβ = str2polynomial('α_1*β_1+α_2*β_2+α_3*β_3')
cosαγ = str2polynomial('α_1*γ_1+α_2*γ_2+α_3*γ_3')
cosβγ = str2polynomial('β_1*γ_1+β_2*γ_2+β_3*γ_3')
a = Δcosα ** 2
print(a)
