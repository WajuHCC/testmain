"""
Napisz funkcje zwracającą zbiór wszsystkich znaków występujących w zadanym napisie
więcej niż podana liczba razy
np:
>>> wiecej_niz("ala ma kota a kot ma ale", 3)
{'a', }
"""
def wiecej_niz():
    return set()
def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("") == set() #nie {}
