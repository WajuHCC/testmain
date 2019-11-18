"""
funkcja z dowolna liczba parametrow
funkcja iloczyn mnozy wartosci podane do jej srodka - mozliwe podanie nieznanej liczby parametrow
"""
def iloczyn(*args):
    wynik = 1
    for nr, arg in enumerate(args,1):
        #print(f"Pozycja {nr} = {arg}")
        wynik *= arg
    return wynik

print(iloczyn(1,2,3,10,24,-9, -2))

def iloczyn(start, *args):
    wynik = start
    for nr, arg in enumerate(args,1):
        #print(f"Pozycja {nr} = {arg}")
        wynik *= arg
    return wynik

print(iloczyn(2,2,3,10,24,-9, -2))