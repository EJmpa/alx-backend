#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching
from collections import defaultdict
from typing import Optional


class LFUCache(BaseCaching):
    """ A caching system that implements the Least
    Frequently Used (LFU) algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key: str, item: str) -> None:
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                least_frequent_keys = [
                    k for k, v in self.frequency.items() if v == min_frequency
                ]
                lru_key = least_frequent_keys[0]
                for k in least_frequent_keys:
                    if self.cache_data[k] in self.cache_data:
                        lru_key = k
                del self.frequency[lru_key]
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.frequency[key] += 1

    def get(self, key: str) -> Optional[str]:
        """ Get an item by key """
        if key is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
                return self.cache_data[key]
        return None
