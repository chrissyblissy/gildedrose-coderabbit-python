# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # helper for running a select number of days of depreciation
    def run_update_quality_n_times(self, items, days):
        gilded_rose = GildedRose(items)
        for _ in range(days):
            gilded_rose.update_quality()
        return items

    # helper for running 1 day of depreciation
    def run_update_quality_once(self, items):
        return self.run_update_quality_n_times(items, 1)

    def test_name_does_not_change_when_quality_updated(self):
        items = self.run_update_quality_once([Item("foo", 0, 0)])
        self.assertEqual("foo", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
