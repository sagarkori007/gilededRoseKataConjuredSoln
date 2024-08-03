"""
Unit tests for the GildedRose inventory management system.

This test suite uses the `unittest` framework to
verify the correctness of the `GildedRose` class and its associated
methods. The tests cover various aspects of the inventory system,
including the update logic for different types of
items as defined in the GildedRose Kata.
"""
# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    """
    Unit tests for the GildedRose inventory management system.

    This test suite is designed to validate the functionality of the `GildedRose` class. It uses Python's built-in
    `unittest` framework to ensure that the inventory system behaves correctly according to the rules defined
    in the Gilded Rose Kata.
    """

    def test_foo(self) -> None:
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_default(self) -> None:
        """
        Test the default behavior of items in the GildedRose inventory system.
        This method checks that the `update_quality` function in the GildedRose class correctly updates the `sell_in`
        and `quality` attributes according to the specified rules for normal items.
        """
        items = [
            Item(name="Lightning spell", sell_in=10, quality=20),
            Item(name="Healing spell", sell_in=5, quality=7),
            Item(name="Invisibility spell", sell_in=1, quality=3),
            Item(name="Freeze spell", sell_in=1, quality=48)
        ]

        gilded_rose = GildedRose(items)
        #For first day
        gilded_rose.update_quality()
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(19, gilded_rose.items[0].quality)
        self.assertEqual(4, gilded_rose.items[1].sell_in)
        self.assertEqual(6, gilded_rose.items[1].quality)
        self.assertEqual(0, gilded_rose.items[2].sell_in)
        self.assertEqual(2, gilded_rose.items[2].quality)
        self.assertEqual(0, gilded_rose.items[3].sell_in)
        self.assertEqual(47, gilded_rose.items[3].quality)
        #for 2nd day
        gilded_rose.update_quality()
        self.assertEqual(8, gilded_rose.items[0].sell_in)
        self.assertEqual(18, gilded_rose.items[0].quality)
        self.assertEqual(3, gilded_rose.items[1].sell_in)
        self.assertEqual(5, gilded_rose.items[1].quality)
        self.assertEqual(-1, gilded_rose.items[2].sell_in)
        self.assertEqual(0, gilded_rose.items[2].quality)
        self.assertEqual(-1, gilded_rose.items[3].sell_in)
        self.assertEqual(45, gilded_rose.items[3].quality)
        #For 3rd day
        gilded_rose.update_quality()
        self.assertEqual(7, gilded_rose.items[0].sell_in)
        self.assertEqual(17, gilded_rose.items[0].quality)
        self.assertEqual(2, gilded_rose.items[1].sell_in)
        self.assertEqual(4, gilded_rose.items[1].quality)
        self.assertEqual(-2, gilded_rose.items[2].sell_in)
        self.assertEqual(0, gilded_rose.items[2].quality)
        self.assertEqual(-2, gilded_rose.items[3].sell_in)
        self.assertEqual(43, gilded_rose.items[3].quality)

    def test_aged_brie(self) -> None:
        """
        Test the behavior of the "Aged Brie" item in the GildedRose inventory system.
        """
        item_name = "Aged Brie"
        items = [
            Item(name=item_name, sell_in=2, quality=0),
            Item(name=item_name, sell_in=5, quality=48),
            Item(name=item_name, sell_in=-2, quality=46),
        ]

        gilded_rose = GildedRose(items)
        #for 1st day
        gilded_rose.update_quality()
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        self.assertEqual(1, gilded_rose.items[0].quality)
        self.assertEqual(4, gilded_rose.items[1].sell_in)
        self.assertEqual(49, gilded_rose.items[1].quality)
        self.assertEqual(-3, gilded_rose.items[2].sell_in)
        self.assertEqual(48, gilded_rose.items[2].quality)
        #for 2nd day
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(2, gilded_rose.items[0].quality)
        self.assertEqual(3, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-4, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)
        #for 3rd day
        gilded_rose.update_quality()
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(4, gilded_rose.items[0].quality)
        self.assertEqual(2, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-5, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)
        #for 4th day
        gilded_rose.update_quality()
        self.assertEqual(-2, gilded_rose.items[0].sell_in)
        self.assertEqual(6, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-6, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)

    def test_sulfuras(self) -> None:
        """
        Test the behavior of the "Sulfuras, Hand of Ragnaros" item in the GildedRose inventory system.
        """
        item_name = "Sulfuras, Hand of Ragnaros"
        items = [
            Item(name=item_name, sell_in=0, quality=80),
            Item(name=item_name, sell_in=-1, quality=80)
        ]

        gilded_rose = GildedRose(items)
        #for 1st day
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[1].sell_in)
        self.assertEqual(80, gilded_rose.items[1].quality)
        #for 2nd day
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[1].sell_in)
        self.assertEqual(80, gilded_rose.items[1].quality)

    def test_backstage_passes(self) -> None:
        """
        Test the behavior of the "Backstage passes to a TAFKAL80ETC concert" item in the GildedRose inventory system.
        """

        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [
            Item(name=item_name, sell_in=15, quality=20),
            Item(name=item_name, sell_in=10, quality=49),
            Item(name=item_name, sell_in=6, quality=42),
            Item(name=item_name, sell_in=2, quality=32),
        ]

        gilded_rose = GildedRose(items)
        #for 1st day
        gilded_rose.update_quality()
        self.assertEqual(14, gilded_rose.items[0].sell_in)
        self.assertEqual(21, gilded_rose.items[0].quality)
        self.assertEqual(9, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(5, gilded_rose.items[2].sell_in)
        self.assertEqual(44, gilded_rose.items[2].quality)
        self.assertEqual(1, gilded_rose.items[3].sell_in)
        self.assertEqual(35, gilded_rose.items[3].quality)
        #for 2nd day
        gilded_rose.update_quality()
        self.assertEqual(13, gilded_rose.items[0].sell_in)
        self.assertEqual(22, gilded_rose.items[0].quality)
        self.assertEqual(8, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(4, gilded_rose.items[2].sell_in)
        self.assertEqual(47, gilded_rose.items[2].quality)
        self.assertEqual(0, gilded_rose.items[3].sell_in)
        self.assertEqual(38, gilded_rose.items[3].quality)
        #for 3rd day
        gilded_rose.update_quality()
        self.assertEqual(12, gilded_rose.items[0].sell_in)
        self.assertEqual(23, gilded_rose.items[0].quality)
        self.assertEqual(7, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(3, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)
        self.assertEqual(-1, gilded_rose.items[3].sell_in)
        self.assertEqual(0, gilded_rose.items[3].quality)
        #for 4th day
        gilded_rose.update_quality()
        self.assertEqual(11, gilded_rose.items[0].sell_in)
        self.assertEqual(24, gilded_rose.items[0].quality)
        self.assertEqual(6, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(2, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)
        self.assertEqual(-2, gilded_rose.items[3].sell_in)
        self.assertEqual(0, gilded_rose.items[3].quality)

    def test_conjured(self) -> None:
        """
        Test the behavior of the "Conjured Mana Cake" item in the GildedRose inventory system.
        """

        item_name = "Conjured Mana Cake"
        items = [Item(name=item_name, sell_in=3, quality=5),
                 Item(name=item_name, sell_in=1, quality=32)
                 ]

        gilded_rose = GildedRose(items)
        #for 1st day
        gilded_rose.update_quality()
        self.assertEqual(2, gilded_rose.items[0].sell_in)
        self.assertEqual(3, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[1].sell_in)
        self.assertEqual(30, gilded_rose.items[1].quality)
        #for 2nd day
        gilded_rose.update_quality()
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        self.assertEqual(1, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[1].sell_in)
        self.assertEqual(26, gilded_rose.items[1].quality)
        #for 3rd day
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(-2, gilded_rose.items[1].sell_in)
        self.assertEqual(22, gilded_rose.items[1].quality)
        #for 4th day
        gilded_rose.update_quality()
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(-3, gilded_rose.items[1].sell_in)
        self.assertEqual(18, gilded_rose.items[1].quality)


if __name__ == '__main__':
    unittest.main()
