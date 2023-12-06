import pytest
from utils import read_txt
from day4 import CampCleanup

test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_part_one_fully_overlapping():
    data = read_txt(test_data)
    camp_cleanup = CampCleanup(data)

    result = camp_cleanup.find_fully_overlapping()

    assert result == 2


def test_part_two_is_overlapping():
    data = read_txt(test_data)
    camp_cleanup = CampCleanup(data)

    result = camp_cleanup.find_overlapping()

    assert result == 4
