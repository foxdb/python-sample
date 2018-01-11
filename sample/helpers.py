def can_divide(a, b):
    is_int = isinstance(a, int) & isinstance(b, int)
    b_non_null = b != 0
    return is_int & b_non_null
