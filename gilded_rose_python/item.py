LEGENDARY = "Sulfuras, Hand of Ragnaros"
CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def age(self):
        self.lower_quality()
        self.lower_sellin()
        if self.is_expired():
            self.lower_quality()

    def is_expired(self):
        return self.sell_in < 0

    def lower_sellin(self):
        self.sell_in = self.sell_in - 1

    def raise_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def lower_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1
