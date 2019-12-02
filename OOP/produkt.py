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

    _NEXT_ID = 1  #atrybut klasowy (gdyby zaczynalo sie od podkreslenia to jest to zmienna prywatna i powinna byc
    # modyfikowana wylacznie poprzez metody)
    def __init__Product(self, name, price):
        self.id = Product.NEXT_ID  #pobiera atrybut klasowy
        self.name = name
        self.price = price
        self.incr_next_id()

    @classmethod
    def incr_next_id(cls):
        cls.NEXT_ID += 1

    @classmethod
    def get_id(cls):
        return cls._NEXT_ID

    def show(self):
        print(self.name, self.id, self.price)

pr = Product(1, "Woda", 10.99)
pr.show()

