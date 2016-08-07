# Square root newton's method

def newtonSqrt(n):
    aprox = 0.5 * n
    valor = 0.5 *(aprox + n/aprox)
    while valor != aprox:
        aprox = valor
        valor = 0.5 * (aprox + n/aprox)
    return aprox

print newtonSqrt(127)
