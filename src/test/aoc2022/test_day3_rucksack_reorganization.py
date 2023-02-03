from aoc2022.day3_rucksack_reorganization import RunsackReorganization
from common.FileReader import InMemoryFileReader

file_name = "202203.txt"
test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

file_reader = InMemoryFileReader()
file_reader.setup(file_name, test_data)

rucksack_reorganization = RunsackReorganization(
    file_name=file_name, file_reader=file_reader
)


def test_part_one_shared_item_priority_sum():
    result = rucksack_reorganization.duplicate_item_priority_sum()

    assert result == 157


def test_part_two_group_badge_item_priority_sum():
    result = rucksack_reorganization.group_badge_item_priority_sum()

    assert result == 70
