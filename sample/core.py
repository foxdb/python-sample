# -*- coding: utf-8 -*-
from . import helpers


def divide(a, b):
    if helpers.can_divide(a, b):
        return a / b

    return None


def modulo(a, b):
    quotient = divide(a, b)
    if quotient:
        return a - (quotient * b)

    return None
