"""
funkcje anonimowe
"""

# x = lambda a, b : a*b
# print(x(10,6))
#
# def fun_sort(x):
#     return x[1]
#
# lista=[('Jablko', 2.99), ("Winogrona", 7.99),("Banan", 4.99)]
# print(sorted(lista, key=fun_sort(x)))

#napisz funkcje ktora z zadanej listy liczb wybierze elementy okreslone przez funkcje klucza
# lista = [1, 2, 3, 4 ,5, 6]
# wybierz (lista, key= lambda x: x%2 == 0)
# [ 2, 4, 6]
# wybierz (lista, key= lambda x: x%2 == 0)

lista = [1, 2, 3, 4 ,5, 6]
lista2 = []
def wybierz(lista, funkcja):
    lista2 = []
    for i in lista:
        if funkcja(i) is True:
            lista2.append(i)
    return lista2

print(wybierz(lista, lambda x: x%2 == 0))

data =[1, 2, 3, 4, 5, 6, 7]
def przytnij(data, start, stop):
    wynik = data
    for x in data:
        if start(x) and stop(x) is True:
            wynik.remove[start(x):stop(x)]
    return wynik

print(przytnij(data, lambda x: x>3, lambda x: x==6 ))
