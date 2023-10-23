#!/usr/bin/env python3
"""
Simple Pagination
"""

import csv
import math
from typing import List, Dict, Union
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.

        Args:
            page (int): Page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(
        self,
        page: int = 1,
        page_size: int = 10
    ) -> Dict[str, Union[int, List[List], None]]:
        """
        Retrieve a hypermedia representation of a page of data.

        Args:
            page (int): Page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            Dict[str, Union[int, List[List], None]]: A dictionary with
            hypermedia information.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_data = self.get_page(page, page_size)
        next_page = page + 1 if len(page_data) > 0 else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hypermedia_info = {
            "page_size": page_size,
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return hypermedia_info
