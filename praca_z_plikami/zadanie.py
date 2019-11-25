"""napisz funkcje, ktora otworzy podany jako argument plik (podana nazwa pliku lub sciezka) i wypisze numerując linie
#plik.txt
Raz Dwa Trzy

Wynik
1 Raz
2 Dwa
3 Trzy

Czesc 2
Pozwol na uruchomienie programu z konsoli testowej
#python numerator.py test
"""

print("Czesc 1")
def numerator(plik):
    wynik = {}
    dlugosc = len(plik)
    with open("plik.txt", encoding='UTF-8') as otw:
        for wyraz in otw:
            for cyfra in range(1:dlugosc):
                wynik = 

