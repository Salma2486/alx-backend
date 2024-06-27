#!/usr/bin/env python3
"""task0"""
from typing import Tuple


def index_range(page, page_size)-> Tuple[int, int]:
    """index range"""
    return (page * page_size - page_size, page * page_size)
