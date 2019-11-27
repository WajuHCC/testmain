# """
# utworz klase produkt
# ktora bedzie:
#
# pr = Product(1, "woda", 10.99)
# pr.id
# 1
# pr.name
# woda
# pr.price
# 10.99
# pr.show()
# "Woda (1), cena: 10.99"
#
# """
class Product:
    def __init__Product(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.id, self.price)

pr = Product(1, "Woda", 10.99)
pr.show()

