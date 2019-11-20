"""
napisz funkcje, ktora zwroci max z podanych 3 liczb
max_of_three(10, 1, 17)
"""
print("A")
def max_of_three(a,b,c):
    lista_a=list((a,b,c))
    return max(lista_a)
print(max_of_three(1,4,8))
print(max_of_three(24,35,2))
print(max_of_three(-1,-35,-2))
print("B")

def bmax_of_three(a,b,c):
    lista_b = list((a, b, c))
    lista_b = sorted(lista_b)
    return lista_b[2]
print(bmax_of_three(24,35,2))
print("C")
# zrobic max_of_two i zagniezdzic