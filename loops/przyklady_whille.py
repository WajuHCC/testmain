#losowanie

import random #importujemy modul random
print(dir(random))
print(help(random.randint))
print(random.randint(1, 10))

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

print("Położenie gracza", gracz_x, gracz_y)
print("Położenie skarbu", skarb_x, skarb_y)

print(abs(100)) #zwraca wartość absolutną danego argumentu
print(abs(-100)) #zwraca wartość absolutną danego argumentu

odleglosc = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

while True:


