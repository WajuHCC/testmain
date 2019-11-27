"""
otworz plik - czytaj plik
1. utworz 2 slowniki Login i Logout
"""
# def login_time(input_file):
logins = {}
logouts = {}
with open("logs.txt") as f:
    for rekord in f:
        lista = rekord.split(";")
        if lista[1] == "LOGIN":
            logins.update({lista[0]:lista[2]})
        else:
            logouts.update({lista[0]:lista[2]})

    print(logins)
    print(logouts)


# login_time(dane/logs.txt)