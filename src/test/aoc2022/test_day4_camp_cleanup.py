from aoc2022.day4_camp_cleanup import CampCleanup
from common.FileReader import InMemoryFileReader


file_name = "202204.txt"
test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

file_reader = InMemoryFileReader()
file_reader.setup(file_name, test_data)


def test_part_one_fully_overlapping():
    camp_cleanup = CampCleanup(file_name=file_name, file_reader=file_reader)

    result = camp_cleanup.find_fully_overlapping()

    assert result == 2


def test_part_two_is_overlapping():
    camp_cleanup = CampCleanup(file_name=file_name, file_reader=file_reader)

    result = camp_cleanup.find_overlapping()

    assert result == 4
