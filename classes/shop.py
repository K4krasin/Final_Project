from classes.product import Product

class Shop:
    def __init__(self, products=[]):
        self.products = products

    def show_all(self):
        for index, item in enumerate(self.products):
            print(index, end=' - ')
            Product.product_show(item)

    def buy(self, index, wallet, level):
        selected = self.products[index]
        return Product.product_buy(selected, wallet, level)
