class Product:
    def __init__(self, name, strenght, intel, dex, price, level):
        self.name = name
        self.strenght = strenght
        self.intel = intel
        self.dex = dex
        self.price = price
        self.level = level

    def product_show(self):
        print(self.name.title(), self.strenght, self.intel, self.dex, self.price, self.level)

    def product_buy(self, money, level):
        if self.level > level:
            print('You dont have enuogh level')
        else:
            if money >= self.price:
                print('Sold')
                return self.name
            else:
                "Its too expensive"
