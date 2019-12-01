# slowniki z kodem Baudot - AI2 version - uzywane do dekodowania
letters = {"00000": "null", "00100": " ", "10111": "Q", "10011": "W", "00001": "E", "01010": "R", "10000": "T",
           "10101": "Y", "00111": "U", "00110": "I", "11000": "O", "10110": "P", "00011": "A", "00101": "S",
           "01001": "D", "01101": "F", "11010": "G", "10100": "H", "01011": "J", "01111": "K", "10010": "L", "10001": "Z",
           "11101": "X", "01110": "C", "11110": "V", "11001": "B", "01100": "N", "11100": "M",
           "01000": "Carriage Return CR", "00010": "Line Feed LF", "11011": "↑", "11111": "↓"}
digits = {"00000": "null", "00100": " ", "10111": "1", "10011": "2", "00001": "3", "01010": "4", "10000": "5",
          "10101": "6", "00111": "7", "00110": "8", "11000": "9", "10110": "0", "00011": "-", "00101": "BELL",
          "01001": "$", "01101": "!", "11010": "&", "10100": "#", "01011": "'", "01111": "(", "10010": ")",
          "10001": '"', "11101": "/", "01110": ':', "11110": ";", "11001": "?", "01100": ",", "11100": ".",
          "01000": "Carriage Return CR", "00010": "Line Feed LF", "11011": "↑", "11111": "↓"}

# odwrocone slowniki Baudot - uzywane do kodowania
inv_letters = dict(zip(letters.values(), letters.keys()))
inv_digits = dict(zip(digits.values(), digits.keys()))

# dekodowanie
new_tape = []


def decode(tape):
    for point in tape:
        char = letters.get(point)  # TODO: dodać pobieranie ze slownika digits
        new_tape.append(char)
    print(" ".join(new_tape))


# kodowanie
new_reply = []


def encode(text):
    for character in text:
        code = inv_letters.get(character)  # TODO: dodac pobieranie ze slownika digits
        new_reply.append(code)
    print(" ".join(new_reply))
# TODO: dodac przełączanie modulu kodowanie dekodowanie

# pobieranie tekstu do zakodowania od uzytkownika i formatowanie
txt = input("Wpisz text do dalekopisu: ")
# TODO: dodac komunikat o bledzie w przypadku uzycia znakow diaktrycznych
final = list(txt.upper())
encode(final)

tasma = ["11111", "10111", "00111", "00110", "01110", "01111", "00100", "11001", "01010", "11000", "10011", "01100",
         "00100", "01101", "11000", "11101", "00100", "01011", "00111", "11100", "10110", "00101", "00100", "11000",
         "11110", "00001", "01010", "00100", "10000", "10100", "00001", "00100", "10010", "00011", "10001", "10101",
         "00100", "01001", "11000", "11010", "00100", "00011", "10010", "10000", "00001", "01010", "01100",
         "00011", "10000", "00110", "11110", "00001", "00100", "00111", "01110", "10001", "01110", "00110", "00001",
         "00100", "00101", "00110", "00001", "00100", "10110", "10101", "10000", "10100", "11000", "01100", "00011",
         "00100", "01111", "10000", "11000", "00100", "10001", "01010", "11000", "11001", "00110", "10010", "00100",
         "01100", "00110", "00001", "01110", "10100", "00100", "10001", "00011", "10110", "10101", "10000", "00011",
         "00100", "11000", "00100", "01100", "00011", "11010", "01010", "11000", "01001", "00001"]

odp = ["P", "Y", "T", "A", "M", " ", "O", " ", "N", "A", "G", "R", "O", "D", "E"]

# decode(tasma)
# encode(odp)
