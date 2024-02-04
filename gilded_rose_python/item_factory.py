from gilded_rose_python.item import Item
from gilded_rose_python.legendary import Legendary

LEGENDARY = "Sulfuras, Hand of Ragnaros"
CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"

class ItemFactory:
    @staticmethod
    def create_item(name, sell_in, quality):
        if name == LEGENDARY:
            return Legendary(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)