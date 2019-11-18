"""
tworzenie rekordu pracownika
2 parametry obowiązkowe, 2 opcjonalne
ma zwrócić zmienną typu słownik
"""
def utworz_pracownika(imie, nazwisko, email="info@firma.pl", telefon=None):
    pracownik = dict()
    pracownik["imie"] = imie
    pracownik["nazwisko"] = nazwisko
    pracownik["email"] = email
    pracownik["telefon"] = telefon
    return pracownik
print(utworz_pracownika("Jan","Kowalski"))
print(utworz_pracownika("Adam","Nowak", "adam.nowak@firma.pl", "5767432"))
print(utworz_pracownika("Jan","Zielinski", telefon="0012345"))
print(utworz_pracownika("Jan","Zielinski", email="jzielinski@firma.pl"))

