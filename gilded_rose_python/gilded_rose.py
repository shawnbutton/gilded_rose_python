SULFURAS = "Sulfuras, Hand of Ragnaros"
CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if self.is_cheese(item) or self.is_tickets(item):
                self.raise_quality(item)
                if self.is_tickets(item):
                    if item.sell_in < 11:
                        self.raise_quality(item)
                    if item.sell_in < 6:
                        self.raise_quality(item)
            else:
                if item.quality > 0:
                    if self.is_legendary(item):
                        continue
                    self.lower_quality(item)
            if not self.is_legendary(item):
                self.lower_sellin(item)
            if item.sell_in < 0:
                if self.is_cheese(item):
                    self.raise_quality(item)
                else:
                    if self.is_tickets(item):
                        item.quality = 0
                    else:
                        if item.quality > 0:
                            if self.is_legendary(item):
                                continue
                            self.lower_quality(item)

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
