from aoc2022.day1_calorie_counting import calorie_counting
from common.FileReader import InMemoryFileReader

file_name = "year2022_day1_test.txt"
file_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_elf_with_most_calories():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, file_data)

    result = calorie_counting(file_name, file_reader=file_reader)

    assert result == 24000


def test_elf_with_most_calories_part_two():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, file_data)

    result = calorie_counting(file_name, file_reader=file_reader, top=3)

    assert result == 45000
