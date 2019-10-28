#dict
print(dict())
x=dict()
print(type(x))
pol_ang = {
    #klucz : wartość
    "klucz": "wartość",
    "wartość": "value",
    "pies": "dog"
}
print(pol_ang)
print(pol_ang["pies"])
if "dog" in pol_ang:
    print(pol_ang["dog"])

print(pol_ang.get("dog"))
print(pol_ang.get("dog", "Brak takiego hasła"))
print(pol_ang.get("pies", "Brak takiego hasła"))

pol_ang["kot"] = "cat"
print(pol_ang)

print({1:"a", 2:"b"})
print({1.1:"a", 2.1:"b"})
#lista i slownik nie moze byc kluczem, ale tuple tak
print(pol_ang.keys())
print(pol_ang.values())
print(pol_ang.items())

print(dict(krowa="cow", dom="house"))
print(pol_ang.pop("pies"))
print(pol_ang)

# set - {}
# kolekcja unikalnych i nieuporzadkowanych wartosci

zbior = {1, 2, 3, 4}
print(zbior, type(zbior))
print(dir(zbior))
zbior2 = {1, "a", 2, "b", "c", "d"}
print(zbior2)
print(zbior2)
zbior2.add(9)
zbior2.add("a")
print(zbior2)

lista = [1,1,1,1,1,1,12,3,2,43,3,4,5,5,3]
print(set(lista))

A = {1, 2, 3, 4}
B = {3,4,5,6}
C = {1,2}
print("Suma zbiorów: ", A | B, A.union(B)) #tutaj sa dwie metody tego samego dlatego sie wyswietla podwojnie wynik
print("Różnica zbiorów: ", A - B, A.difference(B)) #tutaj sa dwie metody tego samego dlatego sie wyswietla podwojnie wynik
print("Czesc wspolna: ", A & B, A.intersection(B)) #tutaj sa dwie metody tego samego dlatego sie wyswietla podwojnie wynik
print("Roznica symetryczna: ", A ^ B, A.symmetric_difference(B))
print("Podzbior: ", A.issubset(B))
print("Podzbior: ", C.issubset(A))





