#!/usr/bin/env python3
"""LIFOCache module"""

from base_caching import BaseCaching
from typing import Optional, List


class LIFOCache(BaseCaching):
    """ A caching system that implements the Last-In-First-Out
    (LIFO) algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order: List[str] = []

    def put(self, key: str, item: str) -> None:
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_item_key = self.order.pop()
                del self.cache_data[last_item_key]
                print(f"DISCARD: {last_item_key}")

            self.cache_data[key] = item

    def get(self, key: str) -> Optional[str]:
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
