import unittest


#napisz funkcje, ktora sprawdzi liczbe pierwsza
def czy_pierwsza(x):
    """ten obszar nazywa sie docstring i sluzy do tworzenia dokumentacji funkcji
    sprawdza czy x jest liczbą pierwszą
    Przykłady użycia:
    # przyklady uzycia doctestow
    >>> czy_pierwsza(10)
    False

    >>> czy_pierwsza(7)
    True
    """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
#prymitywna forma testow
#assert czy_pierwsza(2) is True
#assert czy_pierwsza (10) is False

#unittesty

# class TestCzyPierwsza(unittest.TestCase):
#
#     def test_czy_pierwsza_dla_liczby_pierwszej(self):
#         self.assertEqual(czy_pierwsza(7), True)
#         self.assertEqual(czy_pierwsza(17), True)
#         self.assertEqual(czy_pierwsza(13), True)
#     def czy_pierwsza_dla_liczby_niepierwszej(self):
#         self.assertIs(czy_pierwsza(10), False)
#         self.assertIs(czy_pierwsza(12), False)
#         self.assertIs(czy_pierwsza(20), False)

#do pytestu
def test_czy_pierwsza_dla_liczby_pierwszej(self):
    assert czy_pierwsza(7), True
    assert czy_pierwsza(17), True
    assert czy_pierwsza(13), True
def czy_pierwsza_dla_liczby_niepierwszej(self):
    assert czy_pierwsza(10), False
    assert czy_pierwsza(12), False
    assert czy_pierwsza(20), False