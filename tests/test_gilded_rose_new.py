import pytest

from gilded_rose_python.gilded_rose_2 import GildedRose
from gilded_rose_python.item import Item


def makeItemList(name, sell_in, quality):
    return [Item(name, sell_in, quality)]


class TestGildedRose:

    def test_should_degrade_quality_each_day(self):
        items = makeItemList("foo", 6, 5)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 4

    def test_should_degrade_quality_twice_as_fast_after_sell_by_date(self):
        items = makeItemList("foo", 1, 5)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 4
        gilded_rose.update_quality()
        assert items[0].quality == 2

    def test_should_never_have_a_negative_quality(self):
        items = makeItemList("foo", 4, 0)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 0

    def test_should_increase_the_quality_of_aged_brie(self):
        items = makeItemList("Aged Brie", 4, 5)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 6

    def test_should_increase_quality_of_aged_brie_twice_as_fast_after_sellin(self):
        items = makeItemList("Aged Brie", 1, 10)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 11
        gilded_rose.update_quality()
        assert items[0].quality == 13

    def test_should_never_have_a_quality_greater_than_50(self):
        items = makeItemList("Aged Brie", 0, 50)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 50

    def test_should_not_degrade_the_quality_of_sulfuras(self):
        items = makeItemList("Sulfuras, Hand of Ragnaros", 0, 20)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 20

    def test_should_not_change_the_sellin_of_sulfuras(self):
        items = makeItemList("Sulfuras, Hand of Ragnaros", 10, 0)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 10

    def test_should_not_change_the_quality_of_sulfuras_even_if_created_with_sellin_passed(self):
        items = makeItemList("Sulfuras, Hand of Ragnaros", -1, 10)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 10

    def test_should_increase_quality_of_backstage_pass_twice_as_fast_when_less_than_10_days_remain(self):
        items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 11, 20)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 21
        gilded_rose.update_quality()
        assert items[0].quality == 23
        gilded_rose.update_quality()
        assert items[0].quality == 25

    def test_should_increase_quality_of_backstage_pass_three_times_as_fast_when_5_days_left(self):
        items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 6, 20)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 22
        gilded_rose.update_quality()
        assert items[0].quality == 25
        gilded_rose.update_quality()
        assert items[0].quality == 28

    def test_should_never_increase_quality_of_backstage_pass_past_maximum_even_if_close_to_concert(self):
        items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 5, 50)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 50

    def test_should_set_quality_to_zero_for_backstagepass_after_expires(self):
        items = makeItemList("Backstage passes to a TAFKAL80ETC concert", 1, 10)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 13
        gilded_rose.update_quality()
        assert items[0].quality == 0
        gilded_rose.update_quality()
        assert items[0].quality == 0

    # def test_conjured_items_decrease_in_quality_twice_as_fast(self):
    #     items = makeItemList("Conjured Mana Cake", 3, 10)
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #
    #     assert items[0].quality == 8

