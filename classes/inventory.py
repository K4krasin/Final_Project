class Inventory:
    def __init__(self, inv = []):
        self.inv = inv

    def item_in_inv(self, name):
        return name in self.inv


    def show_items(self):
        print(f'Your items: {self.inv}')
