from piskvorky import tah
import pytest


def prazdne_pole():
    return '-' * 20


def test_tah_33_nejde():
    with pytest.raises(ValueError):
        pole = tah(prazdne_pole(), 'x', 33)


def test_hrat_teckama_nejde():
    with pytest.raises(ValueError):
        pole = tah(prazdne_pole(), '.', 2)


def test_tah_x0_je_prvni_x():
    pole = tah(prazdne_pole(), 'x', 0)
    assert pole == 'x' + ('-' * 19)


def test_tah_o2_je_treti_o():
    pole = tah(prazdne_pole(), 'o', 2)
    assert pole == '--o' + ('-' * 17)


def test_tah_do_plneho():
    pole = 'xoxoxoxo-oxoxoxoxoxo'
    pole = tah(pole, 'x', 8)
    assert pole == 'xo' * 10
