"""
napisać funkcje do obliczenia pola i obwodu kola
"""

from math import pi, sin

def oblicz_pole_kola(r):
    return pi*r**2

def oblicz_obwod_kola(r):
    return pi*2*r

def oblicz_pole_i_obwod_kola(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)

print(oblicz_pole_i_obwod_kola(10))