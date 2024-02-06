from gilded_rose_python.item import Item


class Brie(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def age(self):
        self.raise_quality()
        self.lower_sellin()
        if self.is_expired():
            self.raise_quality()


