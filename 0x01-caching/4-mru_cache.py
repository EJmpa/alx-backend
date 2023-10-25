#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching
from typing import Optional, List


class MRUCache(BaseCaching):
    """ A caching system that implements the Most
    Recently Used (MRU) algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order: List[str] = []

    def put(self, key: str, item: str) -> None:
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.order.pop()
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key: str) -> Optional[str]:
        """ Get an item by key """
        if key is not None:
            if key in self.cache_data:
                # Move the accessed key to the end of the order list
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
