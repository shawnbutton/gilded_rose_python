LEGENDARY = "Sulfuras, Hand of Ragnaros"
CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def age(self):
        if self.is_cheese():
            self.raise_quality()
            self.lower_sellin()
            if self.not_expired():
                self.raise_quality()
        elif self.is_tickets():
            self.raise_quality()
            if self.sell_in < 11:
                self.raise_quality()
            if self.sell_in < 6:
                self.raise_quality()
            self.lower_sellin()
            if self.not_expired():
                self.quality = 0
        else:
            if self.not_worthless():
                self.lower_quality()
            self.lower_sellin()
            if self.not_expired():
                if self.not_worthless():
                    self.lower_quality()

    def not_expired(self):
        return self.sell_in < 0

    def not_worthless(self):
        return self.quality > 0

    def is_legendary(self):
        return self.name == LEGENDARY

    def is_tickets(self):
        return self.name == CONCERT_TICKETS

    def is_cheese(self):
        return self.name == BRIE

    def lower_sellin(self):
        self.sell_in = self.sell_in - 1

    def raise_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def lower_quality(self):
        self.quality = self.quality - 1
