#!/usr/bin/env python3
"""1-simple_pagination module"""

import csv
from logging import exception
import math
from shutil import ExecError
from typing import List, Tuple

index_range = __import__("0-simple_helper_function").index_range


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
        """get data set

        Args:
            page (int, optional): number of page. Defaults to 1.
            page_size (int, optional): size or limit of the page.
            Defaults to 10.

        Returns:
            List[List]: data set filtered by page indexes
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)
        start = indexes[0]
        end = indexes[1]

        try:
            return self.dataset()[start:end]
        except Exception:
            return []
