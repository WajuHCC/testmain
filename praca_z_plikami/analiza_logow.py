"""
otworz plik - czytaj plik
1. utworz 2 slowniki Login i Logout
"""


def login_time(user):
    user_logins = []
    user_logouts = []
    with open("logs.txt") as f:
        for rekord in f:
            lista = rekord.split(";")
            if lista[0] == user and lista[1] == "LOGIN":
                user_logins.append(int(lista[2]))

            elif lista[0] == user and lista[1] == "LOGOUT":
                user_logouts.append(int(lista[2]))
        total_log = sum(user_logouts) - sum(user_logins)
        return print("Całowity czas zalogowania uzytkownika: " + user + " wynosi " + str(total_log))


def all_login_times(input_file):
    user_set = set()
    with open(input_file) as g:
        for rekord in g:
            user_set.add(rekord[0:6])
    user_names = sorted(user_set)
    for user in user_names:
        login_time(user)
    return


login_time("user-1")
login_time("user-2")
print()
all_login_times("logs.txt")
