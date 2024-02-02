import pytest

from gilded_rose_python.gilded_rose import GildedRose
from gilded_rose_python.item import Item

gilded_rose = GildedRose()


def makeItemList(name, sell_in, quality):
    return [Item(name, sell_in, quality]

class TestGildedRose:

    def test_should_degrade_quality_each_day:
      items = makeItemList("foo", 6, 5)
      items = GildedRose.update_quality(items)
      assert items[0].quality == 4


    # def test_should degrade quality twice as fast after sell by date:
    #   items = makeItemList("foo", 1, 5)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 4
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 2
    #
    #
    # def test_should never have a negative quality:
    #   items = makeItemList("foo", 4, 0)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 0
    #
    #
    # def test_should increase the quality of aged brie:
    #   items = makeItemList("Aged Brie", 4, 5)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 6
    #
    #
    # def test_should increase quality of aged brie twice as fast after sellin:
    #   items = makeItemList("Aged Brie", 1, 10)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 11
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 13
    #
    #
    # def test_should never have a quality greater than 50:
    #   items = makeItemList("Aged Brie", 0, 50)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 50
    #
    #
    # def test_should not degrade the quality of sulfuras:
    #   items = makeItemList("Sulfuras, Hand of Ragnaros", 0, 20)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 20
    #
    #
    # def test_should not change the sellin of sulfuras:
    #   items = makeItemList("Sulfuras, Hand of Ragnaros", 10, 0)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).sell_in == 10
    #
    #
    # def test_should not change the quality of sulfuras, even if created with sellin passed:
    #   items = makeItemList("Sulfuras, Hand of Ragnaros", -1, 10)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 10
    #
    #
    # def test_should increase quality of backstage pass twice as fast when less than 10 days remain:
    #   items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 11, 20)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 21
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 23
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 25
    #
    #
    # def test_should increase quality of backstage pass three times as fast when 5 days left:
    #   items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 6, 20)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 22
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 25
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 28
    #
    #
    # def test_should never increase quality of backstage pass past maximum, even if close to concert:
    #   items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 5, 50)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 50
    #
    #
    # def test_should set quality to zero for backstagepass after expires:
    #   items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 1, 10)
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 13
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 0
    #   items = GildedRose.update_quality(items)
    #   assert List.first(items).quality == 0


