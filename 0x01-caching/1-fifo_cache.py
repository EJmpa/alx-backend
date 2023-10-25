#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching
from typing import Optional, List


class FIFOCache(BaseCaching):
    """ A caching system that implements the First-In-First-Out
    (FIFO) algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order: List[str] = []

    def put(self, key: str, item: str) -> None:
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key: str) -> Optional[str]:
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
