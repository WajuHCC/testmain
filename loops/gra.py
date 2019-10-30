import random
DEBUG = True

print("""
Witaj, Twoim zadaniem jest odnalezenie skarbu!
Mozesz poruszac sie wpisujac komendy:
w - gora
s - dół
d - w prawo
a - lewo
UWAZAJ, mozesz wypasc poza plansze.
Po kazdym ruchu dostaniesz info o tym czy sie zblizasz czy oddalasz.

ZACZYNAMY""")
#teraz wylosujemy początkowe połozenia gracza i skarbu

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

#obliczam odległość po wylosowaniu

odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

#w zależnosci od wartosci zmiennej DEBUG
#printuje info o polozeniu
if DEBUG:
    print(f"Położenie gracza (x={gracz_x}, y={gracz_y})")
    print(f"Położenie skarbu (x={skarb_x}, y={skarb_y})")
    print(f"Minimalna liczba ruchów = {odleglosc_po_wylosowaniu}")

liczba_ruchow = 0
while True:
    #pytamy gracza o ruch - ruch = input
    ruch = input("Wpisz komende (a - lewo, d - prawo, w - gora, s - dol)")
    odleglosc_przed = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    liczba_ruchow = liczba_ruchow + 1
    #zmieniamy pozycje gracza zgodnie z komenda
    if ruch == "a":
        gracz_x = gracz_x - 1
    elif ruch =="s":
        gracz_y = gracz_y - 1
    elif ruch == "d":
        gracz_x = gracz_x + 1
    elif ruch == "w":
        gracz_y = gracz_y + 1
    else:
        print("Trzymaj sie regul!!!!!!!")



    if DEBUG:
        print(f"Położenie gracza po ruchu (x={gracz_x}, y={gracz_y})")
        print(f"Położenie skrbu (x={skarb_x}, y={skarb_y})")

    # sprawdzenie po ruchu
    odleglosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    if not (1<= gracz_x <= 10 and 1<= gracz_y <= 10):
        print("Wypadłeś poza planszę !!!!!!!")
        break
    if odleglosc_po_ruchu == 0:
        print("BRAWO, WYGRALES")
        break


    if DEBUG:
        print()
        print("#" * 40)
        print(f"Odl przed: {odleglosc_przed}")
        print(f"Odl po: {odleglosc_po_ruchu}")
    #sprawdyam cyz sie ybliyzlem cyz oddalilem
    szansa = random.randint(1, 5)
    if szansa != 1:
        if odleglosc_po_ruchu < odleglosc_przed :
            print("Ciepło")
        else:
            print("Bez zmian")
    else:
        print("Sorry, nie bedzie wskazowki")

    if liczba_ruchow > 2* odleglosc_po_wylosowaniu:
        print("Sorki, polozenie skarbu sie zmienilo")
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)