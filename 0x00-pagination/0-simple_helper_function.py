#!/usr/bin/env python3
"""
Simple Helper Function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indices for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
