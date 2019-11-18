"""
przekazywanie listy parametrow nazwanych

"""
def fun_parametry(**kwargs):
    print(kwargs)
fun_parametry(imie="Jan", nazwisko="Kowalski", email="jk@firma.pl", wiek="44")