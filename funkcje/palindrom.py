#napisac funkcje ktora sprawdzi czy dane slowo jest palindromem tzn. czy jest taki sam czytany wstecz

# is palindrom("kajak") == True
# is palindrom("kot") == False

###
def is_palindrom(x):
    x = x.upper()
    x = x.replace(" ", "")
    x = x.replace(",", "")
    x = x.replace(".", "")
    y = x[::-1]
    if x == y:
        return True
    else:
        return False

def test_is_palindrom_for_palindrom():
    assert is_palindrom("kajak") is True
    assert is_palindrom("A to idiota") is True
    assert is_palindrom("Ada, gmina za nim gada.") is True


is_palindrom("ja pierdziu")
