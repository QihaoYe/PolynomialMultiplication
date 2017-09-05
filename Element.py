#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Yee_172'
__data__ = '2017/8/28'

# from copy import deepcopy


def ftoi(num):
    """ Float to int if it has no decimal """
    return int(num) if int(num) == num else num


def dtos(num):
    """ Digit to Simply digit """
    return ftoi(round(num, 16))


def stos(string):
    """ String to Simply digit """
    return dtos(float(string))


class Indeterminate:
    """ A member of the term """
    def __init__(self, unknown, subscript=None, degree=1):
        if not isinstance(unknown, str):
            raise Exception('Name of indeterminate must be string!')
        if not isinstance(subscript, str) and subscript is not None:
            raise Exception('Subscript must be string!')
        if isinstance(degree, bool) or isinstance(degree, str):
            raise Exception('Degree must be int or float!')

        if degree:
            self.unknown = unknown
            self.subscript = subscript
            self.degree = dtos(degree)
        else:
            self.unknown = ''
            self.subscript = None
            self.degree = 0

    def tolist(self):
        """ Return a list of its info """
        return [self.unknown, self.subscript, self.degree]

    def __str__(self):
        """ Return a string means the same """
        if not self.unknown:
            return '1'
        elif self.degree == 1:
            if self.subscript:
                return '%s_%s' % (self.unknown, self.subscript)
            else:
                return self.unknown
        else:
            if self.subscript:
                return '%s_%s^%s' % (self.unknown, self.subscript, str(self.degree))
            else:
                return '%s^%s' % (self.unknown, str(self.degree))

    def showdetail(self, spaces=0):
        """ Print detailed info """
        if not isinstance(spaces, int):
            raise Exception('The number of spaces must be integer!')

        print(' '*spaces + 'unknown  :\t    %s' % self.unknown)
        print(' '*spaces + 'subscript:\t    %s' % self.subscript)
        print(' '*spaces + 'degree   :\t    %s' % str(self.degree))

    def __eq__(self, other):
        """ Judge if two indeterminates are equal """
        if not isinstance(other, Indeterminate):
            raise Exception('Must compare with an indeterminate!')

        if self.unknown == other.unknown:
            if self.subscript == other.subscript:
                if self.degree == other.degree:
                    return True
        return False

    def __ne__(self, other):
        """ Judge if two indeterminates are not equal """
        return False if self == other else True

    def ismultiplicative(self, other):
        """ Judge if two indeterminates can multpily """
        if not isinstance(other, Indeterminate):
            raise Exception('Must compare with an indeterminate!')

        if not self.unknown and not self.subscript:
            return True
        if not other.unknown and not other.subscript:
            return True
        if self.unknown == other.unknown:
            if self.subscript == other.subscript:
                return True
        return False

    def __mul__(self, other):
        """ Multiply two multiplicative indeterminates """
        if not isinstance(other, Indeterminate):
            raise Exception('Indeterminate must be valid!')
        if not self.ismultiplicative(other):
            raise Exception('Multiplicative indeterminate acquired!')

        if not self.unknown and not self.subscript:
            return other
        degree = self.degree + other.degree
        return Indeterminate(self.unknown, self.subscript, degree) if degree else CONSTANT

    def __truediv__(self, other):
        """ Divide a indeterminate by another """
        return self * Indeterminate(other.unknown, other.subscript, -other.degree)


CONSTANT = Indeterminate('', degree=0)


