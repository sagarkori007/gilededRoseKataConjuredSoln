"""
Gilded Rose Inventory Management

This module contains the implementation of the GildedRose inventory system,
which manages and updates the quality and
sell-in values of various items in inventory.
"""
# -*- coding: utf-8 -*-

class GildedRose(object):
    """Handles the item quality and sell-in updates."""

    def __init__(self, items) -> None:
        self.items = items

    def update_quality(self) -> None:
        modify_item = Modify()

        for item in self.items:
            if item.name == 'Sulfuras, Hand of Ragnaros':
                modify_item.update_sulfuras(item)
            elif item.name == 'Aged Brie':
                modify_item.update_aged_brie(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                modify_item.update_backstage_passes(item)
            elif item.name == 'Conjured Mana Cake':
                modify_item.update_conjured(item)
            else:
                modify_item.update_normal_item(item)

class Modify(object):
    """
    Handles the logic for updating item quality and sell-in values.
    This class contains methods for updating different types of items based on their
    specific rules.
    """

    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def update_normal_item(self, item) -> None:
        if item.sell_in > 0:
            decrease_by = -1
        else:
            decrease_by = -2
        item.quality = max((item.quality + decrease_by), self.MIN_QUALITY)
        item.sell_in -= 1

    def update_aged_brie(self, item) -> None:
        if item.sell_in > 0:
            increase_by = 1
        else:
            increase_by = 2
        item.quality = min((item.quality + increase_by), self.MAX_QUALITY)
        item.sell_in -= 1

    def update_sulfuras(self, item) -> None:
        # Sulfuras items do not change in quality or sell-in
        pass

    def update_backstage_passes(self, item) -> None:

        def get_quality(item, increase_by) -> None:
            item.quality = min(item.quality + increase_by, self.MAX_QUALITY)

        if item.sell_in > 10:
            increase_by = 1
            get_quality(item, increase_by)
        elif item.sell_in > 5:
            increase_by = 2
            get_quality(item, increase_by)
        elif item.sell_in > 0:
            increase_by = 3
            get_quality(item, increase_by)
        else:
            item.quality = 0
        item.sell_in -= 1

    def update_conjured(self, item) -> None:
        if item.sell_in > 0:
            depreciation = -2
        else:
            depreciation = -4

        item.quality = max((item.quality + depreciation), self.MIN_QUALITY)
        item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
