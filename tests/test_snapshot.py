import pathlib

from gilded_rose_python.gilded_rose import GildedRose
from gilded_rose_python.item import Item

ITEM_NAMES = [
    '+5 Dexterity Vest',
    'Aged Brie',
    'Backstage passes to a TAFKAL80ETC concert',
    'Arbitrary Item'
]


def test_gilded_rose_with_snapshot(snapshot):
    items = create_items()
    gilded_rose = GildedRose(items)

    snapshot_text = ''

    for runs in range(0, 4):
        snapshot_text += 'Run ' + str(runs) + '\n'
        gilded_rose.update_quality()
        snapshot_text += items_into_str(gilded_rose.items)

    snapshot.snapshot_dir = str(pathlib.Path(__file__).parent.resolve()) + '/snapshots'
    snapshot.assert_match(snapshot_text, 'snapshot.txt')


def items_into_str(items):
    snapshot_text = ''
    for item in items:
        snapshot_text += str(item) + '\n'
    return snapshot_text


def create_items():
    items = []
    for name in ITEM_NAMES:
        for sell_in in range(-1, 20):
            for quality in range(-1, 55):
                items.append(Item(name, sell_in, quality))
    return items
