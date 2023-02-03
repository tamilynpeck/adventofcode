from aoc2022.day3_rucksack_reorganization import rucksack_reorganization
from common.FileReader import InMemoryFileReader

file_name = "202203.txt"
test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_rucksack_reorganization_part_one():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)

    result = rucksack_reorganization(file_name=file_name, file_reader=file_reader)

    assert result == 157
