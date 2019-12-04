from produkt import Product
from basket import Basket

class TestBasket:

    def test_add_produkt_to_basket(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert len(basket.items) == 1

    def count_total_price(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert basket.count




