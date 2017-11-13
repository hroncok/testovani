def tah(pole, znak, pozice):
    if pozice > 19:
        raise ValueError('takhle teda ne! pozice musí být do 19')
    if pozice < 0:
        raise ValueError('takhle teda ne! pozice musí být nezáporná')
    if znak != 'o' and znak != 'x':
        raise ValueError('hraj x nebo o!')
    return pole[:pozice] + znak + pole[pozice+1:]
