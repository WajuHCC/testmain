"""
1. napisz funkcje ktora wymnozy przez siebie elementy podane w liscie wejsciowej"""

def pomnoz(lista):
    wynik = 1
    for i in lista:
        wynik = wynik*i
    return wynik
tadam = [2,4,6,8,9]
print(pomnoz(tadam))

print()

def liczby(ciag):
    lista = list((ciag))
    wynik = []
    for i in lista:
        if i*2>0:
            wynik.append(i)
        else:
            break
    return
print(liczby("a8s8d8a8asda"))