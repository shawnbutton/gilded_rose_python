SULFURAS = "Sulfuras, Hand of Ragnaros"
CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.process_item(item)

    def process_item(self, item):
        if self.is_legendary(item):
            pass
        elif self.is_cheese(item):
            self.raise_quality(item)
            self.lower_sellin(item)
            if self.not_expired(item):
                self.raise_quality(item)
        else:
            if self.is_tickets(item):
                self.raise_quality(item)
                if item.sell_in < 11:
                    self.raise_quality(item)
                if item.sell_in < 6:
                    self.raise_quality(item)
            else:
                if self.not_worthless(item):
                    self.lower_quality(item)
            self.lower_sellin(item)
            if self.not_expired(item):
                if self.is_tickets(item):
                    item.quality = 0
                else:
                    if self.not_worthless(item):
                        self.lower_quality(item)

    def not_expired(self, item):
        return item.sell_in < 0

    def not_worthless(self, item):
        return item.quality > 0

    def is_legendary(self, item):
        return item.name == SULFURAS

    def is_tickets(self, item):
        return item.name == CONCERT_TICKETS

    def is_cheese(self, item):
        return item.name == BRIE

    def lower_sellin(self, item):
        item.sell_in = item.sell_in - 1

    def raise_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def lower_quality(self, item):
        item.quality = item.quality - 1
