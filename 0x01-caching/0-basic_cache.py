#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching
from typing import Optional


class BasicCache(BaseCaching):
    """ A basic caching system that inherits from BaseCaching """

    def put(self, key: str, item: str) -> None:
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: str) -> Optional[str]:
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
