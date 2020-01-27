from django.http import HttpResponse

def funkcja_widoku(request):
    html = """<!doctype html>
    <html>
    <head></head>
    <body>
    HELLO ALX!!
    </body>
    </html>"""

    return HttpResponse(html)

def hello_name(request, name):
    html = f"""<!doctype html>
    <html>
    <head></head>
    <body>
    HELLO {name}!!
    </body>
    </html>"""
    return HttpResponse(html)

def sum(request, op, liczba1, liczba2): #praca domowa
    if op == sum:
        wynik = liczba1 +liczba2
    html = f"""<!doctype html>
    <html>
    <head></head>
    <body>
    HELLO {name}!!
    </body>
    </html>"""
    return HttpResponse(wynik)

#/sum/1/2 - uwaga bo
