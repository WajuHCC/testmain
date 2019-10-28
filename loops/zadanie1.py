#zapytaj uzytkownika 10 razy o  liczbe i wypisz ich srednia

lista = []
for liczba in range(10): #to range okresla zakres
    a = int(input("Podaj liczbe: "))
    lista.append(a)
print(sum(lista)/len(lista))



