"""
funkcje anonimowe
"""

x = lambda a, b : a*b
print(x(10,6))

def fun_sort(x):
    return x[1]

lista=[('Jablko', 2.99), ("Winogrona", 7.99),("Banan", 4.99)]
print(sorted(lista, key=fun_sort(x)))
