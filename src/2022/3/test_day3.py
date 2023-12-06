import pytest
from utils import read_txt
from day3 import RunsackReorganization

test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

data = read_txt(test_data)
rucksack_reorganization = RunsackReorganization(data)


def test_part_one_shared_item_priority_sum():
    result = rucksack_reorganization.duplicate_item_priority_sum()

    assert result == 157


def test_part_two_group_badge_item_priority_sum():
    result = rucksack_reorganization.group_badge_item_priority_sum()

    assert result == 70
