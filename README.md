# PolynomialMultiplication
A little tool for polynomial multiplication\
Warning: '\(' & '\)' & '\[' & '\]' & '\{' & '\}' are not supported yet!!!
## PolynomialMultiplication.py
Main
## Element.py
A class container
### Indeterminate:
##### Example
'x'\
'x_1^2'\
'y_2^-1'\
'' -> CONSTANT


##### Supported operations
str()\
==\
\*\
/
### Term:
##### Example
'x\*y'\
'5x_1^2\*x_2^3\*x_3^4'\
'-3x^3\*y^-1'\
'0' -> ZERO_TERM


##### Supported operations
str()\
==\
\+\
\-\
\*\
/
### Polynomial:
##### Example
'3x^2\*y^2+4x\*y+7'\
'-5x_1^2\*y_1^-2-4'\
'-5x_1^2\*y_1^3+6x_2^2\*y_2^4-x_3^1\*y_3^1'\
'2'


##### Supported operations
str()\
==\
\+\
\-\
\*\
\**
