lista = [1, 0, 10, "a"]

for i in lista:
    try:
        print(10 / i)  # test
    except ZeroDivisionError:
        print("dzielisz przez zero")
    except TypeError:
        print("dzielisz przez cos co nie jest liczba")
