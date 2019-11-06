"""
marchew: 2.35, ziemniaki: 2.20, cebula: 1.0, ogorki: 4.0

co chcesz kupic? marchew
ile chcesz kupic [marchew)

za [marchew] zaplacisz 7.05 PLN

dodac obsluge magazynu
"""

vege = {
    "marchew": 2.35,
    "ziemniaki": 2.20,
    "cebula": 1.0,
    "ogorki": 4.0
}
magazyn = {"marchew": 100,
           "ziemniaki": 300,
           "cebula": 50,
           "ogorki": 20
           }
print("W sprzedaży mamy nastepujace warzywa:")
for i in vege:
    print(f" - {i}: {vege[i]}")
print()

while True:
    tryb = input("Wybierz tryb: [z - zakupowy] [m - magazynowy")
    if tryb == "z":
        while True:
            x = input("Jakie warzywo chcesz kupic? [wpisz k by zakończyc]")
            if x == "k":
                break
            if x in vege:
                y = float(input(f"Podaj ilosc [{x}] jaka chcesz kupic: "))
                if y > magazyn[x]:
                    print("Sorry, nie mamy tyle w magazynie")
                    continue
                z = y * vege[x]
                print(f"Za [{x}] placisz: {z:.2f} PLN")
                magazyn[x] = magazyn[x] - y
            else:
                print("Brak towaru")
    if tryb == "m":
        towar = input("Podaj ktory towar chcesz uzupelnic:  ")
        dostawa = float(input("Podaj wielkosc dostawy: "))
        for towar in magazyn:
            magazyn[towar] = magazyn[towar] + dostawa

    for i in vege:
        print(f" - {i}: {magazyn[i]}")
print()

#funkcje
def stan_magazynowy():
    for i in vege:
        print(f" - {i}: {magazyn[i]}")
