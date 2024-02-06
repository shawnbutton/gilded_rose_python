from gilded_rose_python.item import Item

SULFURAS = "Sulfuras, Hand of Ragnaros"

CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"

AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            process_item(item)


def process_item(item: Item):
    if is_brie(item) or is_tickets(item):
        raise_quality(item)
        if is_tickets(item):
            if item.sell_in < 11:
                raise_quality(item)
            if item.sell_in < 6:
                raise_quality(item)
    else:
        if is_sulfuras(item):
            return
        lower_quality(item)
    if is_sulfuras(item):
        pass
    else:
        lower_sell_in(item)
    if item.sell_in < 0:
        if is_brie(item):
            raise_quality(item)
        else:
            if is_tickets(item):
                item.quality = 0
            else:
                if is_sulfuras(item):
                    return
                lower_quality(item)


def lower_sell_in(item):
    item.sell_in = item.sell_in - 1


def lower_quality(item):
    if item.quality > 0:
        item.quality = item.quality - 1


def raise_quality(item):
    if item.quality < 50:
        item.quality = item.quality + 1


def is_sulfuras(item):
    return item.name == SULFURAS


def is_tickets(item):
    return item.name == CONCERT_TICKETS


def is_brie(item):
    return item.name == AGED_BRIE