#
#typ danych: napisy (string)
#
napis1 = "Ala ma kota"
napis2 = 'Ala ma kota'
print(napis1)
napis3= 'A to jest "cudzysłów" '
napis4= "A to jest \"cudzysłów\" "
print(napis4)
napis5 = "Znaki specjalne: \t \n \r "
print(napis5)

dlugosc = len(napis1)
print(dlugosc)
print(napis3)

wiek = input("Podaj wiek:")
print("Twój wiek to:", wiek.strip())
s = "Ruda tańczy jak szalona"
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.center(100))
print(s.replace("R","D"))
print("czy liczba:",s.isdecimal())

print("4-ta litera:",s[3]) #pobierz czwartą literę napisu
