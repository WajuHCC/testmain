# lista = [-2, 10, 0, 5, 1, 16, 9]
# wybierz_z_przedzialu(lista, 5, 10)

lista = [-2, 10, 0, 5, 1, 16, 9]

def wybierz_z_przedzialu(lista,x,y):
    wynik = []
    for i in lista:
        if i > x and i <y:
            wynik.append(i)
    return wynik


wybierz_z_przedzialu(lista,5,10)

def test_wybierz_z_przedzialu():
    assert test_wybierz_z_przedzialu([-2, 10, 0, 5, 1, 16, 9],5,10) == [10, 5, 9]
