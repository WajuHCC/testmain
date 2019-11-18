"""
obliczanie silni
"""
import time
#na podstawie rekurencki
#n! = n*(n-1)!

def silnia_rek(n):
    if n<=1:
        return 1
    else:
        return n*silnia_rek(n-1)

def silnia_iter(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik
print(silnia_rek(998))
print(silnia_iter(999))

ts1 = time.time()
for i in range(0, 1000):
    silnia_rek(800)
ts2 = time.time()
print("Czas rekurencji:", ts2-ts1)

ts1 = time.time()
for i in range(0, 1000):
    silnia_iter(800)
ts2 = time.time()
print("Czas iteracji:", ts2-ts1)