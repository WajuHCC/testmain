import sys
file_name = sys.argv[1]


def ponumeruj(nazwa_pliku):
    with open(nazwa_pliku) as f:
        i = 1
        for line in f:
            print(i, line.rstrip())
            i += 1

ponumeruj(file_name)
