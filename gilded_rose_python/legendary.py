from gilded_rose_python.item import Item


class Legendary(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def age(self):
        pass
