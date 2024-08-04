# Gilded Rose Kata - Conjured Items Solution

## Overview

This project provides a Python solution to the Gilded Rose Kata, with a particular focus on handling Conjured items. The Gilded Rose Kata is a coding exercise that involves managing an inventory system with specific rules for different types of items.

The solution includes functionality for various item types, including the handling of Conjured items, which degrade in quality twice as fast as normal items.

## Features

- **Conjured Items**: Special handling for Conjured items, which degrade in quality at twice the rate of normal items.
- **Regular Items**: Implementation of standard behavior for regular items.
- **Aged Brie**: Special handling where the quality of Aged Brie increases as it ages.
- **Backstage Passes**: Quality changes based on the remaining sell-in days.
- **Sulfuras**: A legendary item that does not change in quality or sell-in.

## Solution Approach

### Classes and Methods

#### `GildedRose` Class

- **`__init__(self, items)`**: Initializes the class with a list of `Item` objects.
- **`update_quality(self)`**: Iterates through the list of items and updates each one based on its type using the `Modify` class.

#### `Modify` Class

- **Constants**:
  - `MAX_QUALITY`: The maximum allowable quality value for items (50).
  - `MIN_QUALITY`: The minimum allowable quality value for items (0).

- **Methods**:
  - **`update_normal_item(self, item)`**: Updates normal items by decreasing their quality and adjusting the sell-in value. If the sell-in value is negative, the quality decreases at a faster rate.
  - **`update_aged_brie(self, item)`**: Increases the quality of `Aged Brie` items. The quality increase is greater if the sell-in value is negative.
  - **`update_sulfuras(self, item)`**: Handles `Sulfuras` items, which do not change in quality or sell-in value.
  - **`update_backstage_passes(self, item)`**: Updates `Backstage Passes` with varying quality increases based on the sell-in value. The quality drops to 0 after the event.
  - **`update_conjured(self, item)`**: Updates `Conjured` items, which degrade in quality at twice the rate of normal items. Quality decreases faster when the sell-in value is negative.
