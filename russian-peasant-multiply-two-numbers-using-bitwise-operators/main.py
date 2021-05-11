def russianPeasant(a, b):
    res = 0
    while b > 0:
        if b % 2 == 1:
            res += a
        a *= 2
        b //= 2

    return res


assert 18 == russianPeasant(18, 1)
assert 240 == russianPeasant(20, 12)