class Term:
    """ A member of the polynomial """
    def __init__(self, *indeterminates, coefficient=1):
        if isinstance(coefficient, bool) or isinstance(coefficient, str):
            raise Exception('Coefficient must be valid!')
        for each in indeterminates:
            if not isinstance(each, Indeterminate):
                raise Exception('Each indeterminate must be valid!')

        # Sort the indeterminates by indeterminate and subscript
        indeterminates = sorted(indeterminates, key=lambda x: x.subscript or '', reverse=True)
        indeterminates = sorted(indeterminates, key=lambda x: x.unknown)
        index = 0
        while 1:
            if index >= len(indeterminates)-1:
                break
            try:
                indeterminates = indeterminates[:index]\
                                 + [indeterminates[index] * indeterminates[index+1]]\
                                 + indeterminates[index+2:]
            except:
                index += 1

        if coefficient:
            self.indeterminates = indeterminates or [CONSTANT]
            self.coefficient = dtos(coefficient)
            self.degree = dtos(sum(each.degree for each in indeterminates))
        else:
            self.indeterminates = [CONSTANT]
            self.coefficient = 0
            self.degree = 0

    def tolist(self):
        """ Return a list of its info """
        return [[each.tolist() for each in self.indeterminates], self.coefficient, self.degree]

    def __str__(self):
        """ Return a string means the same """
        pass  # TODO term.tostring

    def showdetail(self, spaces=0):
        """ Print detailed info """
        print(' '*spaces + 'number of indeterminates:\t    %d' % len(self.indeterminates))
        print(' '*spaces + 'coefficient             :\t    %s' % str(self.coefficient))
        print(' '*spaces + 'degree                  :\t    %s' % str(self.degree))
        for n, each in enumerate(self.indeterminates):
            print(' '*spaces + 'indeterminate#%02d:' % (n+1))
            each.showdetail(5+spaces)

    def isincreasable(self, other):
        """ Judge if two terms is increasable """
        if not isinstance(other, Term):
            raise Exception('Must compare with a term!')

        if self.degree == other.degree:
            if len(self.indeterminates) == len(other.indeterminates):
                for n, each in enumerate(other.indeterminates):
                    if self.indeterminates[n] != each:
                        return False
                return True
        return False

    def __add__(self, other):
        """ Add two terms """
        pass  # TODO add

    def __sub__(self, other):
        """ Subtract two terms """
        pass  # TODO sub

    def __mul__(self, other):
        """ Multiply two terms """
        pass  # TODO mul

    def __truediv__(self, other):
        """ Divide two terms """
        pass  # TODO div


ZERO_TERM = Term(coefficient=0)


class Polynomial:
    """ A set of terms """
    def __init__(self, *terms):
        for each in terms:
            if not isinstance(each, Term):
                raise Exception('Each term must be valid!')

        # Sort the terms by degree and number of indeterminates
        terms = sorted(terms, key=lambda x: len(x.indeterminates))
        terms = sorted(terms, key=lambda x: x.degree, reverse=True)

        self.terms = terms
        self.degree = terms[0].degree

    def tolist(self):
        """ Return a list of its info """
        return [[each.tolist() for each in self.terms], self.degree]

    def __add__(self, other):
        """ Add polynomials together """
        if not isinstance(other, Polynomial):
            if not isinstance(other, int):
                if not isinstance(other, float):
                    raise Exception('Each polynomial must be valid!')

        try:
            other = Polynomial(Term(CONSTANT, coefficient=other))
        except:
            pass
        finally:
            print(other.tolist())


# ---[test zone]---
a = Indeterminate('x', subscript='1', degree=1)
b = Indeterminate('y', subscript='3', degree=2)
c = Indeterminate('x', subscript='2', degree=4)
d = Indeterminate('x', subscript='1', degree=1)
T1 = Term(a, b, c, a, coefficient=5)
T2 = Term(a, a, b, coefficient=3)
T3 = Term(c, c, coefficient=4)
T4 = Term(coefficient=-1)
T5 = Term(a, b, d)
P = Polynomial(T2, T1, T3, T4)
# c.multiply(c).showdetail()
T1.showdetail()
# P.add(5).tostring())
# print([i.tolist() for i in T1.indeterminates])
# print(T1.tolist())
# print([i.tolist() for i in P.terms])
# print(P.tolist())
# print(T2.isincreasable(T5))
# P+1
